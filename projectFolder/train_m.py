import Tkinter
import tkFileDialog
import os
import generateMFCC as g
import numpy as np
from sklearn.mixture import GMM 
import pickle

song_list = 20

def splitstr(str):
    strlist = str.split("/")
    return strlist[-1]
    

def train():
    ncomponents = 16
    path = tkFileDialog.askdirectory()
    
    genrename = splitstr(path)
    print genrename
    #print(dlg)
    modelfile = genrename+".dat"
    filenames = []
    features = []
    for file in os.listdir(path):
        fpath =  path+"/"+file
        if file.endswith(".wav"):
            feature=g.generate_mfcc(fpath)
            filehandle = open(modelfile,'a')
            np.savetxt(filehandle, feature)
            filehandle.close()  
    
    
    featvect = np.loadtxt(modelfile)
    gmm_model = GMM(n_components=ncomponents).fit(featvect)
    modelname = genrename+".bin"
    fileobj= open(modelname,'wb')
    pickle.dump(gmm_model, fileobj)
    fileobj.close()
    print("finish")
    
    