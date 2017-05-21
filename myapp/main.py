#!/usr/bin/python2.7

import os, shutil

from myapp.getCcl import getCcl
from myapp.lematize import lematize
from myapp.createModel import createModel
from myapp.Word2VecModel import Word2VecModel
from myapp.Word2VecModelCSVOutputHelper import Word2VecModelCSVOutputHelper

cclout = 'cclout/'
lematizedout = 'lematizedout/'

def createDirs(textin, modelout):
    if (not os.path.exists(textin)):
        os.makedirs(textin)
    if (not os.path.exists(cclout)):
        os.makedirs(cclout)
    if (not os.path.exists(lematizedout)):
        os.makedirs(lematizedout)
    if (not os.path.exists(modelout)):
        os.makedirs(modelout)

def removeTempDirs():
    shutil.rmtree(cclout);
    shutil.rmtree(lematizedout);

def run(textin, modelout, modelname,
        flexems=["subst", "depr",
                 "adj", "adja", "adjp", "adjc",
                 "fin", "bedzie", "aglt", "praet", "impt", "imps", "inf", "pcon", "pant", "ger", "pact", "ppas"]):
    if (not textin.endswith("/")):
        textin += "/"
    if (not modelout.endswith("/")):
        modelout += "/"

    createDirs(textin, modelout);
    getCcl(textin+'*', cclout);
    lematize(cclout+'*', lematizedout, flexems);
    createModel(lematizedout, modelout, modelname);
    removeTempDirs();

def testModel(modelout, modelname):
    if (not modelout.endswith("/")):
        modelout += "/";

    word2VecModel = Word2VecModel();
    word2VecModel.loadModel(modelout, modelname);

    csvOutputHelper = Word2VecModelCSVOutputHelper(word2VecModel);
    # Wszystkie slowa w modelu:
    words = csvOutputHelper.getWordsInModelCSV();
    print("%s" % words);
    # Wszystkie slowa w modelu koniec.

    # Macierz podobienstwa slow:
    simmatrix = csvOutputHelper.getSimilarityMatrixCSV([["wiosna", "lato"], ["serce", "szabla"], ["zima", "noga"]]);
    print("%s" % simmatrix);
    # Macierz podobienstwa slow koniec.

    # Macierz podobienstwa slowa do zestawu slow:
    simmatrix2 = csvOutputHelper.getWordSimilarityMatrixCSV("wiosna", ["lato", "serce", "szabla", "zima", "noga"]);
    print("%s" % simmatrix2);
    # Macierz podobienstwa slowa do zestawu slow koniec.

    # Najbardziej podobne slowa (do klikadelka):
    mostsim = word2VecModel.mostSimilar(['szabla'], [], 5);
    for pair in mostsim:
        print('most similar: [%s, %s]' % (pair[0], pair[1]));
    # Najbardziej podobne slowa (do klikadelka) koniec.

    # Niepasujace slowa (do klikadelka):
    print('doesn\'t match: %s' % word2VecModel.doesntMatch(['wiosna', 'lato', 'zima', 'noga']));
    # Niepasujace slowa (do klikadelka) koniec.

    # Podobienstwa slow lczbowe (do klikadelka):
    print('similar: %f' % word2VecModel.similarity('serce', 'szabla'));
    # Podobienstwa slow lczbowe (do klikadelka) koniec.

if __name__ == '__main__':
    run("paczka", "modelout", "model");
    testModel("modelout", "model");