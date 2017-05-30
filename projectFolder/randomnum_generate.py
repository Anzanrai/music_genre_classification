#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Anzaan
#
# Created:     12/08/2014
# Copyright:   (c) Anzaan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np

def generate(data,ncomponents):

    x = np.zeros(ncomponents,dtype=float)
    x[0] = data.mean
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

if __name__ == '__main__':
    main()