###############################################################################
#       import MFCC
#       x = ...         # x is a wave signal saved in a 1-D numpy array
#       mfcc = MFCC.extract(x)
#                       # mfcc is a 2-D numpy array, where each row is the
#                       # MFCC of a frame in x
#       mfcc = MFCC.extract(x, show = True)
#                       # This will also plot the MFCC and the spectrogram
#                       # reconstructed from MFCC by inverse DCT
###############################################################################

from numpy import *
from numpy.linalg import *
from scipy.fftpack import dct
from matplotlib.pyplot import *


def hamming(n):
    """
    Generate a hamming window of n points as a numpy array.
    """
    return 0.54 - 0.46 * cos(2 * pi / (n-1) * arange(n))


def melfb(p, n, fs):
    """
    Return a Mel filterbank matrix as a numpy array.
    Inputs:
        p:  number of filters in the filterbank
        n:  length of fft
        fs: sample rate in Hz
    Ref. http://www.ifp.illinois.edu/~minhdo/teaching/speaker_recognition/code/melfb.m
    """
    f0 = 700.0 / fs
    fn2 = int(floor(n / 2))
    lr = log(1 + 0.5 / f0) / (p + 1)
    CF = fs * f0 * (exp(arange(1, p + 1) * lr) - 1)
    bl = n * f0 * (exp(array([0, 1, p, p + 1]) * lr) - 1)
    b1 = int(floor(bl[0])) + 1
    b2 = int(ceil(bl[1]))
    b3 = int(floor(bl[2]))
    b4 = min(fn2, int(ceil(bl[3]))) - 1
    pf = log(1 + arange(b1, b4 + 1) / f0 / n) / lr
    fp = floor(pf)
    pm = pf - fp
    M = zeros((p, 1 + fn2))
    for c in range(b2 - 1, b4):
        r = fp[c] - 1
        M[r, c + 1] += 2 * (1 - pm[c])
    for c in range(b3):
        r = fp[c]
        M[r, c + 1] += 2 * pm[c]
    return M, CF


FS = 16000                              # Sampling rate
FRAME_LEN = int(0.025 * FS)             # Frame length
FRAME_SHIFT = int(0.01 * FS)            # Frame shift
FFT_SIZE = 2048                         # How many points for FFT
WINDOW = hamming(FRAME_LEN)             # Window function
PRE_EMPH = 0.95                         # Pre-emphasis factor

BANDS = 32                              # Number of Mel filters
POWER_SPECTRUM_FLOOR = 1e-100           # Flooring for the power to avoid log(0)
M, CF = melfb(BANDS, FFT_SIZE, FS)      # The Mel filterbank matrix and the center frequencies of each band


def extract(x, show=False):
    
    """
    Extract MFCC coefficients of the sound x in numpy array format.
    """
    if x.ndim > 1:
        print "INFO: Input signal has more than 1 channel; the channels will be averaged."
        x = mean(x, axis=1)
    frames = (len(x) - FRAME_LEN) / FRAME_SHIFT + 1

    # Removal of silence part
    energies = []
    frms = []
    for f in range(frames):
        frame = x[f*FRAME_SHIFT: f*FRAME_SHIFT+FRAME_LEN]
        energies.append(mean(square(frame)))
    threshold_energy = median(energies)
    for index,f in enumerate(range(frames)):
        frame = x[f*FRAME_SHIFT: f*FRAME_SHIFT+FRAME_LEN]
        if threshold_energy < energies[index]:
            frms.append(frame)
 
    feature = []
    for f in frms:
        # Windowing
        frame = f
        frame = frame * WINDOW
        # Pre-emphasis
        frame[1:] -= frame[:-1] * PRE_EMPH
        # Power spectrum
        X = (abs(fft.fft(frame, FFT_SIZE))[:FFT_SIZE / 2 + 1] ** 2) / FRAME_LEN
        X[X < POWER_SPECTRUM_FLOOR] = POWER_SPECTRUM_FLOOR  # Avoid zero
        # Mel filtering, logarithm, DCT
        # Raising the log-mel-amplitudes to a suitable power (around 2 or 3) before taking the DCT reduces the influence of low-energy components
        X = dct(log(dot(M, X))**3)
        feature.append(X)
    feature = row_stack(feature)
    # Show the MFCC spectrum before normalization
    # if show:
    #     show_MFCC_spectrum(feature)
    # Mean & variance normalization
    if feature.shape[0] > 1:
        mu = mean(feature, axis=0)
        sigma = std(feature, axis=0)
        feature = (feature - mu) / sigma

    # Show the MFCC
    if show:
        show_MFCC(feature)

    return feature


def show_MFCC(mfcc):
    """
    Show the MFCC as an image.
    """
    imshow(mfcc.T, aspect="auto", interpolation="none")
    title("MFCC features")
    xlabel("Frame")
    ylabel("Dimension")
    show()