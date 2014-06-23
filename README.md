# Duolingo


Unofficial Duolingo API Written in Python. This is mostly a collection of functions that give you common data
directly from the api resource dictionary. More methods to come.


#### TODO

- Integrate authenticated data
- Add user activity stream


## Installation

```sh
$ pip install duolingo-api
```


### Usage


```py
import duolingo

lingo  = duolingo.Duolingo('kartik')
```

### Methods


#### Summary

- lingo **.get_user_info()**
- lingo **.get_user_settings()**
- lingo **.get_languages()**
- lingo **.get_friends()**
- lingo **.get_language_details(language_name)**
- lingo **.get_language_progress(language_abbr)**
- lingo **.get_known_topics(language_abbr)**
- lingo **.get_known_words(language_abbr)**
- lingo **.get_learned_skills(lang)**


#### get_user_info()

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_user_info()
```

```
{'admin': False,
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
 'ui_language': u'en'}
```

#### get_user_settings()

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_user_settings()
```

```
{'deactivated': False,
 'is_follower_by': False,
 'is_following': False,
 'notify_comment': True}
```

#### get_languages()

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_languages()
```

```
[u'French', u'German', u'Spanish']
```

#### get_friends()

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_friends()
```

```
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

#### get_language_details(language_name)

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_language_details('French')
```

```
{u'current_learning': True,
 u'language': u'fr',
 u'language_string': u'French',
 u'learning': True,
 u'level': 6,
 u'points': 604,
 u'streak': 0}
```

#### get_language_progress(language_abbr)

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_language_progress()
```

```
{'language': u'fr',
 'language_string': u'French',
 'level_left': 146,
 'level_percent': 51,
 'level_points': 300,
 'level_progress': 154,
 'next_level': 7,
 'num_skills_learned': 15,
 'points': 604,
 'points_rank': 3,
 'streak': 0}
```

#### get_known_words(language_abbr)

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_known_words()
```

```
[u'absolument',
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
u'aimerais']
```

#### get_known_topics(language_abbr)

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_known_topics()
```

```
[u'Colors',
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
 u'Adjectives 1']
```

#### get_learned_skills(language_abbr)

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_learned_skills('fr')
```

```
[u'Basics',
 u'Basics 2',
 u'Colors',
 u'Animals',
 u'Possessives',
 u'Verbs: \xcatre / Avoir',
 u'Verbs: Present 1',
 u'Clothing',
 u'Food',
 u'Questions',
 u'Plurals',
 u'Common Phrases',
 u'Adjectives 1']
```
