import os
import unittest
from datetime import datetime

import duolingo

USERNAME = os.environ.get('DUOLINGO_USER', 'ferguslongley')
PASSWORD = os.environ.get('DUOLINGO_PASSWORD')


class DuolingoTest(unittest.TestCase):
    lingo = duolingo.Duolingo(USERNAME, PASSWORD)

    def setUp(self):
        self.lang = self.lingo.user_data.learning_language

    def test_get_user_info(self):
        response = self.lingo.get_user_info()
        assert isinstance(response, dict)
        assert "avatar" in response
        assert "id" in response
        assert "location" in response
        assert "learning_language_string" in response

    def test_get_settings(self):
        response = self.lingo.get_settings()
        assert isinstance(response, dict)
        assert "deactivated" in response

    def test_get_languages(self):
        response1 = self.lingo.get_languages(abbreviations=False)
        assert isinstance(response1, list)
        for lang in response1:
            assert isinstance(lang, str)
        response2 = self.lingo.get_languages(abbreviations=True)
        assert isinstance(response2, list)
        for lang in response2:
            assert isinstance(lang, str)
        assert len(response1) == len(response2)

    def test_get_friends(self):
        response = self.lingo.get_friends()
        assert isinstance(response, list)
        for friend in response:
            assert "username" in friend
            assert "points" in friend
            assert isinstance(friend['points'], int)
            assert "languages" in friend
            assert isinstance(friend['languages'], list)
            for lang in friend['languages']:
                assert isinstance(lang, str)

    def test_get_calendar(self):
        response1 = self.lingo.get_calendar()
        response2 = self.lingo.get_calendar(self.lang)
        for response in [response1, response2]:
            assert isinstance(response, list)
            for item in response:
                assert "skill_id" in item
                assert "improvement" in item
                assert "event_type" in item
                assert "datetime" in item
                assert isinstance(item['datetime'], int)

    def test_get_streak_info(self):
        response = self.lingo.get_streak_info()
        assert isinstance(response, dict)
        assert "site_streak" in response
        assert "daily_goal" in response
        assert "streak_extended_today" in response

    def test_get_leaderboard(self):
        response1 = self.lingo.get_leaderboard('week', datetime.now())
        response2 = self.lingo.get_leaderboard('month', datetime.now())
        for response in [response1, response2]:
            assert isinstance(response, list)
            for item in response:
                assert "points" in item
                assert "unit" in item
                assert "id" in item
                assert "username" in item

    def test_get_language_details(self):
        language = self.lingo.get_language_from_abbr(self.lang)
        response = self.lingo.get_language_details(language)
        assert isinstance(response, dict)
        assert "current_learning" in response
        assert "language" in response
        assert "language_string" in response
        assert "learning" in response
        assert "level" in response
        assert "points" in response
        assert "streak" in response

    def test_get_language_progress(self):
        response = self.lingo.get_language_progress(self.lang)
        assert isinstance(response, dict)
        assert "language" in response
        assert "language_string" in response
        assert "level_left" in response
        assert "level_percent" in response
        assert "level_points" in response
        assert "level_progress" in response
        assert "next_level" in response
        assert "num_skills_learned" in response
        assert "points" in response
        assert "points_rank" in response
        assert "streak" in response

    def test_get_known_topics(self):
        response = self.lingo.get_known_topics(self.lang)
        assert isinstance(response, list)
        for topic in response:
            assert isinstance(topic, str)

    def test_get_unknown_topics(self):
        response = self.lingo.get_unknown_topics(self.lang)
        assert isinstance(response, list)
        for topic in response:
            assert isinstance(topic, str)

    def test_get_golden_topics(self):
        response = self.lingo.get_golden_topics(self.lang)
        assert isinstance(response, list)
        for topic in response:
            assert isinstance(topic, str)

    def test_get_reviewable_topics(self):
        response = self.lingo.get_reviewable_topics(self.lang)
        assert isinstance(response, list)
        for topic in response:
            assert isinstance(topic, str)

    def test_get_known_words(self):
        response = self.lingo.get_known_words(self.lang)
        assert isinstance(response, list)
        for word in response:
            assert isinstance(word, str)

    def test_get_related_words(self):
        # Setup
        vocab = self.lingo.get_vocabulary()
        word = vocab['vocab_overview'][0]['normalized_string']
        # Get value
        response = self.lingo.get_related_words(word)
        # Check
        assert isinstance(response, list)

    def test_get_learned_skills(self):
        response = self.lingo.get_learned_skills(self.lang)
        assert isinstance(response, list)
        for skill in response:
            assert "language_string" in skill
            assert "id" in skill
            assert "title" in skill
            assert "explanation" in skill
            assert "progress_percent" in skill
            assert "words" in skill
            assert "name" in skill

    def test_get_language_from_abbr(self):
        response = self.lingo.get_language_from_abbr(self.lang)
        assert isinstance(response, str)

    def test_get_abbreviation_of(self):
        response = self.lingo.get_abbreviation_of('portuguese')
        assert isinstance(response, str)

    def test_get_translations(self):
        response1 = self.lingo.get_translations('e')
        response2 = self.lingo.get_translations('e', self.lang)
        response3 = self.lingo.get_translations('e', self.lang, 'fr')
        for response in [response1, response2, response3]:
            assert isinstance(response, dict)
            assert "e" in response
            assert isinstance(response['e'], list)
        response = self.lingo.get_translations(['e', 'a'])
        assert isinstance(response, dict)
        assert "e" in response
        assert isinstance(response['e'], list)
        assert "a" in response
        assert isinstance(response['a'], list)

    def test_get_vocabulary(self):
        response1 = self.lingo.get_vocabulary()
        response2 = self.lingo.get_vocabulary(self.lang)
        for response in [response1, response2]:
            assert isinstance(response, dict)
            assert response['language_string']
            assert "language_string" in response
            assert "learning_language" in response
            assert "from_language" in response
            assert "language_information" in response
            assert "vocab_overview" in response
            assert isinstance(response["vocab_overview"], list)

    def test_get_audio_url(self):
        # Setup
        vocab = self.lingo.get_vocabulary()
        word = vocab['vocab_overview'][0]['normalized_string']
        # Test
        response = self.lingo.get_audio_url(word)
        assert isinstance(response, str)
        response = self.lingo.get_audio_url(word, self.lang)
        assert isinstance(response, str)
        response = self.lingo.get_audio_url("zz")
        assert response is None


if __name__ == '__main__':
    unittest.main()
