# Group Name: Nott-Very-Smart
# Author: Looi Jie Ying, Liew Qian Hui
# Project Name: Food Ordering Chatbot
# Date: 10/11/2021

####################
# import libraries #
####################
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
nltk.download('punkt')
nltk.download('wordnet')

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random
import pickle

import json
with open('intents.json') as file:
    data = json.load(file)


