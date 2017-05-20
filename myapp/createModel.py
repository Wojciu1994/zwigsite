#!/usr/bin/python2.7

import gensim
import os, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

class Word2VecModel:
    def __init__(self, sentences):
        self.model = gensim.models.Word2Vec(sentences, min_count=10, workers=8);

    def trainModel(self, sentences):
        self.model.train(sentences);

    def saveModel(self, directory, fileName):
        self.model.save(directory + os.path.basename(fileName));

    def loadModel(self, fileName):
        self.model = gensim.models.KeyedVectors.load_word2vec_format(fileName, binary=True)
    
    def mostSimilar(self, positiveWords, negativeWords=[], topN=1):
        mostsim = self.model.most_similar(positive=positiveWords, negative=negativeWords, topn=topN)
        for pair in mostsim:
            print ('most similar: %s' % pair[0])

    def doesntMatch(self, wordList):
        doesntmatch = self.model.doesnt_match(wordList)
        print ('doesn\'t match: %s' % doesntmatch)

    def similarity(self, firstWord, secondWord):
        sim = self.model.similarity(firstWord, secondWord)
        print ('similar: %f' % sim)

def testModel(model):
    model.mostSimilar(['Polska'], [], 5);
    model.doesntMatch(['pies', 'kot', 'mysz', 'miasto'])
    model.similarity('brat', 'siostra')

def createModel(input, output, modelName):
    print("input: %s, output: %s" % (input, output));
    sentences = MySentences(input);
    word2VecModel = Word2VecModel(sentences);
    word2VecModel.saveModel(output, modelName);
    # testModel(word2VecModel);

if __name__ == '__main__':
    createModel('lematizedout/', 'modelout/');
