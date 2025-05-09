import pygame

import gymnasium as gym
import numpy as np

# Initialize the FrozenLake environment
env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)

# Get number of states and actions
state_size = env.observation_space.n
action_size = env.action_space.n

# Initialize Q-table with zeros
q_table = np.zeros((state_size, action_size))

# Set training parameters
episodes = 1000              # Total number of training episodes
max_steps = 100              # Max steps per episode
alpha = 0.1                  # Learning rate
gamma = 0.99                 # Discount factor
epsilon = 1.0                # Initial exploration rate
epsilon_min = 0.01           # Minimum exploration rate
epsilon_decay = 0.995        # Decay rate for exploration

# print(env.spec)  # Print environment specification

# Training loop
for episode in range(episodes):
    state, info = env.reset()

    for _ in range(max_steps):
        # Choose action using ε-greedy strategy (explore or exploit)
        if np.random.rand() <= epsilon:  # explore
            print("Explore => ", end='')
            action = env.action_space.sample()
        else:  # exploit
            action = np.argmax(q_table[state])

        # Execute action in the environment
        observation, reward, terminated, truncated, info = env.step(action)

        # Update Q-table using Q-learning update rule
        # Q(s, a) + α [r + γ * max(Q(s', a')) - Q(s, a)]
        current_q = q_table[state, action]
        max_future_q = np.max(q_table[observation])
        updated_q = current_q + alpha * (reward + gamma * max_future_q - current_q)
        q_table[state, action] = updated_q

        # Set current state to observation
        state = observation
        
        episode_over = terminated or truncated

        # Print process
        print(f"state: {state}, action: {action}, epsilon: {epsilon:.3f}, reward: {reward}, episode_over: {terminated} | {truncated}, info: {info}")

        # Break the loop if the episode is over
        if episode_over:
            break

        pass  # Placeholder

    # Decay epsilon (exploration rate)
    epsilon = max(epsilon * epsilon_decay, epsilon_min)

env.close()