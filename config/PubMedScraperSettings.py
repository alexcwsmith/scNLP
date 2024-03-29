#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:00:08 2020

@author: smith
"""
from Bio import Entrez
import pandas as pd
from bs4 import BeautifulSoup
from multiprocessing import Pool
import os
import glob
import nltk
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt
###You must generate an Entrez API key through myNCBI and enter here to use this package:
Entrez.email = 'smitaw@musc.edu'
Entrez.api_key = '8f015d17da5ac2df68b84d558b46e5150508'

searchTerms=['opioid', 'psychiatric', 'brain']

baseDirectory = os.getcwd()
dataDirectory = os.path.join(baseDirectory, 'Data/')
indexDirectory = os.path.join(baseDirectory, 'Indexes/')
geneDirectory = os.path.join(dataDirectory, 'GeneExpression/')
resultDirectory = os.path.join(baseDirectory, 'Results/')

if 'setName' not in globals():
    setName = input("Cluster & Condition to Analyze (e.g. Cluster4_MarkerGenes, or Cluster12_UpSaline): ")
    cluster = setName.split('_')[0]
    comparison = setName.split('_')[1]
elif setName in globals():
    cluster = setName.split('_')[0]
    comparison = setName.split('_')[1]

if 'scanpyDataQ' not in globals():
    scanpyDataQ = input("Use default scanpy expression data? (Y/N) : ")
if scanpyDataQ == 'Y' or 'y':
    scanpyData = '/home/smith/scNLP/config/DP_OCvsSaline_DiffExp_UpregulatedOC_t-test_leiden_3696genes.xlsx'
    print("Using scanpy data from: " + "\n" + scanpyData)
elif scanpyDataQ == 'N' or 'n':
    scanpyData = input("Enter path to gene expression .xlsx file: ")


if not os.path.exists(os.path.join(resultDirectory, setName + '_Results/')):
    print("Creating result directories...")
    os.mkdir(os.path.join(resultDirectory, setName + '_Results/'))
clusterDirectory = os.path.join(resultDirectory, setName + '_Results/')

if not os.path.exists(resultDirectory):
    os.mkdir(resultDirectory)
pubDirectory = resultDirectory
if not os.path.exists(os.path.join(pubDirectory, 'papers/' + setName + '_papers/')):
    if not os.path.exists(os.path.join(pubDirectory, 'papers/')):
        os.mkdir(os.path.join(pubDirectory, 'papers/'))
    os.mkdir(os.path.join(pubDirectory, 'papers/' + setName + '_papers/'))
paperDirectory = os.path.join(pubDirectory, 'papers/' + setName + '_papers/')
if not os.path.exists(os.path.join(paperDirectory, 'papers/')):
    os.mkdir(os.path.join(paperDirectory, 'papers/'))
if not os.path.exists(os.path.join(paperDirectory, 'titles/')):
    os.mkdir(os.path.join(paperDirectory, 'titles/'))
titleDirectory = os.path.join(paperDirectory, 'titles/')
if not os.path.exists(os.path.join(paperDirectory, 'abstracts/')):
    os.mkdir(os.path.join(paperDirectory, 'abstracts/'))
abstractDirectory = os.path.join(paperDirectory, 'abstracts/')

