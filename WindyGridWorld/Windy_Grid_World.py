import numpy as np
import matplotlib.pyplot as plt
from GridWorld import GridWorld
from Agent import Agent

if __name__ == '__main__':

    alpha = 0.5
    gamma = 0.5
    rows = 15
    cols = 25

    grid = GridWorld(rows,cols)
    grid.MakeGrid()


    start = [8,5]  # row, col
    end = [9,20] # row, col
    grid.DefineStartEnd(start,end)
    #grid.AddWind(wind = "const")

    # initialize Q randomly, Q(end) = 0
    Q_map = GridWorld(rows+3,cols+3)
    Q_map.DefineStartEnd(start,end)
    Q_map.MakeGrid() #set every position to 0
    # Q_map.MakeRandomGrid(terminus="zero") # set end to zero
    Q_map.Unattractive_Border()


    # define Reward (everywhere -1)
    rewards = -1 * np.ones((rows+3,cols+3),dtype='float16')

    policy = Agent()


    episodes = 10000
    number_steps = []
    for i in range(episodes):

        if np.mod(i,200):
            print(i)

        state = start

        walk = np.zeros((rows+3,cols+3))

        steps = 0
        while state != end:

            epsilon = 0.1

            if i > 1000:
                epsilon = 0.01
                alpha = 0.9

            elif i> 5000:
                epsilon = 0.001
                alpha = 1

            Q_map.Unattractive_Border() # make the borders again unattractive
        #######################################################
        # First Run to get S, A, R
        #######################################################
            action1 = policy.SARSA(state, Q_map.GetGrid(),epsilon=epsilon)

            # this looks a bit wild, but it is just
            # because y and x coordinates from numpy
            # do not fit with (x, y) of tuples
            new_state1 = [state[0] - action1[1],
                         state[1] + action1[0]]

            walk[new_state1[0],new_state1[1]] = steps

            reward = rewards[new_state1[0], new_state1[1]]

            #######################################################
            # Second Run to get S', A'
            #######################################################
            action2 = policy.SARSA(new_state1, Q_map.GetGrid(),epsilon=epsilon)
            new_state2 = [new_state1[0] - action2[1],
                         new_state1[1] + action2[0]]


            # update the position after step 1, based on
            # the information of step 2 and step 1
            position = new_state1
            q_values = Q_map.GetGrid()
            old_Q = q_values[new_state1[0], new_state1[1]]
            new_Q = q_values[new_state2[0], new_state2[1]]


            if new_state1 == end:
                reward = 5
            Q_update = old_Q + alpha * (reward +
                                        gamma * new_Q -
                                        old_Q)


            Q_map.UpdateGrid(position,Q_update)

            state = new_state1


            # save the Q_map and start again
            np.save("Qmap.npy", Q_map.GetGrid())
            steps += 1

        number_steps.append(steps)


        if np.mod(i,200)==0:

            plt.figure()
            plt.imshow(walk)
            plt.axis('off')
            plt.savefig("Walk_Images/" + str(i).zfill(3) + ".png")
            plt.close()


            plt.figure()
            plt.imshow(Q_map.GetGrid(),vmin=-1, vmax=1)
            plt.axis('off')
            plt.savefig("Q_Images/" + str(i).zfill(3) + ".png")
            plt.close()


    plt.figure()
    plt.plot(np.arange(len(number_steps)),number_steps)
    plt.savefig("Necessary_Steps.png")
    plt.xlabel("Episode")
    plt.ylabel("Steps to reach the goal")
    plt.show()
    # final_grid = grid.GetGrid()
    # final_grid[grid.start[0], grid.start[1]] = 5
    # final_grid[grid.end[0],grid.end[1]] = 2*5
    #
    # plt.figure()
    # plt.imshow(final_grid)
    # plt.show()