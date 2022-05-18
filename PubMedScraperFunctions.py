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
from config.PubMedScraperUtils import *

def info(title):
    print(title, 'processID:', os.getpid())

def getDir(directory, ext=None):
    if ext:
        return [os.path.join(directory, x) for x in os.listdir(directory) if x.endswith(ext)]
    elif not ext:
        return [os.path.join(directory, x) for x in os.listdir(directory)]

def makeDirs(dirs):
    for saveDir in dirs:
        if not os.path.exists(saveDir):
            os.mkdir(saveDir)

def countPMCResults(term1):
    """
    Query PubMedCentral and return the number of results
    
    Parameters
    ----------
    term1 : str
        Search term.
        
    Returns
    -------
    int : number of results
    """
    page = requests.get('https://www.ncbi.nlm.nih.gov/pmc/?term=' + term1)
    soup = BeautifulSoup(page.content, features='xml')
    res = soup.find(id='maincontent')
    res = soup.find(class_='result_count left').get_text()
    numRes = int(res.rsplit()[-1])
    return(numRes)


def findPMCIDs(searchTerm, term2=None, results=20, start=0, sort='relevance'):
    """
    Query PubMedCentral and return list of PMCIDs.

    Parameters
    ----------
    searchTerm : str
        Term to search for.
    term2 : str, optional
        Second term to append to searchTerm. The default is None.
    results : int, optional
        Number of results to query. The default is 20.
    start : int, optional
        Where to begin retrieving results. The default is 0, will start with first results.
    sort : str, optional
        How to sort results. The default is 'relevance'.

    Returns
    -------
    None.

    """
    if term2:
        searchTerm = ' '.join([searchTerm, term2])
    search = Entrez.esearch(db='pmc', retmax=results, term=searchTerm, retstart=start, sort=sort)
    record = Entrez.read(search)
    recDf = pd.DataFrame.from_dict(record, orient='index').T
    IDs = recDf.IdList.apply(pd.Series).T
    IDs.columns=['PMCID']
    IDlist= IDs['PMCID'].tolist()
    if len(IDlist) < 5:
        if not term2:
            print("WARNING: Low number of results detected for " + str(searchTerm.split(' ')[0]))
        elif term2:
            print("WARNING: Low number of results detected for '" + str(searchTerm)+"'")            
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
    """
    Retrieve full text for a single PMCID.

    Parameters
    ----------
    PMCID : int
        PMCID of manuscript to retrieve.

    Returns
    -------
    None.

    """
    makeDirs([paperDirectory, abstractDirectory, titleDirectory, os.path.join(paperDirectory, 'null/')])
    article = Entrez.efetch(db='pmc', id=PMCID, rettype='full', retmode='xml')
    art = article.read()  
    soup = BeautifulSoup(art, features='xml')
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
    """
    Query PMC and retrieve full texts for a list of PMCIDs.

    Parameters
    ----------
    IDs : list of ints
        List of PMCIDs to query
    results : int, optional
        Number of results to retrieve. The default is 50.
    start : int, optional
        Index to start retrieving results from. The default is 0 (starts with first result)
    end : int, optional
        Index to limit result retrieval to. The default is None.
    sort : str, optional
        How to sort results. The default is 'relevance'. See Entrez docs for more info.

    Returns
    -------
    None.

    """         
    makeDirs([paperDirectory, abstractDirectory, titleDirectory, os.path.join(paperDirectory, 'null/')])
    for ID in IDs[start:end]:
        dirs = getDir(paperDirectory, ext='fulltext.txt')
        if len(dirs) < results:
            getFullText(ID)
        else:
            pass
        
