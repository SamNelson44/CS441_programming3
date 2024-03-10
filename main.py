#Sam Nelson, CS441, programming #3, Tic Tac Toe

import numpy as np

def q_learning(Q, state, action, reward, next_state, alpha, gamma):
    current_q = Q[state][action]
    max_next_q = max(Q[next_state])
    print(max_next_q)
    new_q = current_q + alpha * (reward + gamma * max_next_q - current_q)
    Q[state][action] = new_q
    return Q

def main():


    #initialize q-matrix

    state_size = 3**9
    action_size = 9
    Q_table = np.zeros((state_size, action_size))

    # Example parameters
    state = 'state1'
    action = 'action1'
    reward = 1
    next_state = 'state2'
    alpha = 0.1
    gamma = 0.9

    # Update Q-value
    q_learning(Q_table, state, action, reward, next_state, alpha, gamma)
    print(state_size)
    return

if __name__ == "__main__":
    main()