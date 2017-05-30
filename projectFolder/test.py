import numpy as np
import os
import glob
import pickle
import operator as op
#import mfcc

#testfile name is returned here
testfile =

#mfcc value is computed here
# mfccs vectors are returned in "features"
modelpath = "C:/Users/anju/Documents/eclipse_workspace/MusicGenreClassification/"
modelnames = []

for file in os.listdir(modelpath):
    if file.endswith(".bin"):
        modelnames.append(file)


score_dict = {}
for files in modelnames:
    fileobject = open(files,'rb')
    name, extension = files.split(".")
    model = pickle.load(fileobject)
    score_dict[name] = sum(model.score(features))


genre = max(score_dict.iteritems(), key = op.itemgetter(1))[0]
print genre


def keywithmaxval(d):
     """ a) create a list of the dict's keys and values;
         b) return the key with the max value"""
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

genre = keywithmaxval(score_dict)
print genre
