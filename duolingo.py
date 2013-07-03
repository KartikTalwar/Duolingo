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
            data[key] = getattr(array, key, None)

        return data


    def get_settings(self):
        keys = ['notify_comment', 'deactivated', 'is_follower_by', 'is_following']

        return self._make_dict(keys, self.user_data)



if __name__ == '__main__':

    from pprint import pprint as pp

    duolingo = Duolingo('kartik')
    settings = duolingo.get_settings()

    pp(settings)
