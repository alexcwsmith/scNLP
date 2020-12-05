#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 01:49:15 2020

@author: smith
"""

from __future__ import unicode_literals, print_function
import pandas as pd
import os
from SpaCySettings import *


def info(title):
    print(title, "processID:", os.getpid())


def getArgs():
    from PubMedScraperSettings import cluster, comparison, clusterDirectory
    from SpaCySettings import modelName

    return (cluster, comparison, clusterDirectory, modelName)


def multiProcessTextMinimal(textFile):
    """Process a text file with ACWS spaCy model.

    Parameters
    ----------
    textFile : string
        Path to text file to process
    setName : string
        Name of data set for naming convention
    iteration : int, optional
        Iteration number for batch processing. The default is 0.
    start : int
        Character index to start processing, default 0.
    end : int
        Character index to end processing, default 10 million

    Returns
    -------
    None. Saves results .csv file and entity frequency .xlsx file.
    """
    info("Processing lit ")
    cluster, comparison, clusterDirectory, modelName = getArgs()
    setName = (
        cluster + "_" + comparison + "_" + modelName + "_" + textFile.split(sep="/")[-2]
    )
    model = modelDirectory
    iteration = 0
    start = 0
    end = None
    save = True
    import time

    def getCurrentTime():
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        return current_time

    t = str(getCurrentTime())
    print(setName + " Start Time: " + t)
    print("Saving results to " + clusterDirectory)
    t = str(getCurrentTime())
    nlp.max_length = 20000000
    with open(textFile, "r+") as f:
        testText = f.read()
        f.close()
    print(
        "Total text length: "
        + str(
            len(testText),
        )
        + " \n Processing chars "
        + str(start)
        + " through "
        + str(end)
    )
    text = testText[start:end]
    doc = nlp(text)
    t = str(getCurrentTime())
    print("NLP complete at " + t)

    setName = setName + "_Iteration" + str(iteration)
    entsList = list(doc.ents)
    sentList = []
    labList = []
    for ent in doc.ents:
        labList.append(ent.label_)
        sentList.append(str(ent.sent))

    sentDf = pd.DataFrame(sentList)
    sentDf.columns = ["Sentence"]
    sentDf = sentDf.drop_duplicates(subset="Sentence", keep="first")
    sentDf.to_excel(
        os.path.join(
            clusterDirectory,
            "Sentences_"
            + cluster
            + "/"
            + setName
            + "_NER_Results_Filtered_Sentences.xlsx",
        )
    )

    entCatDf = pd.DataFrame(data=[entsList, labList]).T
    entCatDf.columns = ["entity", "category"]
    entCatDf = entCatDf.drop_duplicates(subset="entity", keep="first")
    entCatDf.to_excel(
        os.path.join(
            clusterDirectory,
            "Categories_"
            + cluster
            + "/"
            + setName
            + "_NER_Results_Entities_Categories.xlsx",
        )
    )

    funcs = entCatDf.loc[entCatDf["category"] == "FUNCTION"]
    funcs = funcs.drop_duplicates(subset="entity", keep="first")
    regions = entCatDf.loc[entCatDf["category"] == "REGION"]
    regions = regions.drop_duplicates(subset="entity", keep="first")
    NTs = entCatDf.loc[entCatDf["category"] == "NEUROTRANSMITTER"]
    NTs = NTs.drop_duplicates(subset="entity", keep="first")
    phys = entCatDf.loc[entCatDf["category"] == "PHYSIO"]
    phys = phys.drop_duplicates(subset="entity", keep="first")
    CTs = entCatDf.loc[entCatDf["category"] == "CELLTYPE"]
    CTs = CTs.drop_duplicates(subset="entity", keep="first")
    if save == True:
        funcs.to_excel(
            os.path.join(
                clusterDirectory,
                "Functions_" + cluster + "/" + setName + "NER_Functions.xlsx",
            )
        )
        regions.to_excel(
            os.path.join(
                clusterDirectory,
                "Regions_" + cluster + "/" + setName + "NER_Regions.xlsx",
            )
        )
        NTs.to_excel(
            os.path.join(
                clusterDirectory,
                "NTs_" + cluster + "/" + setName + "NER_Neurotransmitters.xlsx",
            )
        )
        CTs.to_excel(
            os.path.join(
                clusterDirectory,
                "CellTypes_" + cluster + "/" + setName + "NER_CellTypes.xlsx",
            )
        )
        phys.to_excel(
            os.path.join(
                clusterDirectory,
                "Physio_" + cluster + "/" + setName + "NER_Physio.xlsx",
            )
        )
    t = str(getCurrentTime())
    print("Results file written at " + t)
    # return(funcs, regions, NTs, phys, CTs)
