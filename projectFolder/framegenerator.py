import scipy.io.wavfile as wav
import numpy as np
#import MFCC


Fs = 16000;
winLen = int(0.01*Fs);
winOverlap = int(0.5*winLen);
def framegenerator():
    path = 'C:/Users/Anzaan/Documents/Matlab/major/classic/'
    filename = 'Schumann_CarnavalOp.9.wav'
    song = path+filename;
    rate,samples = wav.read(song);
        # print samples
    samples = samples[1323000:2646000:1]
    samples = np.mean(samples,axis=1)
    #print samples.shape
    #raw_input()
    return samples

def extractfeatures():
    rawdata = framegenerator()
    print rawdata
    
"""features = MFCC.extract(x,show=False)
print features
raw_input()"""
