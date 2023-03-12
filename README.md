# Reinforcement-Learning
Excercises and Projects from the book "Reinforcement Learning - An Introduction" and the EPFL Lecture

### Action-Value Methods
- k armed bandid with dynamic updating rewards
- $\epsilon$-greedy policy with 
  - average approximation of expected reward (should fail for $n \rightarrow \infty$)
    - $Q_{n+1} = Q_n + \frac{1}{n} [R_n - Q_n]$
  - constant approximation of expected reward (should resist high n)
    - $Q_{n+1} = Q_n + \alpha [R_n - Q_n]$

### Author
Eric Schmidt

