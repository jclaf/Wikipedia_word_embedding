# Wikipedia_word_embedding
University Paris 8 - Text mining project for Master 2 Big Data

## Requirements
### Language programming
- python
  
### Install library
- nltk
- gensim
- string
- wikiextractor
- logging

## Recommandation 
- Name your model with this .model extension.
- Use command screen to save your session
  
## Run project

First, extract the data from your wikipedia dump with the wikiextractor library. Use the following command : `python3 -m wikiextractor.WikiExtractor --json <Wikipedia dump file>` .

A "text" folder is created with several json files.

Use this command to create a vector with the previous folder : `python3 w2v.py <Model name> <language for stopword>` .

Use this command to test vector that has been created : `python3 w2v.py <Model name>` or `python3 read_w2v.py <Model name>`.
