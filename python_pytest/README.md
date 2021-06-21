# tddhome - python (pytest)

This folder contains bare-minimum python project with pytest. `foo` folder contains the project source code and `test` folder contains the tests.

## how to run tests

```
pipenv install
pipenv shell
pytest
```

## how to add a new test

In order for pytest to run the tests, test filenames should match the pattern `test_*.py` or `*_test.py` and test method names should start with `test`.