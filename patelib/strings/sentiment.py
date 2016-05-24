import cgitb
import os


from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

def getScore(string):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(string)
    print(ss["compound"])   # just returning the overall score
