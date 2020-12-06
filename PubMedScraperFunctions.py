#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 03:06:01 2020

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
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt
from config.PubMedScraperSettings import *


def info(title):
    print(title, 'processID:', os.getpid())


def countPMCResults(term1):
    page = requests.get('https://www.ncbi.nlm.nih.gov/pmc/?term=' + term1)
    soup = BeautifulSoup(page.content, 'html.parser')
    res = soup.find(id='maincontent')
    res = soup.find(class_='result_count left').get_text()
    numRes = int(res.rsplit()[-1])
    return(numRes)


def findPMCIDs(searchTerm, term2=None, results=20, start=0, sort='relevance'):
    search = Entrez.esearch(db='pmc', retmax=results, term=searchTerm, retstart=start, sort=sort)
    record = Entrez.read(search)
    recDf = pd.DataFrame.from_dict(record, orient='index').T
    IDs = recDf.IdList.apply(pd.Series).T
    IDs.columns=['PMCID']
#    IDs.to_excel(os.path.join(paperDirectory, searchTerm + '_PMCIDS.xlsx'))
    IDlist= IDs['PMCID'].tolist()
    if len(IDlist) < 5:
        print("WARNING: Low number of results detected for " + str(searchTerm.split(' ')[0]))
    if term2 is not None:
        search = Entrez.esearch(db='pmc', retmax=results, term=term2, retstart=start, sort=sort)
        record = Entrez.read(search)
        recDf = pd.DataFrame.from_dict(record, orient='index').T
        IDs_term2 = recDf.IdList.apply(pd.Series).T
        IDs_term2.columns=['PMCID']
        IDlist2 = IDs_term2['PMCID'].tolist()
        IDlist.extend(IDlist2)
    return(IDlist)



def getFullText(PMCID):
    if not os.path.exists(paperDirectory):
        os.mkdir(paperDirectory)
        os.mkdir(os.path.join(paperDirectory, 'null/'))
    if not os.path.exists(abstractDirectory):
        os.mkdir(abstractDirectory)
    if not os.path.exists(titleDirectory):
        os.mkdir(titleDirectory)
    article = Entrez.efetch(db='pmc', id=PMCID, rettype='full', retmode='xml')
    art = article.read()  
    soup = BeautifulSoup(art, 'html.parser')
    title = soup.find('article-title').get_text()
    journal = soup.find('journal-title')
    if hasattr(journal, 'get_text'):
        journal = soup.find('journal-title').get_text()
    else:
        journal = None
    tables = soup.find_all('tr')
    tab = list(tables)
    for t in tab:
        try:
            t.decompose()
        except AttributeError: 
            pass
    try:
        doi = soup.find_all('article-id')[2].get_text()
    except IndexError:
        doi = 'No DOI available'
    info = 'TITLE: ' + str(title) + '\n' + 'JOURNAL: ' + str(journal) + '\n' + 'DOI: ' + str(doi)
    with open(os.path.join(titleDirectory, str(PMCID) + '_info.txt'), 'w+') as f:
        f.write(info)
        f.close()
    abstract = soup.find('abstract')
    if hasattr(abstract, 'get_text') == True:
        abstract_text = abstract.get_text()
        with open(os.path.join(abstractDirectory, str(PMCID) + '_abstract.txt'), 'w+') as fa:
            fa.write(abstract_text)
            fa.close()
    elif hasattr(abstract, 'get_text') == False:
        with open(os.path.join(abstractDirectory, str(PMCID) + '_abstract_null.txt'), 'w+') as fa:
            fa.write('No abstract available')
            fa.close()
    body = soup.find('body')
    if hasattr(body, 'get_text') == True:
        body_text = body.get_text()
        body_text = re.sub(r'[\ \n]{2,}', '', body_text)
        with open(os.path.join(paperDirectory, str(PMCID) + '_fulltext.txt'), 'w') as fb:
            fb.write(body_text)
            fb.close()
    elif hasattr(body, 'get_text') == False:
        with open(os.path.join(paperDirectory, 'null/' + str(PMCID) + '_fulltext_null.txt'), 'w+') as fb:
            fb.write('No full text available')
            fb.close()


def getFullTexts(IDs, results=50, start=0, end=None, sort='relevance'):          
    if not os.path.exists(paperDirectory):
        os.mkdir(paperDirectory)
        os.mkdir(os.path.join(paperDirectory, 'null/'))
    if not os.path.exists(abstractDirectory):
        os.mkdir(abstractDirectory)
    if not os.path.exists(titleDirectory):
        os.mkdir(titleDirectory)
    for ID in IDs[start:end]:
        dirs = os.listdir(paperDirectory)
        if len(dirs)-2 < results:
            getFullText(ID)
        else:
            pass
        
