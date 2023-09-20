import os.path,logging,sys,multiprocessing,string
from gensim.models import word2vec
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words(sys.argv[2]))
punctuation = set(punctuation)

class MySentences(object):
    def __init__(self, dirnameP):
        self.dirnameP = dirnameP
    def __iter__(self):
        for subdir in os.listdir(self.dirnameP):
            print(subdir)
            if subdir==".DS_Store":
                continue
            subdirpath=os.path.join(self.dirnameP,subdir)
            print(subdirpath)
            for fname in os.listdir(subdirpath):
                if fname[:4]=="wiki":
                    for line in open(os.path.join(subdirpath, fname)):
                        linelist=word_tokenize(line)
                        if len(linelist)>3 and linelist[0][0]!="<":
                            yield [w.lower().strip() for w in linelist if w not in stop_words and w not in punctuation]

# old punctuation ",."" \" () :; ! ?"

def main() :
   program = os.path.basename(sys.argv[0])
   logger = logging.getLogger(program)

   logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
   logging.root.setLevel(level=logging.INFO)
   logger.info("running %s" % ' '.join(sys.argv))

   modelName=sys.argv[1]
   try :
       model=word2vec.Word2Vec.load(modelName)
       print("Already existing model is loaded")
   except :
       print("Model doesn't exist. Training of word2vec model started.")
       sentences = MySentences("text/") # a memory-friendly iterator
       model = word2vec.Word2Vec(sentences,vector_size=400,window=5,min_count=5,workers=multiprocessing.cpu_count())
       print("Le vecteur est terminé !!!")
   model.init_sims(replace=True)
   model.save(modelName)

if __name__ == '__main__':
#   try :
       sys.exit(main())
#   except Exception as e :
#       print(e)
#       rollbar.report_exec_info()
#       exit()
