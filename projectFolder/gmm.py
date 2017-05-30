import numpy as np
import math
import sklearn


def norm_pdf_multivariate(x, mu, sigma):
    size = len(x)
    if size == len(mu) and (size, size) == sigma.shape:
        det = np.linalg.det(sigma)
        if det == 0:
            raise NameError("The covariance matrix can't be singular")

        norm_const = 1.0/(math.pow((2*np.pi), float(size)/2) * math.pow(det, 1.0/2))
        x_mu = (x - mu)
        inv = np.linalg.inv(sigma)
        result = np.e**(-0.5 * (x_mu * inv * x_mu.T))
        return norm_const * result
    else:
        raise NameError("The dimensions of the input don't match")


def emalgo(data, initial_mean, initial_covarmat, initial_mixwt, ncomponents):
    #*******************EM ALGORITHM************************************
    mu = initial_mean
    sigmaarr = initial_covarmat
    mixwt = initial_mixwt
    observation_num, dim = data.shape
    score = range(0, observation_num)
    gamma = range(0, dim)
    #iteration loop begins here
    difference = 1
    while difference != 0:
        #*******************EXPECTATION STEP*********************************
        i = 0
        j = 0
        k = 0
        while i < observation_num:
            total_val = 0
            while k < ncomponents:
                total_val += mixwt[k]*norm_pdf_multivariate(data[i], mu[k], sigmaarr[k])
                k += 1
            while j < ncomponents:
                gamma[j] = (mixwt[j]*norm_pdf_multivariate(data[i], mu[j], sigmaarr[j]))/total_val
                j += 1
            score[i] = gamma
        #*******************MAXIMIZATION STEP*******************************
        nk = score.sum(axis=0)                #nk = np.sum(score,axis=0) sum of score across corresponding dimension
        old_mu = mu
        mu = 1./nk*(np.sum(score*data, axis=0))
        sigmaarr = 1./nk*(np.sum(score*(data-mu)**2, axis=0))
        mixwt = nk/observation_num
        difference = np.sum((old_mu-mu)**2)
    return mu, sigmaarr, mixwt


def gmmfit(initial_gmmparameters,data,ncomponents):
    #*******************PORTION TO INITIALIZE PARAMETERS OF GMM*********
    initial_mean = initial_gmmparameters[0]
    initial_covarmat = initial_gmmparameters[1]
    initial_mixwt = initial_gmmparameters[2]
    mu, sigmaarr, mixwt = emalgo(data, initial_mean, initial_covarmat, initial_mixwt, ncomponents)
    return mu, sigmaarr, mixwt