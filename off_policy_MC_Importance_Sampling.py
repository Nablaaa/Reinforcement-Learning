"""
author: Eric Schmidt
Description:
Example 5.5 in the Reinforcement Learning book from Sutton describes
a system in which the "ordinary" importance sampling fails due to
infinite variance. The "weighted" importance sampling performes
optimally from the beginning.

I want to reconstruct this system:
There is a state S, from which an agent can go a) LEFT or b) RIGHT
If the agent goes right, it reaches the goal immediately. Reward = 0.
If it goes left, then it happens nothing in 90 % of the cases, Reward=0.
In 10 percent of the cases the agent reaches the goal and gets Reward= +1.

Now there are two policies: target policy and behavior policy
The target policy pi(left|S) goes always left from state S.
The exploratory policy goes in 50 % of the cases to the left
and 50 % to the right b(left|S) = b(right|S) = 0.5

The policy should find the correct value for the state S (which is 1).


The program does not reach the state value V=1 for the left state.
The q_expected value for the left state is 1/11

I guess there must be an error in how I calculate the weights

"""
import numpy as np


def Target_policy(state):
    """The target policy goes always
    left = 0
    for any state

    note: independent of state
    """
    return 0

def Behavior_policy(state):
    """The behavior policy goes to
    50 % left and 50 % right

    note: independent of state"""
    random_float = np.random.random_sample()
    action = 0
    if random_float > 0.5:
        action = 1
    return action

def Environment(action):
    state = 0
    reward = 0

    # if the agent goes right, its over
    if action == 1:
        state = 1
        return reward, state

    # otherwise it can be either a win 10%
    # or loose 90 %
    else:
        if np.random.random_sample() < 0.1:
            reward = 1
            state = 1
            return reward, state

        else:
            reward = 0
            return reward, state


def Generate_Episode(policy):
    done = False
    state = 0

    episode = []

    while done == False:
        action = policy(state)

        reward, new_state = Environment(action)
        episode.append([state, action, reward])

        state = new_state

        if state == 1:
            done = True

    return episode


if __name__ == '__main__':
    print(__doc__)

    V_list = []
    q_list = []
    n_list = []


    gamma = 1 # discount factor

    for n in np.linspace(3,6,50):
        n_episodes = int(10**n)
        print(n_episodes)
        n_list.append(n_episodes)


        q_expected = 0 # expected reward
        c_cum = 0 # cummulative weight



        for i in np.arange(n_episodes):

            # initialize policy that has coverage with pi
            policy = Behavior_policy

            # generate an episode with this policy
            # State, action, reward, state, action, reward, ..., S_{T-1}, A_{T-1}, R_T
            episode = Generate_Episode(policy)

            # initialize expected return (do not confuse with reward)
            G = 0

            # initialize weights (ratio between policies)
            W = 1

            #V = W*G/W
            timesteps = len(episode)

            # iterate through episode from last step to first when W != 0
            for t in np.linspace(timesteps-1, 0, timesteps):

                if W == 0:
                    break

                # get reward and calculate return (for all T)
                state, action, reward = episode[int(t)]
                G = gamma * G + reward

                #if c_cum >0:
                #    V = V + W/c_cum *(G - V)


                # cumulated sum of weights gets new weight
                c_cum = c_cum + W

                weight_update = W/(c_cum)# * timesteps)
                q_expected = q_expected + weight_update * (G - q_expected)


                # probability of taking the state "left"
                pi = 1
                b = 0.5

                # Importance sampling ratio is pi/b
                W = W * (pi/b)



        V = W * q_expected
        V_list.append(V)
        q_list.append(q_expected)

    from matplotlib import pyplot as plt

    plt.figure()
    plt.plot(n_list, q_list)
    plt.title("Reward Q")
    plt.show()

    plt.figure()
    plt.plot(n_list, V_list)
    plt.title("Value of state")
    plt.show()
