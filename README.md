# Duolingo


Unofficial Duolingo API Written in Python. This is mostly a collection of functions that give you common data
directly from the api resource dictionary. More methods to come.


#### TODO

- Integrate authenticated data
- Exception when user tries to get data that requires login


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
- lingo **.get_known_words(language_abbr)**
- lingo **.get_learned_skills(lang)**
- lingo **.get_language_from_abbr(language_abbr)**
- lingo **.get_abbreviation_of(language_name)**
- lingo **.get_activity_stream(before=None)**


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

#### get_abbreviation_of(language_abbr)

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