def getFullTextGene(PMCID, directory, gene=None):
    paperDirectory = os.path.join(directory, 'papers/' + str(gene) + '/')
    if not os.path.exists(paperDirectory):
        os.mkdir(paperDirectory)
        os.mkdir(os.path.join(paperDirectory, 'null/'))
    if not os.path.exists(abstractDirectory):
        os.mkdir(abstractDirectory)
        os.mkdir(abstractDirectory, 'null/')
    if not os.path.exists(titleDirectory):
        os.mkdir(titleDirectory)
    article = Entrez.efetch(db='pmc', id=PMCID, rettype='full', retmode='xml')
    art = article.read()  
    soup = BeautifulSoup(art, 'html.parser')
    if hasattr(soup.find('article-title'), 'get_text') ==True:
        title = soup.find('article-title').get_text()
    elif hasattr(soup.find('article-title'), 'get_text') == False:
        title = 'No title available'
    journal = soup.find('journal-title').get_text()
    tables = soup.find_all('tr')
    tab = list(tables)
    for t in tab:
        try:
            t.decompose()
        except AttributeError: 
            pass
    try:
        doi = soup.find_all('article-id')[2].get_text()
    except IndexError:
        doi = 'No DOI available'
    info = 'TITLE: ' + str(title) + '\n' + 'JOURNAL: ' + str(journal) + '\n' + 'DOI: ' + str(doi)
    with open(os.path.join(titleDirectory, str(PMCID) + '_info.txt'), 'w+') as f:
        f.write(info)
        f.close()
    abstract = soup.find('abstract')
    if hasattr(abstract, 'get_text') == True:
        abstract_text = abstract.get_text()
        with open(os.path.join(abstractDirectory, gene + '/' + str(PMCID) + '_abstract.txt'), 'w+') as fa:
            fa.write(abstract_text)
            fa.close()
    elif hasattr(abstract, 'get_text') == False:
        with open(os.path.join(abstractDirectory, gene + '/null/' + str(PMCID) + '_abstract_null.txt'), 'w+') as fa:
            fa.write('No abstract available')
            fa.close()
    body = soup.find('body')
    if hasattr(body, 'get_text') == True:
        body_text = body.get_text()
        body_text = re.sub(r'[\ \n]{2,}', '', body_text)
        with open(os.path.join(paperDirectory, str(PMCID) + '_fulltext.txt'), 'w') as fb:
            fb.write(body_text)
            fb.close()
    elif hasattr(body, 'get_text') == False:
        with open(os.path.join(paperDirectory, 'null/' + str(PMCID) + '_fulltext_null.txt'), 'w+') as fb:
            fb.write('No full text available')
            fb.close()

        
def getFullTextsGene(IDs, directory, gene=None, results=50, start=0, end=None, sort='relevance'):
    complete = False
    paperDirectory = os.path.join(directory, 'papers/', str(gene) + '/')
    if not os.path.exists(paperDirectory):
        os.mkdir(paperDirectory)
        os.mkdir(os.path.join(paperDirectory, 'null/'))
    if not os.path.exists(abstractDirectory):
        os.mkdir(abstractDirectory)
    if not os.path.exists(titleDirectory):
        os.mkdir(titleDirectory)
    for ID in IDs[start:end]:
        dirs = os.listdir(paperDirectory)
        if len(dirs)-2 < results:
            getFullTextGene(ID, directory=directory, gene=gene)
        elif len(dirs)-2 == results:
            pass
    dirs = os.listdir(paperDirectory)
    print("Retrieved " + str(len(dirs)-1) + " literature results for " + gene)
    if len(dirs)-1 == 0:
        print("WARNING: NO RESULTS RETRIEVED FOR " + gene)
        print("WARNING: NO RESULTS RETRIEVED FOR " + gene)
        
def getAbstracts(PMCID):
    if not os.path.exists(paperDirectory):
        os.mkdir(paperDirectory)
        os.mkdir(os.path.join(paperDirectory, 'null/'))
    if not os.path.exists(abstractDirectory):
        os.mkdir(abstractDirectory)
    if not os.path.exists(titleDirectory):
        os.mkdir(titleDirectory)
    article = Entrez.efetch(db='pmc', id=PMCID, rettype='abstract', retmode='xml')
    art = article.read()  
    soup = BeautifulSoup(art, 'html.parser')
    title = soup.find('article-title').get_text()
    journal = soup.find('journal-title')
    if hasattr(journal, 'get_text'):
        journal = soup.find('journal-title').get_text()
    else:
        journal = None
    tables = soup.find_all('tr')
    tab = list(tables)
    for t in tab:
        try:
            t.decompose()
        except AttributeError: pass
    try:
        doi = soup.find_all('article-id')[2].get_text()
    except IndexError:
        doi = 'No DOI available'
    info = 'TITLE: ' + str(title) + '\n' + 'JOURNAL: ' + str(journal) + '\n' + 'DOI: ' + str(doi)
    with open(os.path.join(titleDirectory, str(PMCID) + '_info.txt'), 'w+') as f:
        f.write(info)
        f.close()
    abstract = soup.find('abstract')
    if hasattr(abstract, 'get_text') == True:
        abstract_text = abstract.get_text()
        with open(os.path.join(abstractDirectory, str(PMCID) + '_abstract.txt'), 'w+') as fa:
            fa.write(abstract_text)
            fa.close()
    elif hasattr(abstract, 'get_text') == False:
        with open(os.path.join(abstractDirectory, str(PMCID) + '_abstract_null.txt'), 'w+') as fa:
            fa.write('No abstract available')
            fa.close()

