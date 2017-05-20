#!/usr/bin/python2.7

import glob, os
import time
import xml.etree.ElementTree

def isInterestingCtag(ctag):
    return True;

def processLex(lex):
    ctag = lex.find('ctag').text;

    if(isInterestingCtag(ctag)):
        return lex.find('base').text + ' ';
    else:
        return '';

def processTok(tok):
    lematizedOutput = '';
    for lex in tok.iter('lex'):
        lematizedOutput += processLex(lex);

    return lematizedOutput;

def processSentence(sentence):
    lematizedOutput = '';
    for tok in sentence.iter('tok'):
        lematizedOutput += processTok(tok);

    return lematizedOutput;

def processChunk(chunk):
    lematizedOutput = '';
    for sentence in chunk:
        lematizedOutput += processSentence(sentence);

    return lematizedOutput;

def processChunkList(chunkList):
    lematizedOutput = '';
    for chunk in chunkList:
        lematizedOutput += processChunk(chunk);

    return lematizedOutput;

def lematizeCclXml(xmlRoot):
    print("Starting lematizing Ccl xml");
    lematizedOutput = processChunkList(xmlRoot);
    print("Lematizing done!")
    return lematizedOutput;

def deserializeXml(fileName):
    print("Starting deserializing xml %s" % (fileName));
    tree = xml.etree.ElementTree.parse(fileName)
    root = tree.getroot();
    print("Deserializing done!")
    return root;

def saveFile(directory, fileName, content):
    with open (directory + os.path.basename(fileName) + '.txt', "w") as outfile:
        outfile.write(content);

def lematize(input, output):
    print("input: %s, output: %s" % (input, output));
    globalTime = time.time();
    for fileName in glob.glob(input):
        fileTime = time.time();
        xmlRoot = deserializeXml(fileName);
        lematizedOutput = lematizeCclXml(xmlRoot);
        saveFile(output, fileName, lematizedOutput.encode('utf-8').strip());

        print("File %s: %s seconds" % (fileName, time.time() - fileTime))
    print("GLOBAL %s seconds" % (time.time() - globalTime))  

if __name__ == '__main__':
    lematize('cclout/*', 'lematizedout/');