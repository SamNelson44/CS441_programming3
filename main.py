#Sam Nelson, CS441, programming #3, Tic Tac Toe

def q_learning(Q, state, action, reward, next_state, alpha, gamma):
    current_q = Q[state][action]
    max_next_q = max(Q[next_state])
    print(max_next_q)
    new_q = current_q + alpha * (reward + gamma * max_next_q - current_q)
    Q[state][action] = new_q
    return Q

def main():
        # Initialize Q-values
    Q = {
        'state1': {'action1': 0, 'action2': 0},
        'state2': {'action1': 0, 'action2': 0}
    }
    # Example parameters
    state = 'state1'
    action = 'action1'
    reward = 1
    next_state = 'state2'
    alpha = 0.1
    gamma = 0.9

    # Update Q-value
    q_learning(Q, state, action, reward, next_state, alpha, gamma)
    print(Q)
    return

if __name__ == "__main__":
    main()