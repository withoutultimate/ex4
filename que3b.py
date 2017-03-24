# Question 3b
# Author: Haoye Lu
# Simulate a L_{RI} automaton which is to interact
# with and environmnet with penalty probabilites (c1, c2)

import numpy as np
import numpy.linalg as linalg
import random


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

# ## Simulate  a L_{RI} automaton
# def simulateLRI(c1, c2, kr,  L, S):

#     ## Given an action distribution vector
#      # return an action according the prob
#     def getAction(v):
#         if(sum(v) != 1):
#             print('invalid dist vect')
#             return -1;
#         else:
#             if random.random()<v[0]:
#                 return 1 # choose action 1
#             else:
#                 return 2 # choose action 2

#     ## Update action probability vector
#      # according to the previous one,
#      # the respond from the environmnet
#      # and the action 
#     def updateProb(oldP, respond, action):
#         newP = oldP
#         if respond == 0:
#             if action == 1:
#                 newP = [(1- kr*oldP[1]),(kr*oldP[1])]
#             else:
#                 newP = [(kr*oldP[0]),(1-kr*oldP[0])]
#         return newP

#     stepToConverge = 0
    
#     for r in range(L):
#         # start from uniform distribution
#         p = [0.5, 0.5]
#         action1Counter = 0
#         for i in range(S):
#            # print(p)
#             #print(action1Counter)
#             action = getAction(p)
#             if action == 1:
#                 action1Counter += 1
#             respond = env(action,c1,c2)
#            # print(respond)
#             p = updateProb(p, respond, action)

            
#         action1Freq = action1Counter/S
#         loop = 0;
        
#         while(action1Freq < 0.95):
#             action = getAction(p)
#             if action == 1:
#                 action1Counter += 1
#             action1Freq = action1Counter/(S+loop)
#             respond = env(action,c1,c2)
#             p = updateProb(p, respond, action)
#             loop += 1
#             #print(action)
#             #print(p)
#             #print("# action1: ",action1Freq)
            
#         stepToConverge += (S+loop)
#         #print(r)

        
#     avgStepToConverge = stepToConverge / L

#     return avgStepToConverge;



## Simulate  a L_{RI} automaton
def simulateLRI(c1, c2, kr, L):

    ## Given an action distribution vector
     # return an action according the prob
    def getAction(v):
        if(sum(v) != 1):
            print('invalid dist vect')
            return -1;
        else:
            if random.random()<v[0]:
                return 1 # choose action 1
            else:
                return 2 # choose action 2

    ## Update action probability vector
     # according to the previous one,
     # the respond from the environmnet
     # and the action 
    def updateProb(oldP, respond, action):
        newP = oldP
        if respond == 0:
            if action == 1:
                newP = [(1- kr*oldP[1]),(kr*oldP[1])]
            else:
                newP = [(kr*oldP[0]),(1-kr*oldP[0])]
        return newP
            

    # counters for converging to [1 0] and [0 1] respectively
    cvgP1Counter = 0
    stepCounter = 0
    
    for r in range(L):
    # start from uniform distribution
        p = [0.5, 0.5]

        # for i in range(S):
        #     action = getAction(p)
        #     respond = env(action,c1,c2)
        #     p = updateProb(p, respond, action)

        # for i in range(N):
        #     action = getAction(p)
        #     actionCounter[action-1]+=1
        #     respond = env(action,c1,c2)
        #     p = updateProb(p, respond, action)

        #print(p)
        step = 0
        while(p[0]!=1 and p[1]!=1):
            action = getAction(p)
            respond = env(action, c1, c2)
            p = updateProb(p, respond, action)
            if(p[0] == 1):
                cvgP1Counter+=1
            step+=1
            #elif(p[1] == 1):
               #cvgcounter[1]+=1
        stepCounter+=step
    return [cvgP1Counter/L, stepCounter/L]

# Given: env panalty c1, c2
# Initial k1 and k2
# Required accuracy acc and the
# Number of experiments L
# Return: the kr that achieves the acc
# Assumption: the k1 <= kr <= k2
def findNecessaryKr(c1,c2,acc,k1, k2, L, err):
    kmid = (k1 + k2)/2
    [kmidAcc, cvgSpeed] = simulateLRI(c1, c2, kmid, L)
    #print('k1:', k1, 'k2:', k2)
    #print('kmidAcc',kmidAcc)
    if (0.95<kmidAcc and kmidAcc < 0.95+err):
        return [kmid, cvgSpeed]
    elif kmidAcc < 0.95:
        return findNecessaryKr(c1,c2,acc,kmid, k2, int(1.1*L), err);
    else:
        return findNecessaryKr(c1,c2,acc,k1, kmid, int(1.1*L), err);


############################################################
## Start Simulation

# set c1 and c2
c2 = 0.7

# number of steps before calculating the accuracy
S = 100

# number of experiments for a single simulation
L = 20000

c1 = 0.2

kr = 0.6

acc = 0.95

err = 0.005

#result = simulateLRI(c1, c2, kr, L)
#print(result)

for c1 in np.arange(0.05, 0.7, 0.1):
    print('******************************')
    print("c1 =",c1)
    [kr, cvgSpeed] =  findNecessaryKr(c1,c2,acc, 0.001, 0.999, L, err)
    print('lambdaR =',1-kr )
    print('Converging speed:', cvgSpeed)
    [recheckAcc, recheckSpeed] = simulateLRI(c1, c2, kr, 50000)
    print('Accuracy by reruning the simulation:', recheckAcc)
    print('Converging by reruning the simulation:', recheckSpeed)
    
