import gymnasium as gym
import numpy as np

class FrozenLakeEnvironment:
    def __init__(self, map_size, is_slippery):
        # Initialize the FrozenLake environment
        map_name = f"{map_size}x{map_size}"
        self.env = gym.make("FrozenLake-v1", map_name=map_name, is_slippery=is_slippery)

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

    def random_argmax(self, state):
        q_values = self.q_table[state]
        max_value = max(q_values)
        max_indices = np.flatnonzero(q_values == max_value)
        return np.random.choice(max_indices)

    def select_action(self):
        # Choose action using ε-greedy strategy (explore or exploit)
        on_explore = np.random.rand() <= self.epsilon
        if on_explore:  # explore
            action = self.env.action_space.sample()
        else:  # exploit
            action = self.random_argmax(self.state)
        
        print(f"{'Explore -> ' if on_explore else ''}Action: {action}")

        return action

    def step(self, action):
        if self.step_num == 0:
            self.reset()

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
        
        # Print process
        print(f"Step{self.step_num} | state: {self.state}, epsilon: {self.epsilon:.3f}, reward: {reward}, episode_over: {terminated} | {truncated}, info: {self.info}")

        # Handle the episode is over
        episode_over = terminated or truncated or self.step_num >= self.max_steps
        if episode_over:
            self.step_num = 0
            self.episode_num += 1
            # Decay epsilon (exploration rate)
            self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_min)
        
        return self.state, terminated, truncated

    def close(self):
        self.env.close()