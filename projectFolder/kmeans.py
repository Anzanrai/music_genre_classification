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

def initmeansrandomly (data,dim,ncomponents):
    # this function is to initialize means randomly;
    np.random.seed(4)
    meanval = np.ceil(np.max(data))
    #maxval = np.ceil(maxval)
    initialmeans = meanval*np.random.random_sample((ncomponents,dim)) - meanval;
    initialmeans = np.array(initialmeans);
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
    return cluster

def calculatemeans(clusters,ncomponents,dim):
    means = np.zeros((ncomponents,dim),dtype=float)
    for i in range (0,ncomponents):
        means[i] = clusters[i].mean(axis=0);

    return means;

def generate(data,ncomponents):

    x = np.zeros(ncomponents,dtype=float)
    x[0] = np.mean(data)
    i = 1
    while i<=ncomponents:
        x[i] = rand_num(x[i-1])
        i = i+1

    return x



def rand_num(x):
    a = 32
    c = 16
    m = 100
    r = ((x*a)+c)%m
    return (r)


def kmeans (data,ncomponents,boolval):
    # boolval =1 then randomly initialize means
    # boolval = 0 then means are initialized via quantization
    size = data.shape
    dim = size[1]

    if(boolval==1):
        initialmeans = initmeansrandomly(data,dim,ncomponents)
    else:
        initialmeans = generate(data,ncomponents)
    print initialmeans
    cluster = range(0,ncomponents)
    i= 0
    while True:
        cluster = formcluster(data, ncomponents, initialmeans)
        newmeans = calculatemeans(cluster,ncomponents,dim)
        #print newmeans
        distarr = vect_dist(initialmeans,newmeans)
        if (distarr[distarr.argmax()]<0.00001):
            break
        else:
            initialmeans = newmeans
        i = i+1
    #print newmeans
    print i
    print '*******************************************************************************************************'
    return newmeans
    #print cluster
    print cluster[0]
    #distancearr =
    #for i in range(0,ncomponents):





#dat = [random.randint(1,3000) for _ in xrange(10000)]
#dat = np.array(dat)
#dat = dat.reshape(500,20)
#kmeans(dat,5,1)



