#!/bin/bash
now=$(date "+%F_%H%m")
python -m spacy train config.cfg --output model_$now --paths.train ./train.spacy --paths.dev ./validation.spacy --gpu-id 0
