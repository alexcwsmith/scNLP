#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:08:37 2020

@author: smith
"""

import os
os.chdir('/home/smith/Smith_Scripts/scNLP/')
from config.PubMedScraperSettings import *
import singleCellNLP as scn
from scipy import stats
import statsmodels.api as sm

#If you want to update the manifest file first:
clusters = ['Cluster' + str(x) for x in range(3)]
maniDf = scn.updateManifest(clusters, rettype='full')

#Run NLP on current cluster:
scn.runNLP(cluster, rettype='full', n_genes=25, copy=False, dlProcesses=3)

df = pd.DataFrame()

#Downstream analysis:
category='Physio' #NER recognized categories: Physio, Label (region), NT, CellType
types = scn.concatFrequencies(clusters, category=category, save=True)
catTypes = scn.filterConcatFrequencies(types, clusters, category=category, min_count=50, save=True)

cat = pd.DataFrame()
for cluster in clusters:
    min_count=300
    lz = ga.findUpregulatedEntities(cluster, category=category, min_count=min_count)
    resDf = pd.DataFrame(lz)
    resDf.columns=[cluster + ' term', cluster + '_pvalue', cluster + '_corrected_p', cluster + '_oddsratio']
    resDf = resDf.loc[resDf[cluster + '_oddsratio'] > 1.0]
    resDf = resDf.sort_values(by=cluster + '_corrected_p', ascending=True)
    cat = pd.concat([cat, resDf], axis=1)
cat.to_excel(os.path.join(resultDirectory, 'Combined_Clusters_Enriched_' + category + '_' + comparison + '_minCount' + str(min_count) + '.xlsx'))








