#!/usr/bin/python2.7

import gensim, os, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class Word2VecModel:

    def __init__(self, sentences=None):
        if sentences is not None:
            self.model = gensim.models.Word2Vec(sentences, min_count=10, workers=8);

    def trainModel(self, sentences):
        self.model.train(sentences);

    def saveModel(self, directory, fileName):
        self.model.save(directory + os.path.basename(fileName));

    def loadModel(self, directory, fileName):
        self.model = gensim.models.Word2Vec.load(directory + os.path.basename(fileName));

    def loadBinaryModel(self, directory, fileName):
        self.model = gensim.models.KeyedVectors.load_word2vec_format(directory + os.path.basename(fileName), binary=True)
    
    def mostSimilar(self, positiveWords, negativeWords=[], topN=1):
        return self.model.most_similar(positive=positiveWords, negative=negativeWords, topn=topN);

    def doesntMatch(self, wordList):
        return self.model.doesnt_match(wordList);

    def similarity(self, firstWord, secondWord):
        return self.model.similarity(firstWord, secondWord);

    def getAllModelWords(self):
        return self.model.wv.vocab.keys();
