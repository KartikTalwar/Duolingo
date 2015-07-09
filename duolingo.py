import re
import json
import requests
from werkzeug.datastructures import MultiDict

class Struct:

    def __init__(self, **entries):
        self.__dict__.update(entries)


class Duolingo(object):

    def __init__(self, username, password=None):
        self.username = username
        self.password = password
        self.user_url = "http://duolingo.com/users/%s" % self.username
        self.session = requests.Session()

        if password:
            self._login()

        self.user_data = Struct(**self._get_data())

    def _login(self):
        login_url = "https://www.duolingo.com/login"
        data = {"login": self.username, "password": self.password}
        attempt = self.session.post(login_url, data).json()

        if attempt.get('response') == 'OK':
            return True

        raise Exception("Login failed")

    def get_activity_stream(self, before=None):
        if before:
            url = "https://www.duolingo.com/stream/{}?before={}".format(self.user_data.id, before)
        else:
            url = "https://www.duolingo.com/activity/{}".format(self.user_data.id)
        request = self.session.get(url)
        try:
            return request.json()
        except:
            raise Exception('Could not get activity stream')

    def _switch_language(self, lang):
        data = {"learning_language": lang}
        url = "https://www.duolingo.com/switch_language"
        request = self.session.post(url, data)

        try:
            parse = request.json()['tracking_properties']
            if parse['learning_language'] == lang:
                self.user_data = Struct(**self._get_data())
        except:
            raise Exception('Failed to switch language')

    def _get_data(self):
        get = self.session.get(self.user_url).json()
        return get

    def _make_dict(self, keys, array):
        data = {}

        for key in keys:
            if type(array) == dict:
                data[key] = array[key]
            else:
                data[key] = getattr(array, key, None)

        return data

    def _compute_dependency_order(self, skills):
        """ Add a field to each skill indicating the order it was learned
            based on the skill's dependencies. Multiple skills will have the same
            position if they have the same dependencies.
        """
        # Key skills by first dependency. Dependency sets can be uniquely
        # identified by one dependency in the set.
        dependency_to_skill = MultiDict([(skill['dependencies_name'][0]
                                        if len(skill['dependencies_name']) > 0 else '', skill)
                                        for skill in skills])

        # Start with the first skill and trace the dependency graph through skill, setting the
        # order it was learned in.
        index = 0
        previous_skill = ''
        while True:
            for skill in dependency_to_skill.getlist(previous_skill):
                skill['dependency_order'] = index
            index += 1

            # Figure out the canonical dependency for the next set of skills.
            skill_names = set([skill['name'] for skill in dependency_to_skill.getlist(previous_skill)])
            canonical_dependency = skill_names.intersection(set(dependency_to_skill.keys()))
            if canonical_dependency:
                previous_skill = canonical_dependency.pop()
            else:
                # Nothing depends on these skills, so we're done.
                break

        return skills

    def get_settings(self):
        keys = ['notify_comment', 'deactivated', 'is_follower_by', 'is_following']

        return self._make_dict(keys, self.user_data)

    def get_languages(self, abbreviations=False):
        data = []

        for lang in self.user_data.languages:
            if lang['learning']:
                if abbreviations:
                    data.append(lang['language'])
                else:
                    data.append(lang['language_string'])

        return data

    def get_language_from_abbr(self, abbr):
        for language in self.user_data.languages:
            if language['language'] == abbr:
                return language['language_string']
        return None

    def get_abbreviation_of(self, name):
        for language in self.user_data.languages:
            if language['language_string'] == name:
                return language['language']
        return None

    def get_language_details(self, language):
        for lang in self.user_data.languages:
            if language == lang['language_string']:
                return lang

        return {}

    def get_user_info(self):
        fields = ['username', 'bio', 'id', 'num_following', 'cohort', 'language_data',
                  'num_followers', 'learning_language_string', 'created',
                  'contribution_points', 'gplus_id', 'twitter_id', 'admin',
                  'invites_left', 'location', 'fullname', 'avatar', 'ui_language']

        return self._make_dict(fields, self.user_data)

    def get_certificates(self):
        for certificate in self.user_data.certificates:
            certificate['datetime'] = certificate['datetime'].strip()

        return self.user_data.certificates

    def get_streak_info(self):
        fields = ['daily_goal', 'site_streak', 'streak_extended_today']
        return self._make_dict(fields, self.user_data)

    def _is_current_language(self, abbr):
        return abbr in self.user_data.language_data.keys()

    def get_calendar(self, language_abbr=None):
        if language_abbr:
            if not self._is_current_language(language_abbr):
                self._switch_language(language_abbr)
            return self.user_data.language_data[language_abbr]['calendar']
        else:
            return self.user_data.calendar

    def get_language_progress(self, lang):
        if not self._is_current_language(lang):
            self._switch_language(lang)

        fields = ['streak', 'language_string', 'level_progress', 'num_skills_learned',
                  'level_percent', 'level_points', 'points_rank', 'next_level',
                  'level_left', 'language', 'points', 'fluency_score', 'level']

        return self._make_dict(fields, self.user_data.language_data[lang])

    def get_friends(self):
        for k, v in self.user_data.language_data.iteritems():
            data = []
            for friend in v['points_ranking_data']:
                temp = {'username': friend['username'], 'points': friend['points_data']['total']}
                temp['languages'] = [i['language_string'] for i in friend['points_data']['languages']]
                data.append(temp)

            return data

    def get_known_words(self, lang):
        words = []
        for word in self.user_data.language_data[lang]['skills']:
            if word['learned']:
                words += word['words']

        return set(words)

    def get_learned_skills(self, lang):
        """ Return the learned skill objects sorted by the order they were
            learned in.
        """
        skills = [skill for skill in self.user_data.language_data[lang]['skills']]

        self._compute_dependency_order(skills)

        return [skill for skill in sorted(skills, key=lambda skill: skill['dependency_order'])
                if skill['learned']]

    def get_known_topics(self, lang):
        topics = []
        for topic in self.user_data.language_data[lang]['skills']:
            if topic['learned']:
                topics.append(topic['title'])

        return topics

    def get_translations(self, words, source=None, target=None):
        if not source:
            source = self.user_data.ui_language
        if not target:
            target = self.user_data.language_data.keys()[0]

        word_parameter = json.dumps(words, separators=(',', ':'))
        url = "https://d2.duolingo.com/api/1/dictionary/hints/{}/{}?tokens={}".format(
            target, source, word_parameter)

        request = self.session.get(url)
        try:
            return request.json()
        except:
            raise Exception('Could not get translations')

    def get_vocabulary(self, language_abbr=None):
        if language_abbr and not self._is_current_language(language_abbr):
            self._switch_language(language_abbr)

        overview_url = "https://www.duolingo.com/vocabulary/overview"
        overview_request = self.session.get(overview_url)
        overview = overview_request.json()

        return overview

    _cloudfront_server_url = None

    def _cloudfront_server(self):
        if self._cloudfront_server_url:
            return self._cloudfront_server_url

        homepage_url = "https://www.duolingo.com"
        request = self.session.get(homepage_url)
        server_list = re.search('//.+\.cloudfront\.net', request.text)
        self._cloudfront_server_url = "https:{}".format(server_list.group(0))

        return self._cloudfront_server_url

    def get_audio_url(self, word, language_abbr=None):
        if not language_abbr:
            language_abbr = self.user_data.language_data.keys()[0]
        return "{}/tts/{}/token/{}".format(self._cloudfront_server(), language_abbr, word)

    def get_related_words(self, word, language_abbr=None):
        if language_abbr and not self._is_current_language(language_abbr):
            self._switch_language(language_abbr)

        overview_url = "https://www.duolingo.com/vocabulary/overview"
        overview_request = self.session.get(overview_url)
        overview = overview_request.json()

        for word_data in overview['vocab_overview']:
            if word_data['normalized_string'] == word:
                related_lexemes = word_data['related_lexemes']
                return [w for w in overview['vocab_overview'] if w['lexeme_id'] in related_lexemes]


attrs = [
    'settings', 'languages', 'user_info', 'certificates', 'streak_info',
    'calendar', 'language_progress', 'friends', 'known_words',
    'learned_skills', 'known_topics', 'activity_stream', 'vocabulary'
]

for attr in attrs:
    getter = getattr(Duolingo, "get_" + attr)
    prop = property(getter)
    setattr(Duolingo, attr, prop)


if __name__ == '__main__':

    from pprint import pprint as pp

    duolingo = Duolingo('kartik')
    knowntopic = duolingo.get_known_topics('fr')

    pp(knowntopic)
