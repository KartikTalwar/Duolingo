# Duolingo


Unofficial Duolingo API Written in Python. This is mostly a collection of functions that give you common data
directly from the api resource dictionary. More methods to come.


#### TODO

- Integrate authenticated data
- Add user activity stream


### Usage


```py
import duolingo

lingo  = duolingo.Duolingo('kartik')
```

### Methods

#### get_user_info()

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_user_info()
```

#### get_user_info()

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_user_info()
```

#### get_friends()

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_friends()
```

#### get_languages()

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_languages()
```

```json
```

#### get_language_details(language_name)

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_language_details()
```

```json
```

#### get_language_progress(language_abbr)

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_language_progress()
```

```json
```

#### get_known_words(language_abbr)

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_known_words()
```

```json
```

#### get_known_topics(language_abbr)

```py
lingo  = duolingo.Duolingo('kartik')
print lingo.get_known_topics()
```

```json
```
