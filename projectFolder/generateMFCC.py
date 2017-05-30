import scipy.io.wavfile
import MFCC
import numpy as np

def loadWavFile(filename):
    w = scipy.io.wavfile.read(filename)
    x = w[1]    # data is returned as a numpy array with a data-type determined from the file
    fs = w[0]    # Sample rate of wav file as python integer
    return x

def generate_mfcc(filename, task = 'train', verbose = False):
    rawdata = loadWavFile(filename)
    if task == 'test':
        data = np.array(rawdata[60*44100 : (60+10)*44100][:], dtype = float) #for 30ms data
    elif task == 'train':
        data = np.array(rawdata[60*44100 : (60+90)*44100][:], dtype = float) #for 30ms data 
     
    mfcc = MFCC.extract(data, show=False)
    #mfcc = mfcc.T
    return mfcc