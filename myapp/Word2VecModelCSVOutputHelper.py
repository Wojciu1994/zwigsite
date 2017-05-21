#!/usr/bin/python2.7

import gensim, os, logging
from Word2VecModel import Word2VecModel

class Word2VecModelCSVOutputHelper:

    def __init__(self, word2VecModel):
        self.word2vecmodel = word2VecModel;

    def getSimilarityMatrixCSV(self, pairArray):
        matrix = "slowo1; slowo2; podobienstwo;\n"
        for pair in pairArray:
            sim = self.word2vecmodel.similarity(pair[0], pair[1]);
            matrix += pair[0] + "; " + pair[1] + "; " + str(sim) + ";\n"

        return matrix;

    def getWordsInModelCSV(self):
        words = '';
        for word in self.word2vecmodel.getAllModelWords():
            words += word + ";\n"

        return words;

    def getWordSimilarityMatrixCSV(self, word, otherWordsArray):
        matrix = "slowo1; slowo2; podobienstwo;\n"
        for otherWord in otherWordsArray:
            sim = self.word2vecmodel.similarity(word, otherWord);
            matrix += word + "; " + otherWord + "; " + str(sim) + ";\n"

        return matrix;
