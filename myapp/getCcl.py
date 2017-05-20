#!/usr/bin/python2.7

import json
import urllib2
import glob, os
import time
import zipfile

url="http://ws.clarin-pl.eu/nlprest2/base" 

def readFile(fileName):
    with open (fileName, "r") as myfile:
        return myfile.read();

def saveFile(directory, fileName, content):
    with open (directory + os.path.basename(fileName), "w") as outfile:
        outfile.write(content);

def extractZip(directory, fileName):
    with zipfile.ZipFile(directory + os.path.basename(fileName), "r") as zipref:
        zipref.extractall(directory)

def deleteFile(directory, fileName):
    os.remove(directory + os.path.basename(fileName))

def upload(fileName, payload):
    print("Starting upload %s" % (fileName))
    data = urllib2.urlopen(urllib2.Request(url+'/upload/',payload,{'Content-Type': 'binary/octet-stream'})).read();
    print("Upload done!")
    return data;

def download(fileName, fileID):
    print("Starting download %s" % (fileName))
    content = urllib2.urlopen(urllib2.Request(url+'/download'+fileID)).read();
    print("Download done!")
    return content;

def tool(lpmn,user): 
    data={}
    data['lpmn'] = lpmn
    data['user'] = user
    request = json.dumps(data)

    taskid = urllib2.urlopen(urllib2.Request(url+'/startTask/',request,{'Content-Type': 'application/json'})).read();
    time.sleep(0.1);
    response = urllib2.urlopen(urllib2.Request(url+'/getStatus/'+taskid));

    data=json.load(response)
    while(data["status"] == "QUEUE" or data["status"] == "PROCESSING"):
        print("%s: %.1f%%" % (data["status"], 100*data["value"]));
        time.sleep(1);
        response = urllib2.urlopen(urllib2.Request(url+'/getStatus/'+taskid));
        data = json.load(response)

    if(data["status"]=="ERROR"):
        print("Error "+data["value"]);
        return None

    print("Processing done!");
    return data["value"];

def getCcl(input, output):
    print("input: %s, output: %s" % (input, output));
    globalTime = time.time();
    for fileName in glob.glob(input):
        fileTime = time.time();
        identity = upload(fileName, readFile(fileName));
        if(fileName.endswith(".zip")):
            data = tool('filezip('+identity+')|any2txt|wcrft2({\"model\":\"names\"})|makezip','adres e-mail')
        else:
            data = tool('file('+identity+')|any2txt|wcrft2|liner2({\"model\":\"names\"})','adres e-mail')

        if(data == None):
            continue;

        fileID = data[0]["fileID"];
        saveFile(output, fileName, download(fileName, fileID));

        if (fileName.endswith(".zip")):
            extractZip(output, fileName)
            deleteFile(output, fileName)
        
        print("File %s: %s seconds" % (fileName, time.time() - fileTime))
    print("GLOBAL %s seconds" % (time.time() - globalTime))    

if __name__ == '__main__':
    getCcl('paczka/*', 'cclout/')