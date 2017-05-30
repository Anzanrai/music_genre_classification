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
import random
a = [1,2,3,4,5,6,7,8,9]
data1 = np.array([1,11,23,78,75,65,1,2,36,59,54,3,2,56,7,5,6,21,45,6,3,2,1,45,8])
data1 = data1.reshape(5,5)
data2 = np.array([1,223,5,78,96,4,5,63,5,6,5,2,3,5,4,5,5,2,45,78])
data2 = data2.reshape(4,5)
data3 = np.array([1,56,2,47,23])
def main():
    sumval = 2*test(a)
    print sumval
    #print productval
    #print listval

def test(a):
    suma = np.sum(a)
    #product = np.prod(a)
    #lista = a[1:4]
    return suma
if __name__ == '__main__':
    main()
