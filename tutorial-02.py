# To run in an ipython notebook on the docker image

%%capture
%load_ext autoreload
%autoreload 2
%matplotlib inline
import sys
sys.path.append("..")
import statnlpbook.util as util
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['figure.figsize'] = (10.0, 6.0)


dictionary = {'i':'ich', 'ate':'aß', 'red':'rot', 'apple':'apfel', 'yesterday':'gestern','friend':'freund', 'with':'mit', 'an':'ein', 'a':'ein'}


import math
import numpy as np

x_space = ['I ate an apple', 
           'I ate a red apple', 
           'Yesterday I ate a red apple', 
           'Yesterday I ate a red apply with a friend']
y_space = ['Ich aß einen Apfel',
           'Ich aß einen roten Apfel',
           'Gestern aß ich einen roten Apfel',
           'Gestern aß ich einen roten Apfel mit einem Freund']
data = list(zip(x_space,y_space))
train = data[:2]
test = data[2:]

def f(x):
    input_ = x.split()
    fake_translation = []
    for word in input_:
        try:
            fake_translation.append(dictionary[word.lower()])
        except: pass
    return fake_translation

def similarity(x, y):
    fake_translation = f(x)
    real_translation = y.split()
    total = 0
    for fake_word in fake_translation:
        for real_word in real_translation:
            if fake_word in real_word.lower():
                total +=1
    lenx, leny = len(x.split()), len(y.split())
    
    measure = total / float(max(lenx, leny))
    if measure > 1.0:
        return 1.0
    else:
        return measure

def prediction(x, y_space):
    measure = 0
    for idx, sentence in enumerate(y_space):
        score = similarity(x, sentence)
        if score > measure:
            measure = score
            position = idx
    return y_space[position]

xpred = 'An apple fell off the tree yesterday'
prediction(xpred, y_space)

sample = x_space[3]
util.Table([(sample, y, similarity(sample, y)) for y in y_space for sample in x_space])