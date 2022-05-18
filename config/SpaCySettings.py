#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 09:36:29 2020

@author: smith
"""
from __future__ import unicode_literals, print_function
import spacy
#from scispacy.abbreviation import AbbreviationDetector
from gensim import models
from collections import Counter
from string import punctuation
import numpy as np
import pandas as pd
import os
import codecs
import re
import random
from pathlib import Path
from spacy.util import minibatch, compounding
import nltk

modelName = 'model051022'
resultDirectory = '/home/smith/scNLP/model/model051022/Results'
modelDirectory = '/home/smith/scNLP/model/model051022/output/model-best'
print("\n Loading NLP model from " + modelDirectory)
nlp = spacy.load(modelDirectory)
nlp.max_length=20000000