def getFullTextGene(PMCID, directory, gene=None):
    """
    Query PMC and retrieve full text of a single PMCID.

    Parameters
    ----------
    PMCID : int
        PMCID to query
    directory : str
        Parent directory of result folders. Should contain subfolders 'titles', 'abstracts', 'papers'
    gene : str, optional
        Name of gene being queried, for sorting of results.

    Returns
    -------
    None.
    """
    paperDirectory = os.path.join(directory, 'papers', str(gene))
    makeDirs([paperDirectory, abstractDirectory, titleDirectory, os.path.join(paperDirectory, 'null/')])
    article = Entrez.efetch(db='pmc', id=PMCID, rettype='full', retmode='xml')
    art = article.read()  
    soup = BeautifulSoup(art, features='xml')
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
        with open(os.path.join(abstractDirectory, gene, str(PMCID) + '_abstract.txt'), 'w+') as fa:
            fa.write(abstract_text)
            fa.close()
    elif hasattr(abstract, 'get_text') == False:
        with open(os.path.join(abstractDirectory, gene, 'null', str(PMCID) + '_abstract_null.txt'), 'w+') as fa:
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
        with open(os.path.join(paperDirectory, 'null', str(PMCID) + '_fulltext_null.txt'), 'w+') as fb:
            fb.write('No full text available')
            fb.close()

    
def getFullTextsGene(IDs, directory, gene=None, results=50, start=0, end=None, sort='relevance'):
    """
    Query PMC and retrieve full text of a list of PMCIDs.

    Parameters
    ----------
    IDs : list of ints
        List of PMCIDs to query
    directory : str
        Parent directory of result folders. Should contain subfolders 'titles', 'abstracts', 'papers'
    gene : str, optional
        Name of gene being queried, for sorting of results.
    results : int, optional
        Number of result papers to retrieve. Default is 50.
    start : int, optional
        Index to start retrieving from.
    end : int, optional
        Index to stop retrieving at. Default is None.
    sort : str, optional
        How to sort results. Default is 'relevance'.

    Returns
    -------
    None.
    """

    complete = False
    paperDirectory = os.path.join(directory, 'papers', str(gene))
    makeDirs([paperDirectory, abstractDirectory, titleDirectory, os.path.join(paperDirectory, 'null/')])
    for ID in IDs[start:end]:
        dirs = getDir(paperDirectory, ext='fulltext.txt')
        if len(dirs) < results:
            getFullTextGene(ID, directory=directory, gene=gene)
        elif len(dirs) == results:
            pass
    dirs = getDir(paperDirectory, ext='fulltext.txt')
    print("Retrieved " + str(len(dirs)) + " literature results for " + gene)
    if len(dirs) == 0:
        print("WARNING: NO RESULTS RETRIEVED FOR " + gene)
        print("WARNING: NO RESULTS RETRIEVED FOR " + gene)
        
def getAbstracts(PMCID):
    makeDirs([paperDirectory, abstractDirectory, titleDirectory, os.path.join(paperDirectory, 'null/')])
    article = Entrez.efetch(db='pmc', id=PMCID, rettype='abstract', retmode='xml')
    art = article.read()  
    soup = BeautifulSoup(art, features='xml')
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
    makeDirs([paperDirectory, abstractDirectory, titleDirectory, os.path.join(paperDirectory, 'null/')])
    article = Entrez.efetch(db='pmc', id=PMCID, rettype='abstract', retmode='xml')
    art = article.read()  
    soup = BeautifulSoup(art, features='xml')
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
    makeDirs([paperDirectory, abstractDirectory, titleDirectory, os.path.join(paperDirectory, 'null/')])
    for ID in IDs[start:end]:
        dirs = getDir(abstractDirectory, ext='abstract.txt')
        if len(dirs) < results:
            getAbstractGene(ID, directory=directory, gene=gene)
        elif len(dirs) == results:
            pass
    dirs = getDir(abstractDirectory, ext='abstract.txt')
    print("Retrieved " + str(len(dirs)-1) + " literature results for " + gene)
    if len(dirs) == 0:
        print("WARNING: NO RESULTS RETRIEVED FOR " + gene)
        print("WARNING: NO RESULTS RETRIEVED FOR " + gene)
        

def combineTextFiles(directory, rettype='full', sizeLimit=1e6):
    """
    Combine full texts into a single .txt corpus.
    
    Parameters
    ----------
    directory : str
        Path to folder containing individual .txt files
    rettype : str, optional
        'full' or 'abstracts', depending what kind of query was performed.
    sizeLimit : float
        Minimum size to be considered a valid full text (in bits).
    """
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
                    