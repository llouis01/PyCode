# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:06:36 2021

@author: GrandLoup
"""

import tensorflow as ts
from tensorflow.keras.preprocessing.text import Tokenizer as TKZ
import pandas as pd
import os

# import data
data = pd.read_excel("C:\\Users\\Loube\\Documents\\GitHub\\Python_Codes\\NLP\\comments.xls")

sentences = ["I love my dog",
             "I love my cat",
             "You love hotdogs"]

# class object to limit words kept
tokenizer = TKZ(num_words=100)

tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)