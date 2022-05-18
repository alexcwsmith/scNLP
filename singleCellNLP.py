#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:51:26 2020

@author: smith
"""

from __future__ import unicode_literals, print_function
import numpy as np
import pandas as pd
import os
import glob
import time
import nltk
import gensim
import PubMedScraperFunctions as pm
from scNLP_NER import multiProcessTextMinimal
from pathos.pools import ProcessPool
import shutil
import scipy.stats as stats
import statsmodels.api as sm

from config.PubMedScraperUtils import resultDirectory, setName, clusterDirectory, paperDirectory, abstractDirectory, scanpyData
from utils.auxiliary import readConfig
from config.SpaCyConfig import projectPath
cfg = readConfig(os.path.join(projectPath, 'config.yaml'))
searchTerms=cfg['searchTerms']
cluster=setName.split('_')[0]
comparison=setName.split('_')[1]
modelName=cfg['projectName']
n_papers=cfg['n_papers']

def getDir(directory, ext=None):
    if ext:
        return [os.path.join(directory, x) for x in os.listdir(directory) if x.endswith(ext)]
    elif not ext:
        return [os.path.join(directory, x) for x in os.listdir(directory)]

def countLitResults(cluster, rettype="full"):
    """
    Counts literature results and creates manifest.

    Parameters:
    -----------
    cluster: string
    rettype (optional): string, 'full' or 'abstract'
    """
    IDlist = []
    geneList = []
    countList = []
    if rettype == 'full':
        path = os.path.join(resultDirectory, 'papers', cluster+'_'+comparison+'_papers', 'papers')
    elif rettype == 'abstract':
        path = os.path.join(resultDirectory, 'papers', cluster+'_'+comparison+'_papers', 'abstracts')
    dirs = os.listdir(path)
    for item in dirs:
        fullpath = os.path.join(path, item)
        if os.path.isdir(fullpath):
            files = getDir(fullpath, ext='fulltext.txt')
            count = len(files)
            geneList.append(item)
            countList.append(count)
            for file in files:
                f = os.path.basename(file)
                ID = f.split("_")[0]
                IDlist.append(ID)
    IDlist = list(set(IDlist))
    IDdf = pd.DataFrame(IDlist)
    IDdf.columns = ["PMCID"]
    IDdf["cluster"] = setName
    countDf = pd.DataFrame(data=[geneList, countList]).T
    countDf.columns = ["gene", "retrievedResults"]
    countDf["cluster"] = cluster
    countDf.to_excel(
        os.path.join(paperDirectory, setName + "_RetreivedLitResults_Manifest.xlsx")
    )
    IDdf.to_excel(os.path.join(paperDirectory, setName + "_RetreivedPMCIDs_Manifest.xlsx"))
    return (IDdf, countDf)


def updateManifest(newClusters, rettype="full", IDs=False):
    """
    Updates manifest file with newly retrieved literature.

    Parameters
    ----------
    newClusters: string
    rettype (optional): string, 'full' or 'abstract'
    IDs (optional): Boolean, whether to include individual PMCIDs in manifest.
    """
    maniDf = pd.DataFrame()
    for cluster in newClusters:
        cluResults = glob.glob(os.path.join(resultDirectory, cluster+'*'+'/'))
        if len(cluResults)==0:
            print("No results found for " + str(cluster) + ", skipping...")
            pass
        else:
            if rettype == "full":
                IDdf, countDf = countLitResults(cluster)
            elif rettype == "abstract":
                IDdf, countDf = countLitResults(cluster, rettype="abstract")
            if not IDs:
                maniDf = pd.concat([maniDf, countDf], axis=0)
                maniDf = maniDf.sort_values(by="cluster", ascending=True)
                maniDf = maniDf.drop_duplicates(keep="first")
                maniDf.to_excel(
                    os.path.join(
                        resultDirectory, "CombinedGeneManifest_" + comparison + ".xlsx"
                    )
                )
            elif IDs:
                maniDf = pd.concat([maniDf, IDdf], axis=0)
                maniDf = maniDf.sort_values(by="cluster", ascending=True)
                maniDf = maniDf.drop_duplicates(keep="first")
                maniDf.to_excel(
                    os.path.join(
                        resultDirectory, "CombinedPMCIDManifest_" + comparison + ".xlsx"
                    )
                )
    return maniDf


def copyLit(genes, rettype="full", copyData=False):
    """
    Examines manifest file for previously downloaded literature and copies CombinedFullText to new directory to avoid downloading again.

    Parameters
    ----------
    genes: list of genes
    rettype (optional): string, 'full' or 'abstract'
    copyData (optional): boolean, whether to copy the NLP result data in addition to literature results
    """
    if copyData == True:
        maniDf = pd.read_excel(
            os.path.join(
                resultDirectory, "CombinedGeneManifest_" + comparison + ".xlsx"
            ),
            index_col=0,
        )
    #   maniDf = pd.read_excel(os.path.join(resultDirectory, 'CombinedGeneManifest_MarkerGenes.xlsx'), index_col=0)
    if rettype == "full":
        targetDirectory = os.path.join(paperDirectory, "papers/")
    elif rettype == "abstract":
        targetDirectory = os.path.join(paperDirectory, "abstracts/")
    maniGenes = maniDf["gene"].unique().tolist()
    incGenes = []
    cGenes = []
    cluList = []
    for item in genes:
        if item in maniGenes:
            cGenes.append(item)
            clu = maniDf.loc[maniDf["gene"] == item]["cluster"]
            clu = clu.reset_index()
            clu = clu.loc[0]["cluster"]
            cluList.append(clu)
        else:
            incGenes.append(item)
    lz = list(zip(cGenes, cluList))
    for pair in lz:
        if rettype == 'full':
            tp = 'papers'
        elif rettype=='abstracts':
            tp = 'abstracts'
        src = os.path.join(
            resultDirectory,
            "papers",
            '_'.join([pair[1], comparison, tp]),
            'papers',
            pair[0],
            'CombinedFullTexts.txt',
        )
        targDir = os.path.join(targetDirectory, pair[0] + "/")
        targFile = os.path.join(targetDirectory, pair[0] + "/CombinedFullTexts.txt")
        if not os.path.exists(targDir):
            os.mkdir(targDir)
        else:
            print("Path already exists:", targDir)
        if not src==targFile:
            shutil.copyfile(src, targFile)
    if copyData:
        copiedGeneData = []
        cats = {"NTs":"Neurotransmitters", "Sentences":"Filtered_Sentences", "Regions":"Regions", "Physio":"Physio", "CellTypes":"CellTypes", "Functions":"Functions"} 
        for pair in lz:
            dataDirectory = os.path.join(
                resultDirectory, pair[1] + "_" + comparison + "_Results"
            )
            #        path = os.path.join(dataDirectory, pair[0])
            path = dataDirectory
            for cat in list(cats.keys()):
                dataPath = os.path.join(path, cat + "_" + pair[1])
                filePath = os.path.join(
                    dataPath,
                    '_'.join([pair[1], comparison, modelName, pair[0]])
                    + '_Iteration0_NER_'+cats[cat]+'.xlsx'
                )
                dataTargPath = os.path.join(
                    resultDirectory,
                    cluster + "_" + comparison + "_Results/" + cat + "_" + cluster,
                )
                if not os.path.exists(dataTargPath):
                    os.mkdir(dataTargPath)
                dataTarg = filePath.replace(pair[1], cluster)
                if not filePath==dataTarg:
                    try:
                        shutil.copyfile(filePath, dataTarg)
                    except FileNotFoundError:
                        print("File not found" + str(filePath))
                        pass
            copiedGeneData.append(pair[0])
        with open(
            os.path.join(targetDirectory, pair[0] + "_CopySummary.txt"), "w+"
        ) as f:
            if copyData:
                copyString = 'with data'
            elif not copyData:
                copyString = 'text only'
            f.write(
                pair[0]
                + " copied " + copyString + " from "
                + pair[1]
                + " at: "
                + "\n"
                + str(src)
            )
            f.close()
    return (incGenes, copiedGeneData)


def makeGeneDirs(genes):
    for gene in genes:
        targetDirectory = os.path.join(paperDirectory, "papers/")
        targDir = os.path.join(targetDirectory, gene + "/")
        if not os.path.exists(targDir):
            os.mkdir(targDir)
        if not os.path.exists(os.path.join(targDir, "null/")):
            os.mkdir(os.path.join(targDir, "null/"))
        absDirectory = os.path.join(paperDirectory, "abstracts/")
        absDir = os.path.join(absDirectory, gene + "/")
        if not os.path.exists(absDir):
            os.mkdir(absDir)
        if not os.path.exists(os.path.join(absDir, "null/")):
            os.mkdir(os.path.join(absDir, "null/"))


def getCurrentTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time


def retrieveAbstracts(genes, term2=searchTerms, n_papers=n_papers, directory=paperDirectory, cluster=cluster):
    """
    Retrieve abstracts from PubMedCentral

    parameters
    ----------
    genes: list of genes
    n_papers: int, number of abstracts to retrieve
    directory (optional): directory to save, default paperDirectory
    cluster (optional): cluster to search, default current working cluster
    """
    print("Using search terms " + str(term2))
    geneIDlist = []
    for gene in genes:
        for term in term2:
            IDs = pm.findPMCIDs(gene, term2=term, results=(n_papers * 2))
            if len(getDir(os.path.join(paperDirectory, "abstracts", gene), ext='fulltext.txt')) < n_papers:
                pm.getFullTextsGene(
                    IDs,
                    directory=directory,
                    gene=gene,
                    results=n_papers,
                    start=0,
                    end=None,
                )
                geneIDlist.extend(IDs)
    IDdf = pd.DataFrame(geneIDlist)
    IDdf.to_excel(os.path.join(directory, cluster + "_PMCIDlist.xlsx"))


def retrieveLiterature(genes, term2=searchTerms, n_papers=n_papers, directory=paperDirectory, cluster=cluster):
    """
    Retrieve full texts and abstracts from PubMedCentral

    parameters
    ----------
    genes: list of genes
    n_papers: int, number of abstracts to retrieve
    directory (optional): directory to save, default paperDirectory
    cluster (optional): cluster to search, default current working cluster
    """
    print("Using search terms " + str(term2))
    geneIDlist = []
    for gene in genes:
        for term in term2:
            IDs = pm.findPMCIDs(gene, term2=term, results=500)
            if len(getDir(os.path.join(paperDirectory, "papers", gene), ext='fulltext.txt')) < n_papers:
                pm.getFullTextsGene(
                    IDs,
                    directory=directory,
                    gene=gene,
                    results=n_papers,
                    start=0,
                    end=None,
                )
                geneIDlist.extend(IDs)
    IDdf = pd.DataFrame(geneIDlist)
    IDdf.to_excel(os.path.join(directory, cluster + "_PMCIDlist.xlsx"))


def _multiRetrieveLiterature(gene, terms=searchTerms):
   # info("Retrieving literature for " + str(gene))
    n_papers = 50
    directory = paperDirectory
    geneIDlist = []
    for term in terms:
        info("Retrieving literature for '" + str(gene) + " " + str(term)+"'")
        IDs = pm.findPMCIDs(gene, term2=term, results=500)
        if len(getDir(os.path.join(paperDirectory, "papers", gene), ext='fulltext.txt')) < n_papers:
            pm.getFullTextsGene(
                IDs,
                directory=directory,
                gene=gene,
                results=n_papers,
                start=0,
                end=None,
            )
    geneIDlist.extend(IDs)
    IDdf = pd.DataFrame(geneIDlist)
    IDdf["gene"] = gene
    IDdf["Cluster"] = cluster
    IDdf.to_excel(
        os.path.join(directory, cluster + "_" + str(gene) + "_PMCIDlist.xlsx")
    )


def multiRetrieveLiterature(genes, terms=searchTerms, processes=3):
    terms=[terms]*len(genes)
    pool = ProcessPool(nodes=processes)
    pool.map(_multiRetrieveLiterature, genes, terms)
    pool.close()
    pool.join()


def _multiRetrieveAbstracts(gene, terms=searchTerms):
    n_papers = 250
    directory = paperDirectory
    geneIDlist = []
    for term in terms:
        info("Retrieving literature for '" + str(gene) + " " + str(term)+"'")
        IDs = pm.findPMCIDs(gene, term2=term, results=2000)
        if len(getDir(os.path.join(paperDirectory, "abstracts", gene), ext='fulltext.txt')) < n_papers:
            pm.getAbstractsGene(
                IDs, directory=directory, gene=gene, results=n_papers, start=0, end=None
            )
        geneIDlist.extend(IDs)
    IDdf = pd.DataFrame(geneIDlist)
    IDdf["gene"] = gene
    IDdf["Cluster"] = cluster
    IDdf.to_excel(
        os.path.join(directory, cluster + "_" + str(gene) + "_PMCIDlist.xlsx")
    )


def multiRetrieveAbstracts(genes, terms=searchTerms, processes=3):
    terms=[terms]*len(genes)
    pool = ProcessPool(nodes=processes)
    pool.map(_multiRetrieveAbstracts, genes, terms)
    pool.close()
    pool.join()


def combineLiterature(paperDirectory, overwrite=False, minSize=1e4):
    """
    Combine all .txt files in paperDirectory into a single file.

    parameters
    ----------
    paperDirectory: string, path to directory
    overwrite (optional): boolean, whether to overwrite if CombinedFullTexts.txt already exists
    minsize (optional): minimum size of papers to include (default 1e4 i.e. 1kb)
    """
    dirs = os.listdir(os.path.join(paperDirectory, "papers/"))
    dirList = []
    nullGenes = []
    for item in dirs:
        fullpath = os.path.join(paperDirectory, "papers/" + item + "/")
        if os.path.isdir(fullpath):
            if not os.path.exists(fullpath + "CombinedFullTexts.txt"):
                dirList.append(item)
                pm.combineTextFiles(fullpath)
            elif (
                os.path.exists(fullpath + "CombinedFullTexts.txt") and overwrite == True
            ):
                pm.combineTextFiles(fullpath)
            if (
                os.stat(os.path.join(fullpath, "CombinedFullTexts.txt")).st_size
                < minSize
            ):
                nullGenes.append(item)
    with open(os.path.join(paperDirectory, "papers/nullGenes.txt"), "w+") as f:
        f.write(str(nullGenes))
        f.close()
    return nullGenes


def combineAbstracts(abstractDirectory, overwrite=False, minSize=1e2):
    """
    Combine all .txt files in a abstractDirectory into a single file.

    parameters
    ----------
    abstractDirectory: string, path to directory
    overwrite (optional): boolean, whether to overwrite if CombinedFullTexts.txt already exists
    minsize (optional): minimum size of papers to include (default 1e2)
    """
    dirs = os.listdir(abstractDirectory)
    dirList = []
    nullGenes = []
    for item in dirs:
        fullpath = os.path.join(abstractDirectory, item)
        if os.path.isdir(fullpath):
            if not os.path.exists(fullpath + "CombinedFullTexts.txt"):
                dirList.append(item)
                pm.combineTextFiles(fullpath, rettype="abstract")
            elif (
                os.path.exists(fullpath + "CombinedFullTexts.txt") and overwrite == True
            ):
                pm.combineTextFiles(fullpath, rettype="abstract")
            if (
                os.stat(os.path.join(fullpath, "CombinedFullTexts.txt")).st_size
                < minSize
            ):
                nullGenes.append(item)
    with open(os.path.join(abstractDirectory, "nullGenes.txt"), "w+") as f:
        f.write(str(nullGenes))
        f.close()
    return nullGenes


def info(title):
    print("processID:", os.getpid(), title)


def multiProcessLit(genes, directory, rettype="full", processes=13):
    """
    Runs NLP on literature with Pathos parallel processing pool.

    parameters
    ----------
    genes: list of genes
    directory: directory containing literature for NLP
    processes (optional): int, number of parallel processe (default 13)
    """
    resultDirs = [
        "Sentences",
        "Categories",
        "Functions",
        "Regions",
        "CellTypes",
        "NTs",
        "Physio",
    ]
    for item in resultDirs:
        if not os.path.exists(
            os.path.join(clusterDirectory, item + "_" + cluster + "/")
        ):
            os.mkdir(os.path.join(clusterDirectory, item + "_" + cluster + "/"))
    pathList = []
    for item in genes:
        if rettype == "full":
            fullpath = os.path.join(directory, "papers/" + item + "/")
        elif rettype == "abstract":
            fullpath = os.path.join(directory, "abstracts/" + item + "/")
        textFile = os.path.join(fullpath, "CombinedFullTexts.txt")
        pathList.append(textFile)
    pool = ProcessPool(nodes=processes)
    pool.map(multiProcessTextMinimal, pathList)
    pool.close()
    pool.join()


def calcEntityFrequency(directory, name, cluster):
    """
    Calculate frequency of named entities in a corpus of literature.

    parameters
    ----------
    directory: string, directory with NLP results
    name: string, name of category of NER ('Physio' 'CellType', 'NT', 'Citation' or 'Label')
    cluster: string, name of cluster
    """
    dirs = os.listdir(directory)
    df = pd.DataFrame()
    for file in dirs:
        d = pd.read_excel(os.path.join(directory, file))
        df = pd.concat([df, d], axis=0)
    df["entity"] = df["entity"].astype(str)
    df["entity"] = df["entity"].str.lower()
    entf = df["entity"].tolist()
    freq = nltk.FreqDist(entf)
    keyList = []
    valList = []
    for key, val in freq.items():
        keyList.append(str(key))
        valList.append(val)
    freqDf = pd.DataFrame(keyList)
    freqDf.columns = ["word"]
    freqDf["Occurances"] = valList
    freqDf = freqDf.sort_values(by="Occurances", ascending=False)
    freqDf = freqDf.loc[freqDf["word"] != "None"]
    freqDf = freqDf.dropna(how="any", axis=0)
    freqDf["Total Length"] = len(entf)
    freqDf["TF-IDF"] = freqDf["Occurances"] / len(entf)
    freqDf.to_excel(
        os.path.join(clusterDirectory, name + "_" + cluster + "_Frequency.xlsx")
    )


def reformatDf(df, name, cluster):
    series = pd.DataFrame(df["entity"].astype(str).drop_duplicates())
    category = df["category"].unique().tolist()[0]
    series["category"] = category
    series["entity"] = series.entity.astype(str).str.lower()
    series["entity"] = series.entity.apply(lambda x: x.split(" "))
    series["entity"] = series.entity.str.join("_")
    series.to_excel(
        os.path.join(resultDirectory, name + "_cat_model062920_" + cluster + ".xlsx")
    )
    return series


def runNLP(
    cluster,
    n_genes=25,
    searchTerms=searchTerms,
    rettype="full",
    update=False,
    copy=True,
    newClusters=None,
    dlProcesses=3,
    nlpProcesses=13,
    clear=False
):
    """
    Main NLP function. Performs named entity recognition on corpus of literature.

    parameters
    ----------
    cluster: string, name of cluster
    n_genes (optional, default 100): int, number of genes
    searchTerms : list of strings
        List of strings to append to search for each gene. For example ['opioid', 'psychatric', 'brain'] will search for each gene
        followed by each of those three words, in order, until it retrieves the number of results specified by n_papers in config file.
    rettype (optional, default 'full'): string, 'full' or 'abstract'
    update (optional, default False): boolean, whether to update manifest file before beginning
    copy (optional, default True): boolean, whether to copy literature using manifest
    newClusters (optional, default None): new clusters to update manifest with
    dlProcesses (optional, default 3): int, number of parallel processes for Entrez eFetch
    nlpProcesses (optional, default 13): int, number of parllel processes for NLP
    """
    clusterNum = cluster.replace("Cluster", "")
    genesDf = pd.read_excel(scanpyData)
    if comparison.startswith("Up"):
        genesList = genesDf["(2, " + str(clusterNum) + ")_n"].tolist()
        genes = genesList[:n_genes]
    elif comparison.startswith("MarkerGenes"):
        genesList = genesDf[str(clusterNum) + "_n"].tolist()
        genes = genesList[:n_genes]
    elif comparison.startswith("Down"):
        genesList = genesDf["(1, " + str(clusterNum) + ")_n"].tolist()
        genes = genesList[:n_genes]

    makeGeneDirs(genes)
    t = str(getCurrentTime())
    print("Pipeline started at " + t)
    if update:
        updateManifest(newClusters)
    if copy:
        if rettype == "full":
            incGenes, copiedGenes = copyLit(genes, rettype="full", copyData=True)
        elif rettype == "abstract":
            incGenes, copiedGenes = copyLit(genes, rettype="abstract", copyData=True)
    elif not copy:
        incGenes = genes
    print(str(len(incGenes)) + " genes to retrieve")
    t = str(getCurrentTime())
    print(
        "Start Retrieving Literature at: " + t + " with " + str(dlProcesses) + " nodes"
    )
    if rettype == "full":
        multiRetrieveLiterature(incGenes, terms=searchTerms, processes=dlProcesses)
        nullGenes = combineLiterature(paperDirectory)
    elif rettype == "abstract":
        multiRetrieveAbstracts(incGenes, terms=searchTerms, processes=dlProcesses)
        nullGenes = combineAbstracts(abstractDirectory)
    t = str(getCurrentTime())
    print(
        "Finished Retrieving Literature for "
        + str(len(incGenes))
        + " genes at: "
        + t
        + " with "
        + str(dlProcesses)
        + " nodes"
    )
    for n in nullGenes:
        genes.remove(n)
    if copy == True:
        genes = list(set(genes) - set(copiedGenes))
    else:
        genes = list(set(genes))
    print("Removed null genes: " + str(nullGenes))
    #  directory = paperDirectory
    t = str(getCurrentTime())
    print("Starting NLP with " + str(nlpProcesses) + " processes at " + t)
    if rettype == "full":
        multiProcessLit(genes, paperDirectory, processes=nlpProcesses)
    elif rettype == "abstract":
        multiProcessLit(
            genes, paperDirectory, rettype="abstract", processes=nlpProcesses
        )
    t = str(getCurrentTime())
    print("Finished NLP with " + str(nlpProcesses) + " processes at " + t)
    funcDir = os.path.join(clusterDirectory, "Functions_" + cluster + "/")
    regDir = os.path.join(clusterDirectory, "Regions_" + cluster + "/")
    NTDir = os.path.join(clusterDirectory, "NTs_" + cluster + "/")
    physDir = os.path.join(clusterDirectory, "Physio_" + cluster + "/")
    CTDir = os.path.join(clusterDirectory, "CellTypes_" + cluster + "/")
    calcEntityFrequency(funcDir, "Functions", cluster)
    calcEntityFrequency(regDir, "Regions", cluster)
    calcEntityFrequency(physDir, "Physio", cluster)
    calcEntityFrequency(NTDir, "Neurotransmitters", cluster)
    calcEntityFrequency(CTDir, "CellTypes", cluster)
    t = str(getCurrentTime())
    print("Pipeline finished at " + t)

def clearVariables():
    del globals()['setName']

def concatFrequencies(clusters, category="Functions", save=False):
    """
    Combine frequencies of NERs for clusters

    parameters
    ----------
    clusters: list, clusters to combine
    category (optional, default 'Functions'): string, NER category
    save (optional, default False): boolean, whether to save CSV result

    Returns:
    Concatenated DataFrame
    """
    #   resultDirectory = '/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/UpOC_Abstract_Results'
    cat = pd.DataFrame()
    for cluster in clusters:
        directory = os.path.join(
            resultDirectory, cluster + "_" + comparison + "_Results/"
        )
        df = pd.read_excel(
            os.path.join(directory, category + "_" + cluster + "_Frequency.xlsx"),
            index_col=0,
        )
        cat = pd.concat([cat, df])
    cat = cat.sort_values(by="Occurances", ascending=False)
    if save:
        cat.to_csv(
            os.path.join(resultDirectory, "Concat_" + category + "_unfiltered.csv")
        )
    return cat


def filterConcatFrequencies(df, category="Functions", min_count=50, save=True):
    """
    Filter NER frequency dataframe with minimum number of occurances.

    parameters
    ----------
    df: Pandas DataFrame to filter
    category (optional, default 'Functions'): string, NER category
    min_count (optional, default 50): int, minimum occurance count
    save (optional, default True)

    Returns:
    Filtered pandas DataFrame
    """
    #    resultDirectory = '/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/UpOC_Abstract_Results'
    catList = df.loc[df["Occurances"] > min_count]["word"].unique().tolist()
    sumList = []
    itemList = []
    print("Processing " + str(len(catList)) + " " + category)
    for item in catList:
        count = df.loc[df["word"] == item]
        s = sum(count["Occurances"])
        sumList.append(s)
    totDocLength = sum(df["Total Length"].unique().tolist())
    df = pd.DataFrame(catList)
    df.columns = ["word"]
    df["Combined Occurances"] = sumList
    df["Combined Doc Length"] = totDocLength
    df["TF-IDF"] = df["Combined Occurances"] / df["Combined Doc Length"]
    df = df.sort_values(by="Combined Occurances", ascending=False)
    df.to_excel(
        os.path.join(
            resultDirectory,
            "Combined_Clusters_" + category + "_" + comparison + "_Frequency.xlsx",
        )
    )
    return df


def findUpregulatedEntities(
    cluster, category="Functions", min_count=100, alpha=0.05, min_ratio=1.5
):
    """
    Use Fishers Exact Test to find significantly upregulated entities in corpus for a cluster compared to entire corpus.

    parameters
    ----------
    cluster: string, name of cluster
    category (optional, default 'Functions'): string, NER category
    min_count (optional, default 100): minimum frequency count
    alpha (optional, default .05): float, alpha value
    min_ratio (optional, default 1.5): float, minimum odds ratio to include
    """
    import scipy

   # resultDirectory = "/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/UpOC_Abstract_Results"
    clusterDirectory = os.path.join(
        resultDirectory, cluster + "_" + comparison + "_Results/"
    )
    tot = pd.read_excel(
        os.path.join(
            resultDirectory,
            "Combined_Clusters_" + category + "_" + comparison + "_Frequency.xlsx",
        ),
        index_col=0,
    )
    df = pd.read_excel(
        os.path.join(clusterDirectory, category + "_" + cluster + "_Frequency.xlsx"),
        index_col=0,
    )
    wordList = tot.loc[tot["Combined Occurances"] > min_count]["word"].tolist()
    upList = []
    ratioList = []
    unfoundList = []
    pvalList = []
    for word in wordList:
        try:
            #         ratio = float(df.loc[df['word']==word]['TF-IDF'])/float(tot.loc[tot['word']==word]['TF-IDF'])
            ratio = float(df.loc[df["word"] == word]["Occurances"]) / float(
                tot.loc[tot["word"] == word]["Combined Occurances"]
            )
            s1 = float(df.loc[df["word"] == word]["Occurances"])
            s2 = float(df.loc[df["word"] == word]["Total Length"])
            t1 = float(tot.loc[tot["word"] == word]["Combined Occurances"])
            t2 = float(tot.loc[tot["word"] == word]["Combined Doc Length"])
            arr = np.array([[s1, t1], [s2, t2]], np.float32)
            oddsratio, pvalue = scipy.stats.fisher_exact([[s1, s2], [t1, t2]])
        except TypeError:
            unfoundList.append(word)
            pass
        if pvalue < alpha:
            upList.append(word)
            ratioList.append(oddsratio)
            pvalList.append(pvalue)
            p_corr = sm.stats.multipletests(pvalList)
            p_corr = list(p_corr[1])
            l = list(zip(upList, pvalList, p_corr, ratioList))
            lz = sorted(l, key=lambda x: x[3])[::-1]
    return lz
