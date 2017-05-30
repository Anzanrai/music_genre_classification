import numpy as np
#import kmean
#import gmm
import pickle
import os
from sklearn import mixture
#from gmm import norm_pdf_multivariate
ncomponents = 16
filenames = []
path = "C:/Users/dipen/Downloads/music genre recognition/"




for file in os.listdir(path):
    if file.endswith(".dat"):
        filenames.append(file)

for files in filenames:
    data = np.loadtxt(files)
    gmm_model = mixture.GMM(n_components=ncomponents).fit(data)
    name, extension = files.split('.')
    name = name + ".bin"
    fileobject = open(name, 'wb')
    pickle.dump(gmm_model, fileobject)
    fileobject.close()

#data = np.loadtxt('mfccs.dat')

#gmm = mixture.GMM(n_components = 4).fit(data)
#print "Done"
#print gmm.means_
#
#  data = sklearn.
# mu = np.mean(data, 0)
# sig = np.std(data, 0)
# size, dimension = data.shape
# # #data = data[0:int(size/4)][:]
# data = (data-mu)/sig
# gmm = mixture.GMM(n_components = ncomponents).fit(data)



#datatrans = np.transpose(data)
# dimension, size = np.shape(data)
#
# ncomponents = 4
# #sigma = range(0,ncomponents)
# meanarr, cluster, sigma, mixturewts = kmean.kmeans(data, ncomponents, 1)
# initial_gmmparameters = [meanarr, sigma, mixturewts]
# gmm.gmmfit(initial_gmmparameters, data, ncomponents)
# #
