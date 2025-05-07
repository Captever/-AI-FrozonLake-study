import gym
import numpy as np

# Initialize the FrozenLake environment
env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)

# Get number of states and actions
state_size = env.observation_space.n
action_size = env.action_space.n

# Initialize Q-table with zeros
q_table = np.zeros((state_size, action_size))

# Set training parameters
episodes = 1000          # Total number of training episodes
max_steps = 100          # Max steps per episode
alpha = 0.1              # Learning rate
gamma = 0.99             # Discount factor
epsilon = 1.0            # Initial exploration rate
epsilon_min = 0.01       # Minimum exploration rate
epsilon_decay = 0.995    # Decay rate for exploration

# print(env.spec)  # Print environment specification

# Training loop
for episode in range(episodes):
    state = env.reset()
    done = False

    for _ in range(max_steps):
        # TODO: Choose action using ε-greedy strategy (explore or exploit)

        # TODO: Execute action in the environment
        # next_state, reward, done, info = env.step(action)

        # TODO: Update Q-table using Q-learning update rule

        # TODO: Set current state to next_state

        # TODO: Break the loop if the episode is done

        pass  # Placeholder

    # TODO: Decay epsilon (exploration rate)

env.close()