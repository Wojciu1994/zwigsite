#!/usr/bin/python2.7

import os, shutil

from myapp.getCcl import getCcl
from myapp.lematize import lematize
from myapp.createModel import createModel

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

def run(textin, modelout, modelname):
    if (not textin.endswith("/")):
        textin += "/"
    if (not modelout.endswith("/")):
        modelout += "/"

    createDirs(textin, modelout);
    getCcl(textin+'*', cclout);
    lematize(cclout+'*', lematizedout);
    createModel(lematizedout, modelout, modelname);
    removeTempDirs();

if __name__ == '__main__':
    run("paczka", "modelout", "model"); 