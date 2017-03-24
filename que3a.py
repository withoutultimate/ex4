# Question 3a
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
    cvgcounter = [0,0]
    
    
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
        while(p[0]!=1 and p[1]!=1):
            action = getAction(p)
            respond = env(action, c1, c2)
            p = updateProb(p, respond, action)
            if(p[0] == 1):
                cvgcounter[0]+=1
            elif(p[1] == 1):
                cvgcounter[1]+=1

    return [x/L for x in cvgcounter];

############################################################
## Start Simulation

# set c1 and c2
c2 = 0.7

# number of steps for each simulation
#N = 2000

# after which step, start counting
#S = 0

# number of experiments for a single simulation
L = 100000

# set kr
kr = 0.2

for c1 in np.arange(0.05, 0.7, 0.1):
    print("\n************************************************************")
    print("c1 =",c1)
    result = simulateLRI(c1, c2, kr, L)
    print("Accuracy:",result[0])

