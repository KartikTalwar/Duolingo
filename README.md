# Duolingo API for Python

[![Build Status](https://travis-ci.org/KartikTalwar/Duolingo.svg?branch=master)](https://travis-ci.org/KartikTalwar/Duolingo)
[![Coverage Status](https://coveralls.io/repos/github/KartikTalwar/Duolingo/badge.svg?branch=master)](https://coveralls.io/github/KartikTalwar/Duolingo?branch=master)
[![PyPI version fury.io](https://badge.fury.io/py/duolingo-api.svg)](https://pypi.python.org/pypi/duolingo-api/)

Unofficial Duolingo API Written in Python. This is mostly a collection of functions that give you common data directly from the API resource dictionary. More methods to come.

##### TODO

- Integrate authenticated data

### Installation

```sh
$ pip install duolingo-api
```

### Usage

```py
import duolingo
lingo  = duolingo.Duolingo('kartik', 'my password')
```
Note: You are now required to provide a password to get any data from the Duolingo API

### Documentation
###### Account Information
- [Get User Information](#get-user-information)
- [Get Settings](#get-settings)
- [Get Languages](#get-languages)
- [Get Friends](#get-friends)
- [Get Calendar](#get-calendar)
- [Get Streak Information](#get-streak-information)
- [Get Leaderboard](#get-leaderboard)
- [Get daily XP progress](#get-daily-xp-progress)
- [Buy Item](#buy-item)
- [Buy Streak Freeze](#buy-streak-freeze)
###### Switch account being read
- [Set username](#set-username)
###### Language Information
- [Get Language Details](#get-language-details)
- [Get Language Progress](#get-language-progress)
- [Get Known Topics](#get-known-topics)
- [Get Unknown Topics](#get-unknown-topics)
- [Get Golden Topics](#get-golden-topics)
- [Get Reviewable Topics](#get-reviewable-topics)
- [Get Known Words](#get-known-words)
- [Get Related Words](#get-related-words)
- [Get Learned Skills](#get-learned-skills)
- [Get Language from Abbreviation](#get-language-from-abbreviation)
- [Get Abbreviation Of](#get-abbreviation-of)
- [Get Translations](#get-translations)
- [Get Vocabulary](#get-vocabulary)
- [Get Language Voices](#get-language-voices)
- [Get Audio URL](#get-audio-url)
#### Get User Information
`lingo.get_user_info()`

Returns a dictionary containing various information on the user, including their
avatar, user ID, location, current language, and more.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_user_info())

# Sample Response
{
    'admin': False,
    'avatar': 'https://s3.amazonaws.com/duolingo-images/avatars/22524/PALdVtqnHa',
    'bio': '',
    'cohort': 17,
    'contribution_points': 0,
    'created': '1 year ago',
    'fullname': 'Kartik',
    'gplus_id': None,
    'id': 22524,
    'invites_left': 3,
    'learning_language_string': 'French',
    'location': 'Toronto',
    'num_followers': 3,
    'num_following': 4,
    'twitter_id': None,
    'username': 'kartik',
    'ui_language': 'en'
}
```
#### Get Settings
`lingo.get_settings()`

Returns the user's settings.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_user_settings())

# Sample Response
{
    'deactivated': False,
    'is_follower_by': False,
    'is_following': False,
    'notify_comment': True
}
```
#### Get Languages
`lingo.get_languages(abbreviations)`

Returns a list of languages the user is learning.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_languages(abbreviations=True))
```
##### Parameters
`abbreviations` (boolean) *optional*  
--Returns the list of languages as abbreviations. Default=`False`.
```py
# Sample Response
['fr', 'de', 'es']
```
#### Get Friends
`lingo.get_friends()`

Returns a list of user's friends, their total points earned, and the languages
they are learning. The current user is included in this list.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_friends())

# Sample Response
[{'languages': ['French', 'Spanish', 'German', 'Italian'],
  'points': 4791,
  'username': 'apmechev'},
 {'languages': ['French', 'Spanish'],
  'points': 1810,
  'username': 'jlfwong'},
 {'languages': ['French', 'German', 'Spanish'],
  'points': 754,
  'username': 'kartik'},
 {'languages': ['Spanish', 'French'], 'points': 718, 'username': 'vhisko'},
 {'languages': ['French', 'German'],
  'points': 579,
  'username': 'warrench04'}]
```
#### Get Calendar
`lingo.get_calendar(language_abbr)`

Returns the user's last action.
##### Parameters
`language_abbr` (string) *optional*  
--Abbreviation of a given language. Default=`None`.
#### Get Streak Information
`lingo.get_streak_info()`

Returns the current site-wide streak, including daily goal information, and
whether the streak has been extended today.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_streak_info())

# Sample Response
{
    'site_streak': 141,
    'daily_goal': 30,
    'streak_extended_today': True
}
```
#### Get Leaderboard
`lingo.get_leaderboard(unit, before)`

Returns an ordered list containing the logged user leaderboard. You need to indicate unit as `week` or `month` to get the desired result. The `before` argument comes with the `time.time()` function, but if you need to know your leaderboard for a different date, you can pass the date in a epoch format.
```py
# Sample Request
lingo = duolingo.Duolingo('yurireis5', '...')
print(lingo.get_leaderboard('week'))
```
##### Parameters
`unit` (string) *optional*  
--Receive leaderboard data in specified units. The units `week` and `month` are recommended to receive desired results. Default=`None`.  
`before` (string) *optional*  
--Receive leaderboard data up to a specified date. Default=`time.time()`.
```py
# Sample Response
[
    {
        'unit': 'week',
        'id': 945238,
        'points': 280,
        'username': 'leticiabohrer'
    },
    {
        'unit': 'week',
        'id': 125621306,
        'points': 63,
        'username': 'Candice460698'
    },
    ...
]
```
#### Get Daily XP progress
`lingo.get_daily_xp_progress()`

Returns an ordered list containing the logged user leaderboard. You need to indicate unit as `week` or `month` to get the desired result. The `before` argument comes with the `time.time()` function, but if you need to know your leaderboard for a different date, you can pass the date in a epoch format.
Returns a dict with 3 keys: 'xp_goal', 'lessons_today', and 'xp_today'.
- xp_goal: Is your daily XP goal (int)
- lessons_today: A list of the lesson names which have been completed today
- xp_today: How much XP you have got today (int)

This method does not work if the username has been [set to something else](#set-username) after login.
```py
# Sample Request
lingo = duolingo.Duolingo('yurireis5', '...')
print(lingo.get_daily_xp_progress())

# Sample Response
{
    'xp_goal': 10, 
    'lessons_today': [], 
    'xp_today': 0
}
```
#### Buy Item
`lingo.buy_item(item_name, language_abbr)`

Buy a specific item in the shop. Returns the name of the item and the date and time of purchase.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.buy_item('streak_freeze', 'en'))
```
##### Parameters
`item_name` (string) **required**  
--The name of the item to buy.  
`language_abbr` (string) **required**  
--Abbreviation of a given language.
```py
# Sample Response
{
    'streak_freeze': '2017-01-10 02:39:59.594327'
}
```
Note: This will return [HTTP Status Code](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) 400 if the item can't be bought.

#### Buy Streak Freeze
`lingo.buy_streak_freeze()`

Buy a Streak on Ice extension, if the account has enough Lingots and is not yet equipped with the extension. Returns `True` if the extension was bought, `False` otherwise.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.buy_streak_freeze())

# Sample Response
True
```

#### Set username
`lingo.set_username(username)`

Sets the username, and reloads user data. This then allows you to read another user's information via the same API.
This will not work with the [get_daily_xp_progress()](#get-daily-xp-progress) method, and obviously will not allow you to buy items for other users.
```py
# Sample Request
lingo = Duolingo("kartik","...")
print(lingo.get_languages())
lingo.set_username("kartik2")
print(lingo.get_languages())

# Sample response
['French', 'German', 'Russian', 'Chinese', 'Portuguese', 'Spanish']
['French']
```

#### Get Language Details
`lingo.get_language_details(language_name)`

Returns the language details for a given language, including the current streak, the level, and total number of points.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_language_details('French'))
```
##### Parameters
`language_name` (string) **required**  
--The name of a given language.
```py
# Sample Response
{
    'current_learning': True,
    'language': 'fr',
    'language_string': 'French',
    'learning': True,
    'level': 6,
    'points': 604,
    'streak': 0
}
```
#### Get Language Progress
`lingo.get_language_progress(language_abbr)`

Returns the language progress for a given language.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_language_progress('fr'))
```
##### Parameters
`language_abbr` (string) **required**  
--Abbrieviation of a given language.
```py
# Sample Response
{
    'language': 'fr',
    'language_string': 'French',
    'level_left': 146,
    'level_percent': 51,
    'level_points': 300,
    'level_progress': 154,
    'next_level': 7,
    'num_skills_learned': 15,
    'points': 604,
    'points_rank': 3,
    'streak': 0
}
```
#### Get Known Topics
`lingo.get_known_topics(language_abbr)`

Returns a list containing the names of the known topics. See [`get_learned_skills`](#get-learned-skills) to return entire skill data.

Note: Order is not guaranteed.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_known_topics('fr'))
```
##### Parameters
`language_abbr` (string) **required**  
--Abbrieviation of a given language.
```py
# Sample Response
[
    'Colors',
    'Basics 2',
    'Animals',
    'Possessives',
    'Verbs: \xcatre / Avoir',
    'Clothing',
    'Food',
    'Questions',
    'Basics',
    'Verbs: Present 1',
    'Plurals',
    'Common Phrases',
    'Adjectives 1'
]
```
#### Get Unknown Topics
`lingo.get_unknown_topics(language_abbr)`

Returns a list containing the names of the unlearned topics.

Note: Order is not guaranteed.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_unknown_topics())
```
##### Parameters
`language_abbr` (string) **required**  
--Abbrieviation of a given language.
```py
# Sample Response
[
    'The',
    'Accusative Case',
    'Nature 1'
]
```
#### Get Golden Topics
`lingo.get_golden_topics(language_abbr)`

Returns a list containing the names of fully reviewed, or "golden", topics.

Note: Order is not guaranteed.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_golden_topics('fr'))
```
##### Parameters
`language_abbr` (string) **required**  
--Abbrieviation of a given language.
```py
# Sample Response
[
    'Colors',
    'Basics 2',
    'Animals',
    'Possessives',
    'Verbs: \xcatre / Avoir',
    'Clothing',
    'Verbs: Present 1',
    'Plurals',
    'Common Phrases',
    'Adjectives 1'
]
```
#### Get Reviewable Topics
`lingo.get_reviewable_topics(language_abbr)`

Returns a list containing the names of learned, but not fully "golden", topics.

Note: Order is not guaranteed.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_golden_topics('fr'))
```
##### Parameters
`language_abbr` (string) **required**  
--Abbrieviation of a given language.
```py
# Sample Response
[
    'Food',
    'Questions',
    'Basics'
]
```
#### Get Known Words
`lingo.get_known_words(language_abbr)`

Returns a set containing known words of a given language.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_known_words('fr'))
```
##### Parameters
`language_abbr` (string) **required**  
--Abbrieviation of a given language.
```py
# Sample Response
[
    'absolument',
    'accept\xe9',
    'acier',
    'actuellement',
    'adopt\xe9',
    'affirme',
    'agissant',
    'agit',
    'agr\xe9able',
    'ai',
    'aient',
    'ailes',
    'aime',
    'aimerais'
]
```
#### Get Related Words
`lingo.get_related_words(word, language_abbr)`

Returns a list of "related words" from the user's vocabulary list. For example, for the German verb "gehen", ```get_related_words``` will return a list of miscellaneous conjugations like "gehe" and "gingen".

Note: The dictionaries it returns are identical in format to those returned by [`get_vocabulary`](#get-vocabulary).

```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
 print(lingo.get_related_words('aller'))
 ```
 ##### Parameters
 `word` (string) **required**  
 --The word you want to retrieve related words for.  
 `language_abbr` (string) *optional*  
 --Abbreviation of a given language. Default=`None`.
 ```py
 # Sample Response
[
    {
        'last_practiced': '2015-05-27T06:01:18Z',
        'strength': 0.991741,
        'strength_bars': 4,
        'infinitive': 'aller',
        'lexeme_id': '51a2297870df84c13c7ce0b5f987ae70',
        'normalized_string': 'allait',
        'pos': 'Verb',
        'id': '51a2297870df84c13c7ce0b5f987ae70',
        'last_practiced_ms': 1432706478000.0,
        'gender': None,
        'skill': 'Verbs: Past Imperfect',
        'word_string': 'allait',
        'related_lexemes': [...],
        'skill_url_title': 'Verbs:-Past-Imperfect'
    },
    ...
]
```

#### Get Learned Skills
`lingo.get_learned_skills(language_abbr)`

Returns an ordered list containing the names of the known topics by date learned. Differs from [`get_known_topics`](#get-known-topics) in that it returns the entire skill data of each skill learned, rather than only the name.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_learned_skills('fr'))
```
##### Parameters
`language_abbr` (string) **required**  
--Abbrieviation of a given language.
```py
# Sample Response
[
    {
        'language_string': 'French',
        'dependency_order': 0,
        'dependencies_name': [],
        'practice_recommended': False,
        'learning_threshold': 0,
        'disabled': False,
        'more_lessons': 0,
        'test_count': 3,
        'missing_lessons': 0,
        'lesson': False,
        'progress_percent': 100.0,
        'id': 'aad5e3a9fc5bb6a9b55a4d20d40c3f27',
        'description': '',
        'category': '',
        'num_lessons': 4,
        'language': 'fr',
        'strength': 0.25,
        'beginner': True,
        'title': 'Basics 1',
        'coords_y': 1,
        'coords_x': 2,
        'url_title': 'Basics-1',
        'test': True,
        'lesson_number': 1,
        'learned': True,
        'num_translation_nodes': 0,
        'learning_threshold_percentage': 0,
        'icon_color': 'blue',
        'index': '0',
        'bonus': False,
        'explanation': (string containing HTML of explanation),
        'num_lexemes': 30,
        'num_missing': 0,
        'left_lessons': 0,
        'dependencies': [],
        'known_lexemes': [...],
        'words': [list of words contained in the lesson],
        'path': [],
        'achievements': [],
        'short': 'Basics 1',
        'locked': False,
        'name': 'BASICS',
        'comment_data': {},
        'new_index': 1,
        'changed': False,
        'has_explanation': True,
        'mastered': True
    },
    ...
]
```
#### Get Language from Abbreviation
`lingo.get_language_from_abbr(language_abbr)`

When the ```language_abbr``` of a language is known, but the full language name is not, you can use this method to return the language name. This only works for languages that the user is learning.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_language_from_abbr('fr'))
```
##### Parameters
`language_abbr` (string) **required**  
--Abbrieviation of a given language.
```py
# Sample Response
'French'
```
#### Get Abbreviation Of
`lingo.get_abbreviation_of(language_name)`

When the `language_name` of a language is known, but the language abbreviation is not, you can use this method to get the abbreviation. 

Note: This only works for languages that the user is learning.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_abbreviation_of('French'))
```
##### Parameters
`language_name` (string) **required**  
--The name of a given language.
```py
# Sample Response
'fr'
```
#### Get Translations
`lingo.get_translations(words)`

Returns the translations of a list of words passed to it. By default, the `source` is assumed to be the language of the user's Duolingo UI, and the `target` is assumed to be the user's current language, as of login time. The returned object is a dictionary containing a key for each item in the words list, with a list of translations as its value.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
lingo.get_translations(['de', 'du'], source='de', target='fr')
```
##### Parameters
`words` (list) **required**  
--The list of words you want to translate.  
`source` (string) *optional*  
--Specifies a source language to translate the words from. Default=`None`.  
`target` (string) *optional*  
--Specifies a target language to translate the words into. Default=`None`.
```py
# Sample Response
{
    'de': ['zu', 'von', 'des', 'an', 'auf', 'aus', 'mit', 'um',
            'vor', '\xfcber'],
    'du': ['der', 'nach', 'zur', '\u2205']
}
```
#### Get Vocabulary
`lingo.get_vocabulary()`

Gets the user's vocabulary for a given language. If `language_abbr` is none, the user's current language is used.
```py
#Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_vocabulary(language_abbr='de'))
```
##### Parameters
`language_abbr` (string) *optional*  
--Abbrieviation of a given language.
```py
# Sample Response
{
    language_string: "German",
    learning_language: "de",
    from_language: "en",
    language_information: {...},
    vocab_overview: [
    {
        strength_bars: 4,
        infinitive: null,
        normalized_string: "am",
        pos: "Preposition",
        last_practiced_ms: 1436422057000,
        skill: "Dative Case",
        related_lexemes: [
        "bb7397cbcb9f6665fcba49eced7b8619"
        ],
        last_practiced: "2015-07-09T06:07:37Z",
        strength: 0.999987,
        skill_url_title: "Dative-Case",
        gender: "Masculine",
        id: "2ffcc3aea9f3005d69b38083a6cac19d",
        lexeme_id: "2ffcc3aea9f3005d69b38083a6cac19d",
        word_string: "am"
        },
        ...
    ]
}
```
#### Get Language Voices
`lingo.get_language_voices(language_abbr)`

Returns a list of voices available in a given language. The list will always contain at least one voice, but that voice might not always be named 'default'. For instance, the only voice available for Turkish is named 'filiz'.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_language_voices('fr'))
```
##### Parameters
`language_abbr` (string) **required**  
--Abbrieviation of a given language.
```py
['default', 'mathieu']
```

#### Get Audio URL
`lingo.get_audio_url(word)`

Returns the path to an audio file containing the pronunciation of the word given. The language defaults to the user's current learning language. The voice used by default is randomly selected from Duolingo's available voices. To get a specific voice, pass the voice parameter with the name of the voice. To get the default voice (which is mostly an implementation detail), set random to False without passing a voice.
```py
# Sample Request
lingo  = duolingo.Duolingo('kartik', '...')
print(lingo.get_audio_url('bonjour'))
```
##### Parameters
`word` (string) **required**  
--The word you want an audio file for.  
`language_abbr` (string) *optional*  
--Abbrieviation of a given language. Default=`None`.  
`random` (boolean) *optional*  
--Whether to return a randomly selected language voice. Default=`True`.  
`voice` (string) *optional*  
--The name of a specific language voice. Default=`None`.
```py
# Sample Response
'https://d7mj4aqfscim2.cloudfront.net/tts/fr/token/bonjour'
```
