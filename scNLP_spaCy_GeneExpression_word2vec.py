#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:48:08 2020

@author: smith
"""
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

w2v_dir = '/home/smith/Smith_Scripts/NLP_GeneExpression/w2v_model/model071520/'
w2v_model = Word2Vec.load(os.path.join(w2v_dir, 'w2v_model071520_MarkerGenes_UpOC_DownOC_CombinedSentences.model'))
modelName = '_w2v071520_'

resultDirectory = '/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/'
clusters = ['Cluster' + str(x) for x in range(20)]


category = 'CellTypes'
comparison = 'MarkerGenes'
termIndex = pd.read_excel(os.path.join(resultDirectory, 'MarkerGenes_Results/Combined_Clusters_' + category + '_' + comparison + '_Frequency.xlsx'), index_col=0)
termIndex = termIndex.sort_values(by='Combined Occurances', ascending=False)

enrichIndex = pd.read_excel('/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/Combined_Clusters_Enriched_CellTypes_MarkerGenes.xlsx', index_col=0)
enrIndex = enrichIndex.iloc[:,::4]

def calcTopSimilarities(cluster, category, min_freq=5, topn=2000, save=False):
    resultDirectory = '/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/AllComparisons_Results/'
    clusterDirectory = os.path.join(resultDirectory, cluster + '_MarkerGenes_Results/')
    clusterNum=cluster.replace('Cluster', '')
    genesDf = pd.read_excel('/d1/studies/cellranger/ACWS_DP/scanpy_DiffExp_V2/results_maxGenes3000_maxMito.05_MinDisp0.2/DP_OC_Saline_Merged_t-test_pval_table_500genes_clusters.xlsx')
    genesList = genesDf[str(clusterNum) + '_n'].tolist()
    genes = genesList
    genes = []
    for gene in genesList:
        genes.append(gene.lower())
#    words = pd.read_excel(os.path.join(resultDirectory, str(cluster) + '_' + comparison + '_Results/' + category + '_' + cluster + '_Frequency.xlsx'), index_col=0)
#    words = pd.read_excel('/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/Cluster0_EnrichedFunctions_onlyTest.xlsx', index_col=0)
#    wordsRedacted = words.loc[words['Occurances'] > min_freq]['word'].tolist()
    words = enrIndex
    wordsRedacted = words[cluster + ' term'].tolist()[:-1]
    if category == 'CellTypes':
        wordsRedacted = termIndex['word'].tolist()[:150]
    newWords = []
    for item in wordsRedacted:
        try:
            item = item.replace(' ', '_')
            newWords.append(item)
        except AttributeError:
            pass
    cat = pd.DataFrame()
    catX = pd.DataFrame()
    for gene in genes:
        gene = gene.lower()
        try:
            df = pd.DataFrame(w2v_model.wv.most_similar(positive=[str(gene)], topn=topn), columns=['entity', 'similarity'])
            df['gene'] = gene
            df2 = df.loc[df['entity'].isin(newWords)]
            df2 = df2.reset_index(drop=True)
            dfX = pd.DataFrame(w2v_model.wv.most_similar(positive=[str(gene)], topn=topn), columns=['entity ' + gene, 'similarity ' + gene])
            dfX2 = dfX.loc[dfX['entity ' + gene].isin(newWords)]
            dfX2 = dfX2.reset_index(drop=True)
            cat = pd.concat([cat, df2], axis=0)
            cat = cat.reset_index(drop=True)
            catX = pd.concat([catX, dfX2], axis=1)
            catX = catX.reset_index(drop=True)
        except KeyError:
            pass
    if save:
 #       cat.to_excel(os.path.join(clusterDirectory, cluster + '_Similarities_Enriched_' + category + modelName + '.xlsx'))
 #       catX.to_excel(os.path.join(clusterDirectory, cluster + '_Similarities_Enriched_' + category + modelName + 'axis1.xlsx'))
        cat.to_excel(os.path.join(resultDirectory, cluster + '_Similarities_Enriched_' + category + modelName + '.xlsx'))
        catX.to_excel(os.path.join(resultDirectory, cluster + '_Similarities_Enriched_' + category + modelName + 'axis1.xlsx'))

    return(cat, catX)


def averageSimilarities(cluster, category):
    clusterDirectory = '/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/AllComparisons_Results/'
 #   clusterDirectory = os.path.join(resultDirectory, cluster + '_MarkerGenes_Results/')
    if not os.path.exists(os.path.join(clusterDirectory, cluster + '_Similarities_Enriched_' + category + modelName + '.xlsx')):
        raise FileNotFoundError("Similarities file doesn't exist at " + os.path.join(clusterDirectory, cluster + modelName + '_Similarities_Enriched_' + category + '.xlsx'))
    else:
        df = pd.read_excel(os.path.join(clusterDirectory, cluster + '_Similarities_Enriched_' + category + modelName + '.xlsx'))
    itemList = []
    aveList = []
    stdList = []
    weightList = []
    countList = []
    geneList = []
    for item in df['entity'].unique().tolist():
        ave = np.mean(df.loc[df['entity']==item]['similarity'])
        std = np.std(df.loc[df['entity']==item]['similarity'])
        gene = df.loc[df['entity']==item]['gene'].tolist()
        count = len(gene)
        weightedAve = df.loc[df['entity']==item].shape[0]*ave
        itemList.append(item)
        aveList.append(ave)
        stdList.append(std)
        weightList.append(weightedAve)
        countList.append(count)
        geneList.append(gene)
    df = pd.DataFrame(data=[itemList, aveList, stdList, weightList, countList, geneList]).T
    df.columns=['entity', 'ave_similarity', 'stdev', 'weighted_ave', 'count', 'similar_genes']
    df = df.sort_values(by='weighted_ave', ascending=False)
    df = df.drop_duplicates(subset='entity', keep='first')
    df.to_excel(os.path.join(clusterDirectory, cluster + '_averageSimilarities_Enriched' + category + modelName + '.xlsx'))
    return(df)

def combineAverageSims(clusters, category, save=True):
        clusterDirectory = '/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/AllComparisons_Results/'
        bigDf = pd.DataFrame()
        for cluster in clusters:
            df = pd.read_excel(os.path.join(clusterDirectory, cluster + '_averageSimilarities_Enriched' + category + modelName + '.xlsx'), index_col=0)
            df.columns=[cluster + '_entity', cluster + '_average_sim', cluster + '_stdev', cluster + '_weightedAve', cluster + '_count', cluster + '_similarGenes']
            bigDf = pd.concat([bigDf, df], axis=1)
        if save:
            bigDf.to_excel(os.path.join(clusterDirectory, 'Combined_AverageSimilarities' + modelName + category + '.xlsx'))
        return(bigDf)


cat, catX = calcTopSimilarities('Cluster0', 'Functions', save=True)

df = averageSimilarities('Cluster0', 'Functions')

for cluster in clusters:
    calcTopSimilarities(cluster, 'CellTypes', min_freq=5, topn=10000, save=True)

for cluster in clusters:
    averageSimilarities(cluster, 'CellTypes')

df = combineAverageSims(clusters, 'CellTypes', save=True)

df = averageSimilarities('Cluster5', 'Functions')

###FREQUENCY DISTRIBUTION:
cat = pd.read_excel('/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/Cluster3_Results/Functions_cat_model062920_Cluster3.xlsx')

    
def tsnescatterplot(model, setName, word, list_names,):
    """ Plot in seaborn the results from the t-SNE dimensionality reduction algorithm of the vectors of a query word,
    its list of most similar words, and a list of words.
    """
    arrays = np.empty((0, 300), dtype='f')
    word_labels = [word]
    color_list  = ['red']

    # adds the vector of the query word

    arrays = np.append(arrays, model.wv.__getitem__([word]), axis=0)
    
    # gets list of most similar words
    close_words = model.wv.most_similar([word])
    
    # adds the vector for each of the closest words to the array
    try:
        for wrd_score in close_words:
            wrd_vector = model.wv.__getitem__([wrd_score[0]])
            word_labels.append(wrd_score[0])
            color_list.append('blue')
            arrays = np.append(arrays, wrd_vector, axis=0)
        
        # adds the vector for each of the words from list_names to the array
        for wrd in list_names:
            wrd_vector = model.wv.__getitem__([wrd])
            word_labels.append(wrd)
            color_list.append('green')
            arrays = np.append(arrays, wrd_vector, axis=0)
    except KeyError:
        pass
    # Reduces the dimensionality from 300 to 50 dimensions with PCA
    reduc = PCA(n_components=42).fit_transform(arrays) ###### CHANGED FROM 50 DURING TUTORIAL
    
    # Finds t-SNE coordinates for 2 dimensions
    np.set_printoptions(suppress=True)
    
    Y = TSNE(n_components=2, random_state=0, perplexity=10).fit_transform(reduc)
    
    # Sets everything up to plot
    df = pd.DataFrame({'x': [x for x in Y[:, 0]],
                       'y': [y for y in Y[:, 1]],
                       'words': word_labels,
                       'color': color_list})
    
    fig, _ = plt.subplots()
    fig.set_size_inches(9, 9)
    
    # Basic plot
    p1 = sns.regplot(data=df,
                     x="x",
                     y="y",
                     fit_reg=False,
                     marker="o",
                     scatter_kws={'s': 40,
                                  'facecolors': df['color']
                                 }
                    )
    
    # Adds annotations one by one with a loop
    for line in range(0, df.shape[0]):
         p1.text(df["x"][line],
                 df['y'][line],
                 '  ' + df["words"][line].title(),
                 horizontalalignment='left',
                 verticalalignment='bottom', size='medium',
                 color=df['color'][line],
                 weight='normal'
                ).set_size(15)

    
    plt.xlim(Y[:, 0].min()-50, Y[:, 0].max()+50)
    plt.ylim(Y[:, 1].min()-50, Y[:, 1].max()+50)
            
    plt.title('t-SNE visualization for {}'.format(word.title()))
    plt.savefig(os.path.join(resultDirectory, setName + modelName + word + '_tSNE_42PCs.png'))

tsnescatterplot(w2v_model, setName, word, newWords)


w2v_model.wv.most_similar(positive=["drug_addiction"], topn=20)
w2v_model.wv.most_similar(positive=["nucleus_accumbens"], topn=20)
w2v_model.wv.most_similar(positive=["vta"], topn=20)
w2v_model.wv.most_similar(positive=["dbi"], topn=20)


w2v_model.wv.most_similar(positive=["enkephalin", "cacng4"], negative=["opioid"], topn=20)

w2v_model.wv.most_similar(positive=["slc17a7", "cacng4"], negative=["glutamatergic_neuron"], topn=20)



###RUN PCA:
# fit a 2d PCA model to the vectors
X = w2v_model[w2v_model.wv.vocab]
pca = PCA(n_components=50)
result = pca.fit_transform(X)
#Plot the result
fig, ax = plt.subplots()
ax.plot(result[:, 0], result[:, 1], 'o')
ax.set_title('Entities')
plt.show()

words = list(w2v_model.wv.vocab.keys())



