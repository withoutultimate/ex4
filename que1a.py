# Question 1(a)
# Author: Haoye Lu
# Simulate a Tsetlin automaton 


import numpy as np
import numpy.linalg as linalg
import random

## Simulate Tseltlin automaton with two actions
 # N: the total number of states is 2N
 # c1, c2: panalty probability for action1 and action2
def simulateTseltlin(N, c1, c2):
    L = 50000 # number of steps in total
    S = 40000 # start counting after S steps
    R = 100 # number of experiments 
    
     # Create F0 and F1
    index0 = [0]
    index0.extend(list(range(0,N-1)))
    index0.extend([N])
    index0.extend(list(range(N, 2*N-1)))
    #print(index0)
    F0 =  [genElemVect(i,2*N) for i in index0]

    index1 = list(range(1,N))
    index1.extend([2*N-1])
    index1.extend(list(range(N+1, 2*N)))
    index1.extend([N-1])
    #print(index1)
    F1 =  [genElemVect(i,2*N) for i in index1]

    ## Start simulation
    actionCounter = [0,0]
    for e in range(R):
        state = random.randint(0, 2*N-1)  # random select a state from 2N states
        respond = random.randint(0, 1) # choose initial env respond randomly
        for i in range(S):
            if respond == 0:
                state = step(state,F0)
                if state < N:
                    respond = env(1,c1,c2)
                else:
                    respond = env(2,c1,c2)
            else:
                state = step(state, F1)
                if state < N:
                    respond = env(1,c1,c2)
                else:
                    respond = env(2,c1,c2)

        for i in range(L-S):
            if respond == 0:
                state = step(state,F0)
                if state < N:
                    respond = env(1,c1,c2)
                    actionCounter[0]+=1
                else:
                    respond = env(2,c1,c2)
                    actionCounter[1]+=1
            else:
                state = step(state, F1)
                if state < N:
                    respond = env(1,c1,c2)
                    actionCounter[0]+=1
                else:
                    respond = env(2,c1,c2)
                    actionCounter[1]+=1

    prob = [x /(R*(L-S)) for x in actionCounter]
    return prob


## Environment function
 # Given the action, return award(0)
 # or punish(1)
def env(action, c1, c2):
    rand = random.random()
    result = 0
    if action == 1:
        if rand <c1:
            result = 1
    else:
        if rand <c2:
            result = 1
    return result;

## Step function
 # Given the current state, give the next step
 # state according to the transition matrix
def step(state, F):
    return F[state].index(1);


## Genrate element vector
 # with length n and whose ith
 # entry is 1. The rests are 0s.
def genElemVect(i ,n):
    aList = [0]*n
    aList[i] = 1
    return aList;


print('\n\n')

# c2 = 0.7
# N = 3
# print("N=", N)
# for c1 in np.arange(0.05, 0.7, 0.1):
#     print("c1 =",c1)
#     result = simulateTseltlin(N, c1, c2)
#     print(result)
# print('\n\n')


# c2 = 0.7
# N = 5
# print("N=", N)
# for c1 in np.arange(0.05, 0.7, 0.1):
#     print("c1 =",c1)
#     result = simulateTseltlin(N, c1, c2)
#     print(result)
# print('\n\n')


# c2 = 0.7
# N = 10
# print("N=", N)
# for c1 in np.arange(0.05, 0.7, 0.1):
#     print("c1 =",c1)
#     result = simulateTseltlin(N, c1, c2)
#     print(result)
# print('\n\n')


c2 = 0.9
N = 20
print("N=", N)
for c1 in np.arange(0.05, 0.7, 0.1):
    print("c1 =",c1)
    result = simulateTseltlin(N, c1, c2)
    print(result)
print('\n\n')

