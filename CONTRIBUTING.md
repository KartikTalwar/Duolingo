# Contributing

For installation instructions, please refer to the [Continuous Integration configuration file](./.travis.yml). Most specifically, the `install` section.

## Tests

Since the test suite contains integration tests, you must provide the credentials for a valid Duolingo account. Use the following snippet to export variables with your password and user information:

```sh
export DUOLINGO_PASSWORD="my_secret_password"
export DUOLINGO_USER="Luis"
```

Now, run the tests using pytest:

```sh
pytest tests.py
```
