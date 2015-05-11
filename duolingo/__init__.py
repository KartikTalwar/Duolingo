import requests

try:
    import json
except ImportError:
    import simplejson as json

from operator import attrgetter
from werkzeug.datastructures import MultiDict

class Struct:

    def __init__(self, **entries):
        self.__dict__.update(entries)



class Duolingo(object):

    def __init__(self, username, password=None):
        self.username  = username
        self.password  = password
        self.user_url  = "http://duolingo.com/users/%s" % self.username
        self.session   = requests.Session()

        if password:
            self._login()

        self.user_data = Struct(**self._get_data())


    def _login(self):
        login_url = "https://www.duolingo.com/login"
        data = {"login":self.username, "password":self.password}
        attempt = self.session.post(login_url, data).json()

        if attempt.get('response') == 'OK':
            return True

        raise Exception("Login failed")


    def _switch_language(self, lang):
        data = {"learning_language" : lang}
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
        dependency_to_skill = MultiDict([ (skill['dependencies_name'][0]
                                           if len(skill['dependencies_name']) > 0 else '', skill)
                                          for skill in skills ])

        # Start with the first skill and trace the dependency graph through skill, setting the
        # order it was learned in.
        index = 0
        previous_skill = ''
        while True:
            for skill in dependency_to_skill.getlist(previous_skill):
                skill['dependency_order'] = index
            index += 1

            # Figure out the canonical dependency for the next set of skills.
            skill_names = set([ skill['name'] for skill in dependency_to_skill.getlist(previous_skill)])
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


    def get_languages(self):
        data = []

        for lang in self.user_data.languages:
            if lang['learning']:
                data.append(lang['language_string'])

        return data


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


    def get_language_progress(self, lang):
        current_lang = self.user_data.language_data.keys()

        if lang not in current_lang:
            self._switch_language(lang)

        fields = ['streak', 'language_string', 'level_progress', 'num_skills_learned',
                  'level_percent', 'level_points', 'points_rank', 'next_level',
                  'level_left', 'language', 'points']

        return self._make_dict(fields, self.user_data.language_data[lang])


    def get_friends(self):
        for k,v in self.user_data.language_data.iteritems():
            data = []
            for friend in v['points_ranking_data']:
                temp = {'username' : friend['username'], 'points' : friend['points_data']['total']}
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
        skills = [ skill for skill in self.user_data.language_data[lang]['skills'] ]

        self._compute_dependency_order(skills)

        return [ skill for skill in sorted(skills, key=lambda skill: skill['dependency_order']) if skill['learned'] ]

    def get_known_topics(self, lang):
        topics = []
        for topic in self.user_data.language_data[lang]['skills']:
            if topic['learned']:
                topics.append(topic['title'])

        return topics



if __name__ == '__main__':

    from pprint import pprint as pp

    duolingo   = Duolingo('kartik')
    settings   = duolingo.get_settings()
    languages  = duolingo.get_languages()
    lang_info  = duolingo.get_language_details('French')
    user_info  = duolingo.get_user_info()
    lang_prog  = duolingo.get_language_progress('fr')
    frnd_data  = duolingo.get_friends()
    known_wrds = duolingo.get_known_words('fr')
    knowntopic = duolingo.get_known_topics('fr')

    pp(knowntopic)

