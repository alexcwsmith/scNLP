#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:14:57 2022

Script for converting SpaCy NER training data from format for spacy v2.2 --> 3.2.

@author: smith
"""

import os
os.chdir('/home/smith/scNLP/model')
from spaCy_ModelTrainingData_withCellTypes import *
import pandas as pd
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin
from random import shuffle

train_frac = 0.8
test_frac = 1-train_frac

train_size = int(len(TRAIN_DATA)*train_frac)

TRAIN_DATA = shuffle(TRAIN_DATA)

trainSet = TRAIN_DATA[:train_size]
valSet = TRAIN_DATA[train_size:]

#create training set
nlp = spacy.blank("en") # load a new spacy model
db = DocBin() # create a DocBin object
for text, annot in tqdm(trainSet): # data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)
db.to_disk("./train.spacy") # save the docbin object

#create validation set
nlp = spacy.blank("en") # load a new spacy model
db = DocBin() # create a DocBin object
for text, annot in tqdm(valSet): # data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)
db.to_disk("./validation.spacy") # save the docbin object

