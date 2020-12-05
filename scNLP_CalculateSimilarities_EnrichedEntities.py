#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:52:31 2020

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

logging.basicConfig(
    format="%(levelname)s - %(asctime)s: %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)

w2v_dir = "/home/smith/Smith_Scripts/NLP_GeneExpression/w2v_model/model072820/"
w2v_model = Word2Vec.load(
    os.path.join(
        w2v_dir, "w2v_model071820_MarkerGenes_UpOC_DownOC_CombinedSentences.model"
    )
)
modelName = "_w2v072820_"
resultDirectory = "/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/MarkerGenesV4_Results/"
clusters = ["Cluster" + str(x) for x in range(16)]

category = "CellTypes"
comparison = "MarkerGenesV4"
termIndex = pd.read_excel(
    os.path.join(
        resultDirectory,
        "Combined_Clusters_" + category + "_" + comparison + "_Frequency.xlsx",
    ),
    index_col=0,
)
termIndex = termIndex.sort_values(by="Combined Occurances", ascending=False)

enrichIndex = pd.read_excel(
    "/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/Combined_Clusters_Enriched_"
    + category
    + "_MarkerGenesV4_minCount300.xlsx",
    index_col=0,
)

enrIndex = enrichIndex.iloc[:, ::4]

clusters = ["Cluster" + str(x) for x in range(16)]
for cluster in clusters:
    tList = []
    for term in enrichIndex[cluster + " term"].tolist():
        if isinstance(term, str):
            term = term.replace(" ", "_")
            tList.append(term)
        else:
            tList.append("NaN")
    enrichIndex[cluster + " term"] = tList
enrichIndex.to_excel(
    resultDirectory + "MarkerGenesV4_Combined_Enriched_" + category + ".xlsx"
)

cluster = "Cluster0"
category = "Functions"


def calcEnrichedSimilarities(cluster, category, save=True):
    clusterDirectory = os.path.join(resultDirectory, cluster + "_MarkerGenes_Results/")
    clusterNum = cluster.replace("Cluster", "")
    genesDf = pd.read_excel(
        "/d1/studies/cellranger/ACWS_DP/scanpy_DiffExp_V4/DP_OCvsSaline_V4_t-test_pval_table_500genes_clusters.xlsx",
        index_col=0,
    )
    genesList = genesDf[str(clusterNum) + "_n"].tolist()
    genes = genesList
    genes = []
    for gene in genesList:
        genes.append(gene.lower())
    genes = genes[:75]
    words = pd.Series(enrIndex[cluster + " term"])
    words = words.dropna()
    wordsDf = pd.DataFrame(words)
    words = wordsDf[cluster + " term"].tolist()
    newWords = []
    for word in words:
        word = word.replace(" ", "_")
        newWords.append(word)

    cat = pd.DataFrame()
    for gene in genes:
        g = gene
        failedg = []
        failedw = []
        gs = []
        ws = []
        sims = []
        indList = []
        for word in newWords:
            try:
                ind = newWords.index(word)
                sim = w2v_model.wv.similarity(g, word)
                gs.append(g)
                ws.append(word)
                sims.append(sim)
                indList.append(ind)
            except KeyError:
                failedw.append(word)
                failedg.append(gene)
        lz = list(zip(gs, ws, sims, indList))
        df = pd.DataFrame(lz)
        cat = pd.concat([cat, df])
    cat.columns = ["gene", "term", "similarity", "index"]
    itemList = []
    aveList = []
    stdList = []
    weightList = []
    countList = []
    geneList = []
    aveIndList = []
    for item in cat["term"].unique().tolist():
        ave = np.mean(cat.loc[cat["term"] == item]["similarity"])
        aveIndex = np.mean(cat.loc[cat["term"] == item]["index"])
        std = np.std(cat.loc[cat["term"] == item]["similarity"])
        count = cat.loc[cat["term"] == item].shape[0]
        itemList.append(item)
        aveList.append(ave)
        aveIndList.append(aveIndex)
        stdList.append(std)
        countList.append(count)
    df2 = pd.DataFrame([itemList, aveList, stdList, countList, aveIndList]).T
    df2.columns = [
        cluster + " term",
        cluster + "_aveSim",
        cluster + "_std",
        cluster + "_N",
        cluster + "_aveIndex",
    ]
    df2 = df2.sort_values(by=cluster + "_aveSim", ascending=False)
    if save:
        df2.to_excel(
            os.path.join(
                resultDirectory,
                cluster
                + "_AverageSimilarities_Enriched_"
                + category
                + modelName
                + ".xlsx",
            )
        )
    return df2


catDf = pd.DataFrame()
for cluster in clusters:
    df = calcEnrichedSimilarities(cluster, category, save=True)
    df = df.sort_values(by=[cluster + "_aveSim"], ascending=False)
    df = df.reset_index(drop=True)
    catDf = pd.concat([catDf, df], axis=1)
catDf.to_excel(
    os.path.join(
        resultDirectory,
        "Combined_EnrichedSimilarities_" + category + "_w2vModel072820.xlsx",
    )
)

cat2 = pd.DataFrame()
for cluster in clusters:
    oddsList = []
    simDf = pd.read_excel(
        os.path.join(
            resultDirectory,
            cluster + "_AverageSimilarities_Enriched_" + category + "_w2v072820_.xlsx",
        ),
        index_col=0,
    )
    enrDf = pd.read_excel(
        "/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/MarkerGenesV4_Results/MarkerGenesV4_Combined_Enriched_"
        + category
        + ".xlsx",
        index_col=0,
    )
    terms = simDf[cluster + " term"].tolist()
    for term in terms:
        odds = enrDf.loc[enrDf[cluster + " term"] == term][
            cluster + "_oddsratio"
        ].values[0]
        oddsList.append(odds)
    simDf[cluster + "_oddsratio"] = oddsList
    simDf["OR_Sim_prod"] = simDf[cluster + "_oddsratio"] * simDf[cluster + "_aveSim"]
    simDf = simDf.sort_values(by="OR_Sim_prod", ascending=False)
    simDf = simDf.reset_index(drop=True)
    cat2 = pd.concat([cat2, simDf], axis=1)
cat2.to_excel(
    os.path.join(
        resultDirectory,
        "MarkerGenesV4_Similarities_OddsRatios_Combined_" + category + ".xlsx",
    )
)

X = w2v_model[w2v_model.wv.vocab]
dfX = pd.DataFrame(X)
dfX.shape
dfX.head()

X_corr = dfX.corr()
values, vectors = np.linalg.eig(X_corr)
args = (-values).argsort()
values = vectors[args]
vectors = vectors[:, args]
new_vectors = vectors[:, :2]
neww_X = np.dot(X, new_vectors)

import matplotlib.pyplot as plt

plt.figure(figsize=(13, 7))
plt.scatter(neww_X[:, 0], neww_X[:, 1], linewidths=10, color="blue")
plt.xlabel("PC1", size=15)
plt.ylabel("PC2", size=15)
plt.title("Word Embedding Space", size=20)
vocab = list(w2v_model.wv.vocab)
for i, word in enumerate(vocab):
    plt.annotate(word, xy=(neww_X[i, 0], neww_X[i, 1]))
plt.savefig(os.path.join(resultDirectory, "W2V_PCA.png"))
