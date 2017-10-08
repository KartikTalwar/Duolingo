# Duolingo

[![Build Status](https://travis-ci.org/KartikTalwar/Duolingo.svg?branch=master)](https://travis-ci.org/KartikTalwar/Duolingo)
[![Coverage Status](https://coveralls.io/repos/github/KartikTalwar/Duolingo/badge.svg?branch=master)](https://coveralls.io/github/KartikTalwar/Duolingo?branch=master)


Unofficial Duolingo API Written in Python. This is mostly a collection of functions that give you common data
directly from the api resource dictionary. More methods to come.


#### TODO

- Integrate authenticated data


## Installation

```sh
$ pip install duolingo-api
```


### Usage


```py
>>> import duolingo
>>> lingo  = duolingo.Duolingo('kartik')
# or
>>> lingo  = duolingo.Duolingo('kartik', password='my optional password')
```

- if you want to get information on your learning progress, then you must be logged in


### Methods


#### Summary

- lingo **.get_user_info()**
- lingo **.get_settings()**
- lingo **.get_languages(abbreviations=False)**
- lingo **.get_friends()**
- lingo **.get_calendar(language_abbr=None)**
- lingo **.get_streak_info()**
- lingo **.get_certificates()**
- lingo **.get_language_details(language_name)**
- lingo **.get_language_progress(language_abbr)**
- lingo **.get_known_topics(language_abbr)**
- lingo **.get_unknown_topics(language_abbr)**
- lingo **.get_golden_topics(language_abbr)**
- lingo **.get_reviewable_topics(language_abbr)**
- lingo **.get_known_words(language_abbr)**
- lingo **.get_learned_skills(lang)**
- lingo **.get_language_from_abbr(language_abbr)**
- lingo **.get_abbreviation_of(language_name)**
- lingo **.get_activity_stream(before=None)**
- lingo **.get_translations(words, source=None, target=None)**
- lingo **.get_vocabulary(language_abbr=None)**
- lingo **.get_language_voices(language_abbr)**
- lingo **.get_audio_url(word, language_abbr=None, random=True, voice=None)**
- lingo **.get_related_words(word, language_abbr=None)**
- lingo **.buy_item(item_name, language_abbr)**
- lingo **.buy_streak_freeze()**
- linko **.get_leaderboard(unit=None, before=time.time())**


#### get_user_info()

Returns a dictionary containing various information on the user, including their
avatar, their user id, their location, their current language, etc.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_user_info()
{
    'admin': False,
    'avatar': u'https://s3.amazonaws.com/duolingo-images/avatars/22524/PALdVtqnHa',
    'bio': u'',
    'cohort': 17,
    'contribution_points': 0,
    'created': u'1 year ago',
    'fullname': u'Kartik',
    'gplus_id': None,
    'id': 22524,
    'invites_left': 3,
    'learning_language_string': u'French',
    'location': u'Toronto',
    'num_followers': 3,
    'num_following': 4,
    'twitter_id': None,
    'username': u'kartik',
    'ui_language': u'en'
}
```

#### get_settings()

Returns the user's settings.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_user_settings()
{
    'deactivated': False,
    'is_follower_by': False,
    'is_following': False,
    'notify_comment': True
}
```

#### get_languages(abbreviations=False)

Returns a list of languages the user is learning. To get a list containing the
abbreviations, set the keyword argument "abbreviations" to true.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_languages()
[u'French', u'German', u'Spanish']

>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_languages(abbreviations=True)
[u'fr', u'de', u'es']
```

#### get_friends()

Returns a list of users' friends, their total points earned, and the languages
they are learning. The current user is included in this list.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_friends()
[{'languages': [u'French', u'Spanish', u'German', u'Italian'],
  'points': 4791,
  'username': u'apmechev'},
 {'languages': [u'French', u'Spanish'],
  'points': 1810,
  'username': u'jlfwong'},
 {'languages': [u'French', u'German', u'Spanish'],
  'points': 754,
  'username': u'kartik'},
 {'languages': [u'Spanish', u'French'], 'points': 718, 'username': u'vhisko'},
 {'languages': [u'French', u'German'],
  'points': 579,
  'username': u'warrench04'}]
```

#### get_streak_info()

Returns the current site-wide streak, including daily goal information, and
whether the streak has been extended today.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_streak_info()
{
    'site_streak': 141,
    'daily_goal': 30,
    'streak_extended_today': True
}
```

#### get_certificates()

Returns the list of certificates, including score, language, and a datetime
string.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_certificates()
[{
    u'language_string': u'German',
    u'score': 2.09,
    u'id': u'SgXFt9',
    u'language': u'de',
    u'datetime': u'1 month ago'
}]
```

#### get_language_details(language_name)

Returns the language details for a given language, including the current streak,
the level, and total number of points.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_language_details('French')
{
    u'current_learning': True,
    u'language': u'fr',
    u'language_string': u'French',
    u'learning': True,
    u'level': 6,
    u'points': 604,
    u'streak': 0
}
```

#### get_language_progress(language_abbr)

Returns the language progress for a given language.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_language_progress('fr')
{
    'language': u'fr',
    'language_string': u'French',
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

#### get_known_words(language_abbr)

Returns a set containing known words.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_known_words('fr')
[
    u'absolument',
    u'accept\xe9',
    u'acier',
    u'actuellement',
    u'adopt\xe9',
    u'affirme',
    u'agissant',
    u'agit',
    u'agr\xe9able',
    u'ai',
    u'aient',
    u'ailes',
    u'aime',
    u'aimerais'
]
```

#### get_known_topics(language_abbr)

Returns a list containing the names of the known topics. Differs from
```get_learned_skills``` in that it only returns names, instead of the entire
skill data.

Order is not guaranteed.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_known_topics()
[
    u'Colors',
    u'Basics 2',
    u'Animals',
    u'Possessives',
    u'Verbs: \xcatre / Avoir',
    u'Clothing',
    u'Food',
    u'Questions',
    u'Basics',
    u'Verbs: Present 1',
    u'Plurals',
    u'Common Phrases',
    u'Adjectives 1'
]
```

#### get_unknown_topics(language_abbr)

Returns a list containing the names of the unlearned topics.

Order is not guaranteed.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_unknown_topics()
[
    u'The',
    u'Accusative Case',
    u'Nature 1'
]
```

#### get_golden_topics(language_abbr)

Returns a list containing the names of fully reviewed or "golden" topics.

Order is not guaranteed.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_golden_topics()
[
    u'Colors',
    u'Basics 2',
    u'Animals',
    u'Possessives',
    u'Verbs: \xcatre / Avoir',
    u'Clothing',
    u'Verbs: Present 1',
    u'Plurals',
    u'Common Phrases',
    u'Adjectives 1'
]
```

#### get_reviewable_topics(language_abbr)

Returns a list containing the names of learned but not fully golden topics.

Order is not guaranteed.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_golden_topics()
[
    u'Food',
    u'Questions',
    u'Basics'
]
```

#### get_learned_skills(language_abbr)

Returns an ordered list containing the names of the known topics by date
learned. Differs from ```get_known_topics``` in that it returns the entire
skill data of each skill learned, rather than only the name.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_learned_skills('fr')
[
    {
        u'language_string': u'French',
        u'dependency_order': 0,
        u'dependencies_name': [],
        u'practice_recommended': False,
        u'learning_threshold': 0,
        u'disabled': False,
        u'more_lessons': 0,
        u'test_count': 3,
        u'missing_lessons': 0,
        u'lesson': False,
        u'progress_percent': 100.0,
        u'id': u'aad5e3a9fc5bb6a9b55a4d20d40c3f27',
        u'description': u'',
        u'category': u'',
        u'num_lessons': 4,
        u'language': u'fr',
        u'strength': 0.25,
        u'beginner': True,
        u'title': u'Basics 1',
        u'coords_y': 1,
        u'coords_x': 2,
        u'url_title': u'Basics-1',
        u'test': True,
        u'lesson_number': 1,
        u'learned': True,
        u'num_translation_nodes': 0,
        u'learning_threshold_percentage': 0,
        u'icon_color': u'blue',
        u'index': u'0',
        u'bonus': False,
        u'explanation': (string containing HTML of explanation),
        u'num_lexemes': 30,
        u'num_missing': 0,
        u'left_lessons': 0,
        u'dependencies': [],
        u'known_lexemes': [...],
        u'words': [list of words contained in the lesson],
        u'path': [],
        u'achievements': [],
        u'short': u'Basics 1',
        u'locked': False,
        u'name': u'BASICS',
        u'comment_data': {},
        u'new_index': 1,
        u'changed': False,
        u'has_explanation': True,
        u'mastered': True
    },
    ...
]
```

#### get_language_from_abbr(language_abbr)

When the ```language_abbr``` of a language is known, but the full language name
is not, Duolingo.get_language_from_abbr() can be used to get the
full name. This only works for languages that the user is learning.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_language_from_abbr('fr')
u'French'
```

#### get_abbreviation_of(language_name)

When the ```language_string``` of a language is known, but the language
abbreviation is not, Duolingo.get_abbreviation_of() can be used to get the
abbreviation. This only works for languages that the user is learning.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_abbreviation_of('French')
u'fr'
```

#### get_activity_stream(before=None)

The Duolingo API returns a "before" value with each request to the activity
stream. To get the previous set of data in the stream, feed it the 'before'
value from the current stream.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_activity_stream()
{
    u'more_events': True,
    u'events': [
        {
            u'type': 'practice',
            u'language_string': 'German',
            ...
        },
        ...
    ],
    u'js_version': u'//url_to_javascript',
    u'before': u'2015-07-06 05:42:24'
}

>>> print lingo.get_activity_stream(before='2015-07-06 05:42:24')
{
    u'more_events': True,
    u'events': [
        {
            u'type': "unlock",
            u'skills': [...],
            ...
        },
        ...
    ],
    u'js_version': u'js_version': u'//url_to_javascript',
    u'before': u'2015-07-05 07:44:56'
}
```

#### get_translations(words, source=None, target=None)

Returns the translations of a list of words passed to it. If source is none,
it is assumed to be whatever language the user's Duolingo UI is in. If the
target is none, it is assumed to be the language the user is currently using,
as determined at login time.

The returned object is a dictionary containing a key for each item in the words
list, with a list of translations as its value.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> lingo.get_translations(['de', 'du'])
{
    u'de': [u'of', u'in', u'from', u'by'],
    u'du': [u'of the', u'from the', u'about the', u"'s", u'about',
            u'by the', u'from', u'some']
}

>>> lingo.get_translations(['de', 'du'], target='de')
{
    u'von': [u'from', u'of', u'to', u'about', u'by', u'off', u'on', u'out of',
             u'von', u'with'],
    u'am': [u'the', u'on the', u'at the', u'a', u'about', u'around', u'at',
            u'by the', u'close to the', u'he', u'in', u'next to the', u'on',
            u'that', u'the one who', u'this', u'to', u'which', u'who']
}

>>> lingo.get_translations(['de', 'du'], source='de', target='fr')
{
    u'de': [u'zu', u'von', u'des', u'an', u'auf', u'aus', u'mit', u'um',
            u'vor', u'\xfcber'],
    u'du': [u'der', u'nach', u'zur', u'\u2205']
}
```

#### get_vocabulary(language_abbr=None)

Gets the user's vocabulary for a given language. If language_abbr is none, the
user's current language is used.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_vocabulary()
{
    language_string: "French",
    learning_language: "fr",
    from_language: "en",
    language_information: {...},
    vocab_overview: [
    {
        strength_bars: 4,
        infinitive: null,
        normalized_string: "beaucoup",
        pos: "Adverb",
        last_practiced_ms: 1436317448000,
        skill: "Adverbs 1",
        related_lexemes: [ ],
        last_practiced: "2015-07-08T01:04:08Z",
        strength: 0.961873,
        skill_url_title: "Adverbs-1",
        gender: null,
        id: "cb6d7331b5f41a3d3e3d85f678495259",
        lexeme_id: "cb6d7331b5f41a3d3e3d85f678495259",
        word_string: "beaucoup"
        },
        ...
    ]
}

>>> print lingo.get_vocabulary(language_abbr='de')
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

#### get_language_voices(language_abbr)

Returns a list of voices available in a given language.

The list will always contain at least one voice, but that voice might not always
be named 'default'. For instance, the only voice available for Turkish is named
'filiz'.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_language_voices('fr')
['default', u'mathieu']

>>> print lingo.get_language_voices('tr')
[u'filiz']

>>> print lingo.get_language_voices('de')
['default']
```

#### get_audio_url(word, language_abbr=None, random=True, voice=None)

Returns the path to an audio file containing the pronunciation of the word
given. The language defaults to the user's current learning language.

The voice used by default is randomly selected from Duolingo's available voices.
To get a specific voice, pass the voice parameter with the name of the voice.
To get the default voice (which is mostly an implementation detail), set random
to False without passing a voice.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_audio_url('bonjour')
'https://d7mj4aqfscim2.cloudfront.net/tts/fr/token/bonjour'

>>> print lingo.get_audio_url('hallo', language_abbr='de')
'https://d7mj4aqfscim2.cloudfront.net/tts/de/token/hallo'

>>> print lingo.get_audio_url('bonjour', voice='mathieu')
'https://d7mj4aqfscim2.cloudfront.net/tts/fr/mathieu/token/bonjour'
```

#### get_related_words(word, language_abbr=None)

Returns a list of "related words" from the user's vocabulary list. For instance,
for the German verb "gehen", ```get_related_words``` will return a list of
miscellaneous conjugations like "gehe" and "gingen".

The dictionaries it returns are identical in format to those returned by
get_vocabulary.

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.get_related_words('aller')
[
    {
        u'last_practiced': u'2015-05-27T06:01:18Z',
        u'strength': 0.991741,
        u'strength_bars': 4,
        u'infinitive': u'aller',
        u'lexeme_id': u'51a2297870df84c13c7ce0b5f987ae70',
        u'normalized_string': u'allait',
        u'pos': u'Verb',
        u'id': u'51a2297870df84c13c7ce0b5f987ae70',
        u'last_practiced_ms': 1432706478000.0,
        u'gender': None,
        u'skill': u'Verbs: Past Imperfect',
        u'word_string': u'allait',
        u'related_lexemes': [...],
        u'skill_url_title': u'Verbs:-Past-Imperfect'
    },
    ...
]

>>> print lingo.get_audio_url('hallo', language_abbr='de')
[
    {
        u'last_practiced': u'2015-07-09T06:07:37Z',
        u'strength': 0.999987,
        u'strength_bars': 4,
        u'infinitive': u'gehen',
        u'lexeme_id': u'e29e6fb5291a3c4167f67d9d31dc86aa',
        u'normalized_string': u'ging',
        u'pos': u'Verb',
        u'id': u'e29e6fb5291a3c4167f67d9d31dc86aa',
        u'last_practiced_ms': 1436422057000.0,
        u'gender': None,
        u'skill': u'Verbs: Preterite',
        u'word_string': u'ging',
        u'related_lexemes': [...],
        u'skill_url_title': u'Verbs:-Preterite'
    },
    ...
]
```

#### get_leaderboard(unit=None, before=time.time())

Returns an ordered list containing logged user leaderboard.
You need to bring week or month as a unit to get the desired result.
The before argument come with time.time() function, but if you need to know what's
your leaderboard in another date, you can pass the date in a epoch format

```py
>>> lingo = duolingo.Duolingo('yurireis5')
>>> print lingo.get_leaderboard('week')
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

>>> print lingo.get_leaderboard('month')
[
    {
        'unit': 'month',
        'id': 945238,
        'points': 2290,
        'username': 'leticiabohrer'
    },
    {
        'unit': 'month',
        'id': 125621306,
        'points': 162,
        'username': 'Candice460698'
    },
    ...
]
```

#### buy_item(item_name, language_abbr)

Buy a specific item in the shop

```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.buy_item('streak_freeze', 'en')
{
    'streak_freeze': '2017-01-10 02:39:59.594327'
}
```

This will return a [HTTP Status Code](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) = 400
if the item can't be bought.

#### buy_streak_freeze()

Buy a Streak on Ice extension, if the account has enough Lingots and is not yet equipped with the extension.

Returns 'True' if the extension was bought, 'False' otherwise.


```py
>>> lingo  = duolingo.Duolingo('kartik')
>>> print lingo.buy_streak_freeze()
True
