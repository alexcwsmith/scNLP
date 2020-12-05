#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:04:45 2020

@author: smith
"""

from __future__ import unicode_literals, print_function
import os
import numpy as np
import pandas as pd
import time
import nltk
import gensim
import spacy
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
from gensim.models.phrases import Phrases, Phraser
import os
import multiprocessing
import csv
import re
import pandas as pd
from time import time
from datetime import datetime
from collections import defaultdict
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
import logging
import gensim
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

comparison = 'MarkerGenesV4'
resultDirectory = '/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/MarkerGenesV4_Results/'
w2v_dir = '/home/smith/Smith_Scripts/NLP_GeneExpression/w2v_model/model072820/'
nlp = spacy.load('en_core_sci_lg', disable=['ner', 'parser'])

df_clean = pd.read_csv('/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/Cleaned_Sentences_MarkerGenes_UpOC_DownOC.scv', index_col=0)

clusters = ['Cluster' + str(x) for x in range(16)]

def concatSentences(cluster):
    clusterDirectory = os.path.join(resultDirectory, cluster + '_' + comparison + '_Results/')
    sentDirectory = os.path.join(clusterDirectory, 'Sentences_' + cluster + '/')
    combinedDf = pd.DataFrame()
    dirs = os.listdir(sentDirectory)
    for item in dirs:
        fullpath = os.path.join(sentDirectory, item)
        df = pd.read_excel(fullpath, index_col=0)
        combinedDf = pd.concat([combinedDf, df], axis=0)
    combinedDf.to_excel(os.path.join(clusterDirectory, cluster + '_Sentences_Combined.xlsx'))
    return(combinedDf)


def concatClusters(clusters):
    bigDf = pd.DataFrame()
    for cluster in clusters:
        df = concatSentences(cluster)
        bigDf = pd.concat([bigDf, df], axis=0)
    bigDf = bigDf.drop_duplicates(subset=['Sentence'])
    bigDf.to_csv(os.path.join(w2v_dir, 'BigDf_Sentences_Combined.csv'))    
    return(bigDf)

concatClusters(clusters)

for cluster in clusters:
    concatSentences(cluster)

df = pd.read_csv('/home/smith/Smith_Scripts/NLP_GeneExpression/w2v_model/model072820/BigDf_Sentences_Combined.csv', index_col=0)
df = df.drop_duplicates()

###CLEANING REMOVING STOPWORDS:
def cleaning(doc):
    # Lemmatizes and removes stopwords
    # doc needs to be a spacy Doc object
    txt = [token.lemma_ for token in doc if not token.is_stop]
    # Word2Vec uses context words to learn the vector representation of a target word,
    # if a sentence is only one or two words long,
    # the benefit for the training is very small
    if len(txt) > 2:
        return(' '.join(txt))
    

###CLEANING WITH STOPWORDS:
def cleaning(doc):
    # Lemmatizes and removes stopwords
    # doc needs to be a spacy Doc object
    txt = [token.lemma_ for token in doc]
    # Word2Vec uses context words to learn the vector representation of a target word,
    # if a sentence is only one or two words long,
    # the benefit for the training is very small
    if len(txt) > 2:
        return(' '.join(txt))


###PREPARE INPUT SENTENCES FOR TRAINING
clusters = ['Cluster' + str(x) for x in range(20)]
df = concatClusters(clusters)

###PRE-PROCESS SENTENCES FOR TRAINING
brief_cleaning = (re.sub("[^A-Za-z0-9']['-']+", ' ', str(row)).lower() for row in df['Sentence'])
t = time()
txt = [cleaning(doc) for doc in nlp.pipe(brief_cleaning, batch_size=50000, n_threads=-1)]
print('Time to clean up everything: {} mins'.format(round((time() - t) / 60, 2)))  
df_clean = pd.DataFrame({'clean': txt})
df_clean = df_clean.dropna().drop_duplicates()
df_clean.shape
#df_clean.to_csv(os.path.join(w2v_dir, 'DownOC_df_cleaned.csv'))

sent = [row.split() for row in df_clean['clean']]
phrases = Phrases(sent, min_count=10, progress_per=20000)
bigram = Phraser(phrases)
sentences = bigram[sent]

###DESIGN MODEL
cores = 23
w2v_model = Word2Vec(min_count=7,
                     window=5,
                     size=300,
                     sample=1e-4, 
                     alpha=0.03, 
                     min_alpha=0.00007, 
                     negative=20,
                     workers=cores-1)

###TRAIN MODEL
t = time()
w2v_model.build_vocab(sentences, progress_per=50000)
print('Time to build vocab: {} mins'.format(round((time() - t) / 60, 2)))
t = time()
w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=25, report_delay=1)
print('Time to train the model: {} mins'.format(round((time() - t) / 60, 2)))


###RETRAIN / UPDATE MODEL WITH NEW SENTENCES
#Generate new vocabulary
sent = [row.split() for row in df_clean['clean']]
phrases = Phrases(sent, min_count=10, progress_per=10000)
bigram = Phraser(phrases)
sentences = bigram[sent]

t = time()
w2v_model.build_vocab(sentences, progress_per=50000)
print('Time to build vocab: {} mins'.format(round((time() - t) / 60, 2)))
#Train Model:
t = time()
w2v_model.train(sentences, total_examples=df_clean.shape[0], epochs=10, report_delay=1)
print('Time to train the model: {} mins'.format(round((time() - t) / 60, 2)))
  

###SAVE MODEL AFTER TRAINED:
output_dir = '/home/smith/Smith_Scripts/NLP_GeneExpression/w2v_model/model072820/'
w2v_model.save(os.path.join(output_dir, 'w2v_model072820_MarkerGenes_UpOC_DownOC_CombinedSentences.model'))








