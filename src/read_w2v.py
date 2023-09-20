from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

import logging
import os.path
import sys

program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)

logging.basicConfig(format='%(asctime)s : %(levelname)s :%(message)s')
logging.root.setLevel(level=logging.INFO)
logger.info("running %s" % ' '.join(sys.argv))

model = Word2Vec.load(sys.argv[1])

print("type",type(model))

print(model.wv.most_similar(positive=[sys.argv[2]],topn=20))


print("Number of words in the corpus used for training the model: ",model.corpus_count)
print("Number of words in the model: ",len(model.wv.index_to_key))
print("Time [s], required for training the model: ",model.total_train_time)
print("Count of trainings performed to generate this model: ",model.train_count)
print("Length of the word2vec vectors: ",model.vector_size)
print("Applied context length for generating the model: ",model.window)

