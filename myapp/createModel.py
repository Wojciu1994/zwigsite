#!/usr/bin/python2.7

import gensim, os, logging
from Word2VecModel import Word2VecModel

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

def createModel(input, output, modelName):
    print("input: %s, output: %s" % (input, output));
    sentences = MySentences(input);
    word2VecModel = Word2VecModel(sentences);
    word2VecModel.saveModel(output, modelName);

if __name__ == '__main__':
    createModel('lematizedout/', 'modelout/');
