import json
import urllib2


class Duolingo(object):

    def __init__(self, username):
        self.username  = username
        self.user_url  = "http://duolingo.com/users/%s" % self.username
        self.user_data = self._get_data()


    def _get_data(self):
        get = urllib2.urlopen(self.user_url).read()
        return json.loads(get)




if __name__ == '__main__':

    from pprint import pprint as pp

    duolingo = Duolingo('kartik')

    pp(duolingo.user_data)
