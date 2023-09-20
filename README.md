# Wikipedia_word_embedding
university Paris 8 - Text mining project for Master 2 Big Data

# Install library
- nltk
- gensim
- string
- wikiextractor
- logging
  
# Run project

First, extract the data from your wikipedia dump with the wikiextractor library. Use the following command : `python3 -m wikiextractor.WikiExtractor --json <Wikipedia dump file>` 
A "text" folder is created with several json files.

Use this command for create a vector with previous folder : `python3 w2v.py <Model name> <language for stopword>`
