# Reinforcement-Learning
Excercises and Projects from the book "Reinforcement Learning - An Introduction" and the EPFL Lecture

### Action-Value Methods
- k armed bandid with dynamic updating rewards
- $\epsilon$-greedy policy with 
  - average approximation of expected reward (should fail for $n \rightarrow \infty$)
    - $Q_{n+1} = Q_n + \frac{1}{n} [R_n - Q_n]$
  - constant approximation of expected reward (should resist high n)
    - $Q_{n+1} = Q_n + \alpha [R_n - Q_n]$


### off_policy_MC_Importance_Sampling
- an example, how off_policy MC can be misleaded by using ordinary importance sampling
  - $V(s) = \frac{\sum_{t \in \tau(s)} \rho_{t:T(t)-1} G_t}}{|\tau(s)|}$

### Windy_Grid_World
- Implementation of SARSA, Q-learning and expected SARSA to find the fastest path in a grid world
- possible moves are up, down, left, right, diagonal
- extra trouble comes from a wind that is applied 
  - constantly
  - randomly

- at the moment, the grid world will not be left, because the border is unattractive (Q = -100)
- make this better in future (check if I leave the grid with an action and prevent to do this action)

- at the moment the windy grid world is not windy yet, but it works


### Author
Eric Schmidt

