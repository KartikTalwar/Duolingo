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


    def get_user_info(self):
        data = self.user_data
        return data.id


if __name__ == '__main__':

    from pprint import pprint as pp

    duolingo = Duolingo('kartik')

    pp(duolingo.get_user_info())
