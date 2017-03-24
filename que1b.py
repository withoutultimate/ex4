from que1a import simulateTseltlin
import math
import numpy as np
import numpy.linalg as linalg
import random


def getP1(N,c1,c2):
    return 1/(1+(c1/c2)**N * ((c1-(1-c1))/(c2-(1-c2)))*((c2**N - (1-c2)**N)/(c1**N - (1-c1)**N)))

def binarySearch(L,U,f, value):
    mid = math.ceil((L+U)/2)
    if (L == U or L+1 == U):
        return U
    elif(f(mid,c1,c2)< value):
        return binarySearch(mid,U,f,value)
    else:
        return binarySearch(L,mid,f,value)

def findMinNSatisfyingAcc(c1,c2):
    # Find an upper bound U of N such that p1 >= 0.95
    U = 1
    p1 = 0
    while p1 < accuracy:
        U *= 2
        p1 = getP1(U,c1,c2)

    #print('Binary search between', int(U/2), 'and', U)
    N = binarySearch(int(U/2),U, getP1, accuracy)
   
    if math.isnan(getP1(N,c1,c2)):
        print('Minimun N satisfying accuracy does not exist')
        return -1;
    else:
        print('Minimun N satisfying accuracy :', N)
        print('Accurate p1Ininity =', getP1(N,c1,c2))
        return N;
  #  print('p1NMinus1', getP1(N-1,c1,c2))
c2 = 0.7
accuracy = 0.95

for c1 in np.arange(0.05, 0.7, 0.1):
    print('******************************')
    print("c1 =",c1)
    N =  findMinNSatisfyingAcc(c1,c2)
    if N!=-1:
        print("Simulated P1Infinity:",simulateTseltlin(N, c1, c2)[0])
