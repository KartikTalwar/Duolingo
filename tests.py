import os
import unittest
import duolingo

USERNAME = os.environ.get('DUOLINGO_USER', 'ferguslongley')
PASSWORD = os.environ.get('DUOLINGO_PASSWORD')


class DuolingoTest(unittest.TestCase):
    lingo = duolingo.Duolingo(USERNAME, password=PASSWORD)

    def setUp(self):
        self.lang = self.lingo.user_data.learning_language

    def test_get_user_info(self):
        response = self.lingo.get_user_info()

    def test_get_settings(self):
        response = self.lingo.get_settings()

    def test_get_languages(self):
        response = self.lingo.get_languages(abbreviations=False)
        response = self.lingo.get_languages(abbreviations=True)

    def test_get_friends(self):
        response = self.lingo.get_friends()

    def test_get_calendar(self):
        response = self.lingo.get_calendar()
        response = self.lingo.get_calendar(self.lang)

    def test_get_streak_info(self):
        response = self.lingo.get_streak_info()

    def test_get_certificates(self):
        response = self.lingo.get_certificates()

    def test_get_language_details(self):
        response = self.lingo.get_language_details(self.lang)

    def test_get_language_progress(self):
        response = self.lingo.get_language_progress(self.lang)

    def test_get_known_topics(self):
        response = self.lingo.get_known_topics(self.lang)

    def test_get_unknown_topics(self):
        response = self.lingo.get_unknown_topics(self.lang)

    def test_get_golden_topics(self):
        response = self.lingo.get_golden_topics(self.lang)

    def test_get_reviewable_topics(self):
        response = self.lingo.get_reviewable_topics(self.lang)

    def test_get_known_words(self):
        response = self.lingo.get_known_words(self.lang)

    def test_get_learned_skills(self):
        response = self.lingo.get_learned_skills(self.lang)

    def test_get_language_from_abbr(self):
        response = self.lingo.get_language_from_abbr(self.lang)

    def test_get_abbreviation_of(self):
        response = self.lingo.get_abbreviation_of('portuguese')

    def test_get_activity_stream(self):
        response = self.lingo.get_activity_stream()

    def test_get_translations(self):
        response = self.lingo.get_translations('e')
        response = self.lingo.get_translations('e', self.lang)
        response = self.lingo.get_translations('e', self.lang, 'fr')
        response = self.lingo.get_translations(['e', 'a'])

    @unittest.skipIf(not PASSWORD, "You must have valid username/password")
    def test_get_leaderboard(self):
        response = self.lingo.get_leaderboard('week')
        response = self.lingo.get_leaderboard('month')

    @unittest.skipIf(not PASSWORD, "You must have valid username/password")
    def test_get_vocabulary(self):
        response = self.lingo.get_vocabulary()
        response = self.lingo.get_vocabulary(self.lang)

    @unittest.skipIf(not PASSWORD, "You must have valid username/password")
    def test_get_audio_url(self):
        response = self.lingo.get_audio_url('o')
        response = self.lingo.get_audio_url('o', self.lang)

    @unittest.skipIf(not PASSWORD, "You must have valid username/password")
    def test_get_related_words(self):
        response = self.lingo.get_related_words('o')

if __name__ == '__main__':
    unittest.main()
