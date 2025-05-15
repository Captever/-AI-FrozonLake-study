import gymnasium as gym
import numpy as np

class FrozenLakeEnvironment:
    def __init__(self):
        # Initialize the FrozenLake environment
        self.env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)

        # Get number of states and actions
        self.state_size = self.env.observation_space.n
        self.action_size = self.env.action_space.n

        # Initialize Q-table with zeros
        self.q_table = np.zeros((self.state_size, self.action_size))

        # Set training parameters
        self.max_steps = 100              # Max steps per episode
        self.alpha = 0.1                  # Learning rate
        self.gamma = 0.99                 # Discount factor
        self.epsilon = 1.0                # Initial exploration rate
        self.epsilon_min = 0.01           # Minimum exploration rate
        self.epsilon_decay = 0.995        # Decay rate for exploration

        # Initialize variables
        self.episode_num = 0
        self.step_num = 0
        self.state = None
        self.info = None

        # print(self.env.spec)  # Print environment specification

    def reset(self):
        self.state, self.info = self.env.reset()

    def step(self):
        if self.step_num == 0:
            self.reset()

        # Choose action using ε-greedy strategy (explore or exploit)
        on_explore = np.random.rand() <= self.epsilon
        if on_explore:  # explore
            action = self.env.action_space.sample()
        else:  # exploit
            action = np.argmax(self.q_table[self.state])

        # Execute action in the environment
        observation, reward, terminated, truncated, self.info = self.env.step(action)
        self.step_num += 1

        # Update Q-table using Q-learning update rule
        # Q(s, a) + α [r + γ * max(Q(s', a')) - Q(s, a)]
        current_q = self.q_table[self.state, action]
        max_future_q = np.max(self.q_table[observation])
        updated_q = current_q + self.alpha * (reward + self.gamma * max_future_q - current_q)
        self.q_table[self.state, action] = updated_q

        # Set current state to observation
        self.state = observation
        
        # # Print process
        # print(f"{'Explore => ' if on_explore else ''}state: {self.state}, action: {action}, epsilon: {self.epsilon:.3f}, reward: {reward}, episode_over: {terminated} | {truncated}, info: {self.info}")

        # Handle the episode is over
        episode_over = terminated or truncated or self.step_num >= self.max_steps
        if episode_over:
            self.step_num = 0
            self.episode_num += 1
            # Decay epsilon (exploration rate)
            self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_min)

    def close(self):
        self.env.close()