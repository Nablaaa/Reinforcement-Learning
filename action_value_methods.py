"""
author: Eric Schmidt
Description:
Nonstationary Reinforcement learning problem (like most of the real problems)
- Modified version of the 10-armed testbed, where the real reward estimations start out equal
but then take independent random walks (adding normally distributed increment with \mu=0, \sigma=0.01
- Implement action-value method with sample averages, incrementatlly computed
$Q_{n+1} = Q_n + \frac{1}{n} [R_n - Q_n]$
- Implement another method using constant step size parameter  alpha=0.1, epsilon = 0.1
$New \ estimate = Old \ estimate + Stepsize \cdot [Target - Old \ Estimate]$
"""

import matplotlib.pyplot as plt
import numpy as np
# np.random.seed(42)
# create the arms as 10 different actions
# they should give out 0 in the beginning and then in every next step they should give  random walk next value


class Bandit():
    def __init__(self):
        self.reward = np.ones(10,dtype='float16')
        #self.reward = np.asarray([1,2,3,4,5,6,7,8,9,10],dtype='float16')

    def randomReward(self):
        mu = 0
        sigma = 0.1
        return np.random.normal(mu,sigma,1)


    def getReward(self,action):
        self.reward[action] = self.reward[action] + self.randomReward()
        return self.reward[action]


def epsilonGreedy(reward_list, epsilon=0.1):
    random_number = np.random.uniform(0, 1)

    # be in 1 - epsilon of the cases greedy
    if random_number > epsilon:
        action = np.argmax(reward_list)

    # explore in epsilon of the cases
    else:
        action = np.random.randint(0,len(reward_list))

    return action


def AverageApproximation(previous, actual, n):
    return previous + 1/n * (actual - previous)



N = 1000
Av = 1


bandit = Bandit()
reward_list_expected = np.zeros(10)
print(reward_list_expected)
action_counter = np.zeros(10)


av_reward_per_step = []
av_highest_bandit_reward_per_step = []

sum_reward = 0
plt.figure()

for j in range(Av):
    step_reward = []
    bandit_max = []
    for i in range(N):
        # choose an action
        action = epsilonGreedy(reward_list_expected)
        action_counter[action] +=1

        # previous reward
        expected_reward = reward_list_expected[action]

        # get new reward based on policy
        bandit_reward = bandit.getReward(action)


        sum_reward += bandit_reward
        plt.scatter(j*N + i,sum_reward)


        # update expectation for the reward
        n = action_counter[action]
        reward_list_expected[action] = AverageApproximation(expected_reward, bandit_reward, n)

        bandit_max.append(np.max(bandit.reward))
        step_reward.append(bandit_reward)

    if j == 0:
        av_reward_per_step = np.asarray(step_reward)
        av_highest_bandit_reward_per_step = np.asarray(bandit_max)
    else:
        av_reward_per_step = 1/2 * (av_reward_per_step + np.asarray(step_reward))
        av_highest_bandit_reward_per_step = 1/2 * (av_highest_bandit_reward_per_step + np.asarray(bandit_max))


plt.show()


print(action_counter)
plt.figure()
plt.scatter(np.arange(len(av_reward_per_step)),av_reward_per_step,label="machine", alpha=0.1)
plt.plot(np.arange(len(av_highest_bandit_reward_per_step)),av_highest_bandit_reward_per_step,label="bandit")
plt.legend()





av_reward_per_step = []
av_highest_bandit_reward_per_step = []

for j in range(Av):
    step_reward = []
    bandit_max = []
    for i in range(N):
        # choose an action
        action = epsilonGreedy(reward_list_expected)
        action_counter[action] +=1

        # previous reward
        expected_reward = reward_list_expected[action]

        # get new reward based on policy
        bandit_reward = bandit.getReward(action)

        # update expectation for the reward
        n = action_counter[action]
        reward_list_expected[action] = AverageApproximation(expected_reward, bandit_reward, 1/0.1)

        bandit_max.append(np.max(bandit.reward))
        step_reward.append(bandit_reward)

    if j == 0:
        av_reward_per_step = np.asarray(step_reward)
        av_highest_bandit_reward_per_step = np.asarray(bandit_max)
    else:
        av_reward_per_step = 1/2 * (av_reward_per_step + np.asarray(step_reward))
        av_highest_bandit_reward_per_step = 1/2 * (av_highest_bandit_reward_per_step + np.asarray(bandit_max))


plt.figure()

plt.scatter(np.arange(len(av_reward_per_step)),av_reward_per_step,label="machine 2", alpha=0.1)
plt.plot(np.arange(len(av_highest_bandit_reward_per_step)),av_highest_bandit_reward_per_step,label="bandit 2")
plt.legend()
plt.show()

# update expectation

# do this 10 000 times
