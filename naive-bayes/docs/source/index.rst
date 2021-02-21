Naive-Bayes classifier implementation
=====================================

.. toctree::
   :maxdepth: 1

   ../_api/naive_bayes.rst


Installation 
------------

``$ python3 -m pip install . --upgrade``

Tests
-----

In order to perform tests, first install test dependencies, then run it with pytest as follows:
``$ python3 -m pip install .[tests] --upgrade``
``$ python3 -m pytest tests/test.py``


Usage
-----

.. code-block:: python3

    from naive_bayes import NaiveBayesClassifier
    
    model = NaiveBayesClassifier()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    model.accuracy(y_test, predictions)

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`