import re
import argparse
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

class Lang_Classifier(object):

    def __init__(self, model, text_to_predict):
        self.model = model
        self.text_to_predict = text_to_predict

    def classify(self):
        with open(self.model, 'rb') as f:
            model = pickle.load(f)
        predicted = model.predict(self.text_to_predict)
        return predicted
