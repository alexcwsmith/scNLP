#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:14:07 2020

@author: smith
"""

from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
from spacy.tokens import Span
from spacy.language import Language
from spacy.vocab import Vocab
import pandas as pd
import os
from time import time
from datetime import datetime
import nltk
from nltk import sent_tokenize
import numpy as np

# new entity label
LABEL = "REGION"
CIT = "CITATION"
NT = "NEUROTRANSMITTER"
PHYS = "PHYSIO"
FUNC = "FUNCTION"
CELL = "CELLTYPE"


resultDirectory = '/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062520/Results/'
output_dir = '/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062520/'
nlp = spacy.load(output_dir)

nlp = spacy.load("en_core_sci_sm")
nlp = spacy.load("en_core_sci_lg")
#don't run again:
#nlp.add_pipe(nlp.create_pipe('sentencizer'))
#nlp.disable_pipes('sentencizer')
#nlp.add_pipe(nlp.create_pipe('parser'))

# training data
# Note: If you're using an existing model, make sure to mix in examples of
# other entity types that spaCy correctly recognized before. Otherwise, your
# model might learn the new type, but "forget" what it previously knew.
# https://explosion.ai/blog/pseudo-rehearsal-catastrophic-forgetting



###ADD VECTORS TO MODEL:
w2v_dir = '/home/smith/Smith_Scripts/AllenSDK/CircuitFinder/Data/PubMedScraper/spaCy/spaCy_models/sciSpaCy/W2V_Models/'
w2v_path = os.path.join(w2v_dir, 'W2V_model52320_50epochs.txt')
rows, cols = 0, 0
for i, line in enumerate(open(w2v_path, 'r')):
    if i == 0:
        rows, cols = line.split()
        rows, cols = int(rows), int(cols)
        nlp.vocab.reset_vectors(shape=(rows, cols))
    else:
        word, *vec = line.split()
        vec = np.array([float(i) for i in vec])
        nlp.vocab.set_vector(word, vec)
        print(word)



n_iter = 200

def trainModel(model=None, new_model_name="ACWS_Model", output_dir=output_dir, n_iter=50):
    from spaCy_ModelTrainingData_withCellTypes.py import *
    """Set up the pipeline and entity recognizer, and train the new entity."""
    random.seed(0)
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("en")  # create blank Language class
        print("Created blank 'en' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    
    nlp = spacy.load(output_dir)
    
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe("ner")

    ner.add_label(LABEL)  # add new entity label to entity recognizer
    ner.add_label(CIT)
    ner.add_label(NT)
    ner.add_label(PHYS)
    ner.add_label(FUNC)
    ner.add_label(CELL)
    nlp.vocab.vectors.name='W2V_Vectors'
    if model is None:
        optimizer = nlp.begin_training()
    else:
        optimizer = nlp.resume_training()
    move_names = list(ner.move_names)
    # get names of other pipes to disable them during training
    pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
    with nlp.disable_pipes(*other_pipes):  # only train NER
        sizes = compounding(1.0, 4.0, 1.001)
        # batch up the examples using spaCy's minibatch
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            batches = minibatch(TRAIN_DATA, size=sizes)
            losses = {}
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.5, losses=losses)
            print("Iteration ", str(itn), "Losses", losses)

        
resultDirectory = '/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/Results/'
output_dir = '/home/smith/Smith_Scripts/NLP_GeneExpression/spaCy_model062920/'

# save model to output directory
if output_dir is not None:
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir()
   # nlp.meta["name"] = "ACWS_REGION_MODEL"  # rename model
    nlp.to_disk(output_dir)
    print("Saved model to", output_dir)
    
