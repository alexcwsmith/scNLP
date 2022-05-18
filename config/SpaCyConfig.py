#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 09:36:29 2020

@author: smith
"""
from __future__ import unicode_literals, print_function
import os
import shutil
import spacy
from gensim import models
from collections import Counter
from string import punctuation
import numpy as np
import pandas as pd
import codecs
import re
import random
from pathlib import Path
from spacy.util import minibatch, compounding
import nltk
import utils.scNLP_initNewProject as aux

new=False

if not new:
    configPath = '/home/smith/scNLP/spaCy_geneExpression-May12-2022/config.yaml'
    cfg=aux.read_config(configPath)
elif new:
    projectName='spaCy_geneExpression'
    projectPath=os.getcwd()
    cfg = aux.createProject(projectName, projectPath)
    pretrained = input("Do you want to copy a pretrained model? (y/[n]) ")
    if pretrained.lower().startswith('y'):
        pretrained = input("Enter path to model folder to copy: ")
        shutil.copytree(pretrained, cfg['modelDirectory'], dirs_exist_ok=True)
        
projectPath = cfg['projectPath']
modelName = cfg['projectName']
resultDirectory = cfg['resultDirectory']
modelDirectory = cfg['modelDirectory']
if os.path.exists(os.path.join(modelDirectory, 'meta.json')):
    print("Pretrained model found")
    print("Loading NLP model from " + modelDirectory + "\n")
    nlp = spacy.load(modelDirectory)
    nlp.max_length=cfg['max_length']
    nlp.add_pipe('sentencizer')

