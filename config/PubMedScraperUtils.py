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
import utils.scNLP_initNewProject as aux
from config.SpaCyConfig import *

if not cfg['entrez_API_key']:
    print("Warning: No Entrez email or API key found in config.yaml, query rate will be limited")
else:
    Entrez.email=cfg['entrezEmail']
    Entrez.api_key=cfg['entrez_API_key']
    
searchTerms=cfg['searchTerms']

if 'setName' not in globals():
    setName = input("Cluster & Condition to Analyze (e.g. Cluster4_MarkerGenes, or Cluster12_UpSaline): ")
cluster = setName.split('_')[0]
comparison = setName.split('_')[1]

if 'scanpyDataQ' not in globals():
    scanpyDataQ = input("Use default scanpy expression data? (Y/N) : ")
if scanpyDataQ.lower().startswith('y'):
    scanpyData = '/home/smith/scNLP/config/DP_OCvsSaline_DiffExp_UpregulatedOC_t-test_leiden_3696genes.xlsx'
    print("Using scanpy data from: " + "\n" + scanpyData)
elif scanpyDataQ.lower().startswith('n'):
    scanpyData = input("Enter path to gene expression .xlsx file: ")
    if scanpyData.startswith('~/'):
        scanpyData=os.path.expanduser(scanpyData)
    if not os.path.exists(scanpyData):
        raise FileNotFoundError("No file could be found at that path. Try again and enter the full path.")
else:
    raise ValueError("Must answer Y/N to previous question. Try again.")

if not os.path.exists(os.path.join(resultDirectory, setName + '_Results/')):
    print("Creating result directories...")
    os.mkdir(os.path.join(resultDirectory, setName + '_Results/'))
clusterDirectory = os.path.join(resultDirectory, setName + '_Results/')

if not os.path.exists(resultDirectory):
    os.mkdir(resultDirectory)
paperDirectory = os.path.join(resultDirectory, 'papers', setName + '_papers/')
titleDirectory = os.path.join(paperDirectory, 'titles/')
abstractDirectory = os.path.join(paperDirectory, 'abstracts/')

counter=0
for saveDir in [paperDirectory, titleDirectory, abstractDirectory, os.path.join(paperDirectory, 'papers/')]:
    if not os.path.exists(saveDir):
        if counter==0:
            print("Creating paper directories...")
            counter+=1
        os.mkdir(saveDir)
