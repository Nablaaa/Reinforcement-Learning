import numpy as np


class Agent:
    def __init__(self):
        pass

    def PossibleActions(self,selection):
        actions = {0: (-1,1), 1: (0,1), 2:(1,1),
                   3: (-1,0), 4: (0,0), 5:(1,0),
                   6: (-1,-1), 7: (0,-1), 8:(1,-1)}
        return actions[selection]

    def SARSA(self, state, Q, epsilon = 0.1):
        xpos = state[0]
        ypos = state[1]
        # 3x3 matrix
        decision_region = Q[xpos - 1: xpos + 2, ypos - 1: ypos + 2] # slicing is exluding

        # select the maximum Q value in the region around the state
        # select the maximum in 1-epsilon cases
        random_choice = np.random.random_sample()

        if random_choice < epsilon:
            selection = np.random.randint(0,9)
        else:
            selection = np.argmax(decision_region)

        action = self.PossibleActions(selection)

        return action



if __name__ == "__main__":
    Q = np.random.uniform(0,9,size=(5,5))
    policy = Agent()

    state = [1,1]
    action = policy.SARSA(state,Q)
    print(action)