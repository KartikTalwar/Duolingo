import json
import urllib2


class Struct:

    def __init__(self, **entries):
        self.__dict__.update(entries)



class Duolingo(object):

    def __init__(self, username):
        self.username  = username
        self.user_url  = "http://duolingo.com/users/%s" % self.username
        self.user_data = Struct(**self._get_data())


    def _get_data(self):
        get = urllib2.urlopen(self.user_url).read()
        return json.loads(get)


    def _make_dict(self, keys, array):
        data = {}

        for key in keys:
            if type(array) == dict:
                data[key] = array[key]
            else:
                data[key] = getattr(array, key, None)

        return data


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
        fields = ['username', 'bio', 'id', 'num_following', 'cohort',
                  'num_followers', 'learning_language_string', 'created',
                  'contribution_points', 'gplus_id', 'twitter_id', 'admin',
                  'invites_left', 'location', 'fullname', 'avatar']

        return self._make_dict(fields, self.user_data)


    def get_language_progress(self, lang):
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



if __name__ == '__main__':

    from pprint import pprint as pp

    duolingo   = Duolingo('kartik')
    settings   = duolingo.get_settings()
    languages  = duolingo.get_languages()
    lang_info  = duolingo.get_language_details('French')
    user_info  = duolingo.get_user_info()
    lang_prog  = duolingo.get_language_progress('fr')
    frnd_data  = duolingo.get_friends()

    pp(frnd_data)

