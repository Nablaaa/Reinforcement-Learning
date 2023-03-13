"""
author: Eric Schmidt
Description:
Computational check, which influence beta has on the choice of a 
softmax driven decision policy.

the probability exp(beta * (Q1 - Q2)) is high,
for high difference of Q1 - Q2
and for high beta

High beta leads to a high probability for one case
and hence, this action is choosen more often by the
policy (even when it is not the best!)

Low beta makes decision random (50:50)

Beta = 1 makes the decision by a ratio Q1/Q2

"""


import numpy as np

def p(qa, qb, beta):
    Z = np.exp(beta*qa) + np.exp(beta*qb)
    
    pa = np.exp(beta*qa)/Z
    #pb = np.exp(beta*qb)/Z
    
    return pa
    

def Q_estimate(Q_old, reward, eta):
    return Q_old + eta * (reward - Q_old)


def Action(pa):
    random_number = np.random.uniform(0,1,1)
    if random_number <= pa:
        action = 0
        
    else:
        action = 1
        
    return action


def Reward(action):
    if action == 0:
        reward = 0.5
    else:
        reward = 1
        
    return reward



if __name__ == "__main__":
    print(__doc__)

    beta = 0.1
    eta = 0.1

    Q = np.asarray([0.1,0.1])

    action_counter = np.zeros(2)
    for i in range(1000):
        prob_a = p(Q[0], Q[1], beta)
        action = Action(prob_a)
        
        action_counter[action] = action_counter[action] + 1
        reward = Reward(action)
        
        Q[action] = Q_estimate(Q[action], reward, eta)
        
        if i ==100:
            print(action_counter)
        
    print(Q)
    print(action_counter)
