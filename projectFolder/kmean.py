import numpy as np
import random
def initmeans (data,ncomponents):
    # here data is mfcc data that would be read from file and ncomponents = number of components;
    # shape of data would be num_of_vectors by num_of_dimensions
    size = data.shape;
    dim = size[1];
    maxarr = data.max(axis=0);

    minarr = data.min(axis=0);
    #print minarr
    #print maxarr
    difference = maxarr-minarr;
    incrementval = difference/(ncomponents+1);
    #print incrementval;
    initialmeans = np.zeros((ncomponents,dim),dtype=float);
    i=0;
    while i<ncomponents:
        initialmeans[i] = minarr + (i+1)*incrementval;
        i+=1;
    return initialmeans;

def initmeansrandomly (data,ncomponents,dimension):
    # this function is to initialize means randomly;
    random.seed(250)
    maxval = 9
    minval = -9

    initialmeans = random.sample(data,ncomponents)

    return initialmeans;

def vect_dist(data,meanvect):
    dist_arr = (((data-meanvect)**2).sum(axis=1));
    #print dist_arr
    return np.sqrt(dist_arr);

def formcluster(data,ncomponents,meanvect):
    #distancemat is a number_of_clusters by number_of_vectors matrix to store the distance calculated between each cluster mean and each vector
    distancemat = np.zeros((ncomponents,len(data)),dtype=float);
    for i in range(0,ncomponents):
        distancemat[i] = (vect_dist(data,meanvect[i]));
    #print distancemat.shape
    cluster_indx = distancemat.argmin(axis=0);
    #print cluster_indx;
    cluster = range(0,ncomponents)
    for i in range(0,ncomponents):
        cluster[i]=data[np.where(cluster_indx==i)]
        #print cluster[i]
    return cluster

def calculatemeans(clusters,ncomponents,dim):
    means = np.zeros((ncomponents,dim),dtype=float)
    for i in range (0,ncomponents):
        means[i] = clusters[i].mean(axis=0);

    return means;

def kmeans (data,ncomponents,boolval):
    # boolval =1 then randomly initialize means
    # boolval = 0 then means are initialized via quantization
    observation_num,dim = data.shape # dim = dimension will be the row necessary for covariance matrix calculation

    if(boolval==1):
        initialmeans = initmeansrandomly(data,ncomponents,dim)
    else:
        initialmeans = initmeans(data,ncomponents)

    #print 'initial means'
    #print initialmeans
    print '******************************************************'
    cluster = range(0,ncomponents)
    mixturewts = range(0,ncomponents)
    i=0
    sigma = range(0,ncomponents)
    while True:
        cluster = formcluster(data, ncomponents, initialmeans)
        #print cluster[1][:][:]
        newmeans = calculatemeans(cluster, ncomponents, dim)
        distarr = vect_dist(initialmeans, newmeans)
        if distarr[distarr.argmax()] < 0.001:
            t = 0
            while t<ncomponents:
                sigma[t] = np.cov(np.transpose(cluster[t]))
                cluster_rownum,dimension = np.shape(cluster[t])
                #assert isinstance(observation_num, object)
                mixturewts[t] = float(cluster_rownum)/observation_num
                t += 1
            break
        else:
            initialmeans = newmeans
        i += 1
        #print i
    print i
    #print cluster
    return newmeans, cluster, sigma, mixturewts