def getAbstractGene(PMCID, directory, gene=None):
    paperDirectory = os.path.join(directory, 'papers/' + str(gene) + '/')
    if not os.path.exists(paperDirectory):
        os.mkdir(paperDirectory)
        os.mkdir(os.path.join(paperDirectory, 'null/'))
    if not os.path.exists(abstractDirectory):
        os.mkdir(abstractDirectory)
    if not os.path.exists(titleDirectory):
        os.mkdir(titleDirectory)
    article = Entrez.efetch(db='pmc', id=PMCID, rettype='abstract', retmode='xml')
    art = article.read()  
    soup = BeautifulSoup(art, 'html.parser')
    if hasattr(soup.find('article-title'), 'get_text') ==True:
        title = soup.find('article-title').get_text()
    elif hasattr(soup.find('article-title'), 'get_text') == False:
        title = 'No title available'
    journal = soup.find('journal-title').get_text()
    tables = soup.find_all('tr')
    tab = list(tables)
    for t in tab:
        try:
            t.decompose()
        except AttributeError: pass
    try:
        doi = soup.find_all('article-id')[2].get_text()
    except IndexError:
        doi = 'No DOI available'
    info = 'TITLE: ' + str(title) + '\n' + 'JOURNAL: ' + str(journal) + '\n' + 'DOI: ' + str(doi)
    with open(os.path.join(titleDirectory, str(PMCID) + '_info.txt'), 'w+') as f:
        f.write(info)
        f.close()
    abstract = soup.find('abstract')
    if hasattr(abstract, 'get_text') == True:
        abstract_text = abstract.get_text()
        with open(os.path.join(abstractDirectory, str(gene) + '/' + str(PMCID) + '_abstract.txt'), 'w+') as fa:
            fa.write(abstract_text)
            fa.close()
    elif hasattr(abstract, 'get_text') == False:
        with open(os.path.join(abstractDirectory, str(gene) + '/' + str(PMCID) + '_abstract_null.txt'), 'w+') as fa:
            fa.write('No abstract available')
            fa.close()

def getAbstractsGene(IDs, directory, gene=None, results=500, start=0, end=None, sort='relevance'):
    complete = False
    abstractDirectory = os.path.join(directory, 'abstracts/', str(gene) + '/')
    if not os.path.exists(paperDirectory):
        os.mkdir(paperDirectory)
        os.mkdir(os.path.join(paperDirectory, 'null/'))
    if not os.path.exists(abstractDirectory):
        os.mkdir(abstractDirectory)
    if not os.path.exists(titleDirectory):
        os.mkdir(titleDirectory)
    for ID in IDs[start:end]:
        dirs = os.listdir(abstractDirectory)
        if len(dirs) < results:
            getAbstractGene(ID, directory=directory, gene=gene)
        elif len(dirs) == results:
            pass
    dirs = os.listdir(abstractDirectory)
    print("Retrieved " + str(len(dirs)-1) + " literature results for " + gene)
    if len(dirs)-1 == 0:
        print("WARNING: NO RESULTS RETRIEVED FOR " + gene)
        print("WARNING: NO RESULTS RETRIEVED FOR " + gene)
        

def combineTextFiles(directory, rettype='full', sizeLimit=1e6):
    if rettype == 'full':
        read_files = glob.glob(os.path.join(directory, '*fulltext.txt'))
    elif rettype=='abstract':
        read_files = glob.glob(os.path.join(directory, '*abstract.txt'))
    skipList = []
    with open(os.path.join(directory, 'CombinedFullTexts.txt'), 'w+') as outfile:
        for file in read_files:
            if os.stat(file).st_size < sizeLimit:
                with open(file, 'r+') as infile:
                    outfile.write(infile.read())
            else:
                skipList.append(file)
    with open(os.path.join(directory, 'skippedFullTexts.txt'), 'w+') as f:
        f.write('\n'.join(skipList))
        f.close()
    with open(os.path.join(directory, 'CombinedFullTexts.txt'), 'r+') as r:
        text = r.read()
        r.close()
 #   return(text)
                    









