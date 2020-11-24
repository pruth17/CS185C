import hmm
import numpy as np
from preprocess import data_gathering


class hmmAlphaBeta:
    def alpha_pass(self, observation, a, b, pi):

        T = len(observation)
        N = len(a)
       

        alpha = [[0] * T] * N

        for i in range(N):
            alpha[i][0] = pi[i] * b[i][0]

        for t in range(0, T - 1):
            for i in range(0, N):
                for j in range(0, N):
                    alpha[i][t] += (alpha[j][t - 1] * a[j][i])

                alpha[i][t] *= b[i][t]
        return alpha

    def beta_pass(self, o, a, b, pi):
        number_of_states = len(a)

        t = len(o)

        beta = np.zeros((number_of_states, t))
        
        for row in range(number_of_states):
            beta[row][t - 1] = 1

        for new_t in range(t - 2, 0, -1):
            for row in range(number_of_states):
                for column in range(number_of_states):
                    beta[row][new_t] += (a[row][column] *
                      beta[column][new_t + 1] * b[column][o[new_t + 1]])
        return beta


def main():
    # Transition Matrix
    a = hmm.A

    # Observation Matrix
    b = hmm.B
    
    # Initial State Distribution
    pi = hmm.pi


    # Observation Sequence
    observation = ['A', 'B', '3', '2', 'T', 'R', '8', '4', 'J', 'W', '1', '5',
                   'X']

    model = hmmAlphaBeta()

    print(model.alphaPass(observation, a, b, pi))
    print(model.betaPass(observation, a, b, pi))

data_gathering