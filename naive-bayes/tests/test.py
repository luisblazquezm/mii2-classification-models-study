#!usr/bin/python3

# Copyright 2021 Luis Blazquez Miñambres (@luisblazquezm) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.
# Author: @luisblazquezm and @gandalfran

import pandas as pd
from naive_bayes import NaiveBayesClassifier

def test_naive_bayes():
	CSV_FILE = 'datasets/example.csv'
	df = pd.read_csv(CSV_FILE)
	classifier = NaiveBayesClassifier()

