# Naive-Bayes classifier

Small description

## Instalation, documentation and tests

- **install**: `python3 -m pip install . --upgrade`
- **run tests**: install test dependencies with `python3 -m pip install .[tests]`, then go to the tests foleder and run `pytest test.py`
- **generate doc**: install documentation dependencies with `python3 -m pip install .[docs]`, then go to the docs folder and run `make html`


## Usage

```python3
    from naive_bayes import NaiveBayesClassifier

    model = NaiveBayesClassifier()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    model.accuracy(y_test, predictions)
```
