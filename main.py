import pygame
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim

# Step 1: Define the Grid Environment
class GridEnvironment:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.state_size = grid_size[0] * grid_size[1]  # Total number of grid cells
        self.action_size = 3  # Left, straight, right

        self.grid = np.zeros(grid_size)

    def reset(self):
        # Reset the environment to the initial state
        initial_state = np.zeros(self.grid_size)
        self.grid = initial_state
        return self.grid

    def step(self, actions):
        rewards = np.zeros(len(actions))
        done = False

        # Update the state based on the actions taken
        for i, action in enumerate(actions):
            # Implement your logic here based on the selected action
            # Update the state, calculate the reward for each agent

            # Example: Randomly move the agent to a neighboring cell
            x, y = np.where(self.grid == i + 1)
            current_pos = (x[0], y[0])
            next_pos = current_pos  # Placeholder for the next position based on the action

            if action == 0:  # Left
                next_pos = (current_pos[0], current_pos[1] - 1)
            elif action == 1:  # Straight
                next_pos = (current_pos[0] - 1, current_pos[1])
            elif action == 2:  # Right
                next_pos = (current_pos[0], current_pos[1] + 1)

            # Update the grid state
            self.grid[current_pos] = 0
            self.grid[next_pos] = i + 1

            # Calculate the reward (you can customize this based on your simulation)
            rewards[i] = np.random.randn()

            # Check if the episode is done (you can customize this based on your simulation)
            if np.random.rand() < 0.1:
                done = True

        # Return the next state, rewards, and done flag
        return self.grid, rewards, done

    def get_grid(self):
        return self.grid

# Step 3: Implement the Agent Class
class DQNAgent:
    def __init__(self, agent_id, state_size, action_size):
        self.agent_id = agent_id
        self.state_size = state_size
        self.action_size = action_size
        self.q_network = self.build_model()
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=0.001)

    def build_model(self):
        # Define the neural network architecture for the agent (DQN)
        return nn.Sequential(
            nn.Linear(self.state_size, 64),
            nn.Linear(64, self.action_size)
        )

    def select_action(self, state):
        # Select an action based on the agent's policy (e.g., epsilon-greedy)
        state_tensor = torch.tensor(state.flatten(), dtype=torch.float32)
        q_values = self.q_network(state_tensor)
        action = torch.argmax(q_values).item()
        return action

    def train(self, experiences, target_network=None, gamma=0.99):
        states, actions, rewards, next_states, dones = experiences

        # Convert the experiences to tensors
        states_tensor = torch.tensor(states, dtype=torch.float32)
        actions_tensor = torch.tensor(actions, dtype=torch.long)
        rewards_tensor = torch.tensor(rewards, dtype=torch.float32)
        next_states_tensor = torch.tensor(next_states, dtype=torch.float32)
        dones_tensor = torch.tensor(dones, dtype=torch.float32)

        if target_network is not None:
            # Compute the target Q-values using the Bellman equation with a separate target network
            target_q_values = rewards_tensor + gamma * torch.max(target_network(next_states_tensor), dim=1)[0] * (1 - dones_tensor)
        else:
            # Compute the target Q-values using the Bellman equation without a target network
            target_q_values = rewards_tensor + gamma * torch.max(self.q_network(next_states_tensor), dim=1)[0] * (1 - dones_tensor)

        # Get the predicted Q-values for the current state and selected actions
        predicted_q_values = torch.gather(self.q_network(states_tensor), dim=1, index=actions_tensor.unsqueeze(-1)).squeeze(-1)

        # Compute the loss using the Mean Squared Error (MSE) loss function
        loss = nn.MSELoss()(predicted_q_values, target_q_values.detach())

        # Perform gradient descent and update the weights
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

# Step 4: Create the Pygame Visualization
class TrafficSimulation:
    def __init__(self, grid_size, num_agents):
        self.grid_size = grid_size
        self.num_agents = num_agents

        self.environment = GridEnvironment(grid_size)

        # Create the agents
        self.agents = []
        for i in range(num_agents):
            agent = DQNAgent(i, self.environment.state_size, self.environment.action_size)
            self.agents.append(agent)

        # Set up the Pygame window
        self.cell_size = 50
        self.window_size = (self.grid_size[1] * self.cell_size, self.grid_size[0] * self.cell_size)
        pygame.init()
        self.window = pygame.display.set_mode(self.window_size)

    def reset(self):
        # Reset the environment and agents
        self.environment.reset()
        for agent in self.agents:
            agent.q_network.train()

    def step(self):
        actions = []
        for agent in self.agents:
            state = self.environment.get_grid()
            action = agent.select_action(state)
            actions.append(action)

        next_state, rewards, done = self.environment.step(actions)

        for i, agent in enumerate(self.agents):
            agent.train((state, actions[i], rewards[i], next_state, done))

    def run(self, num_episodes=10):
        self.reset()

        for episode in range(num_episodes):
            self.reset()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                self.window.fill((255, 255, 255))

                # Draw the grid cells
                grid = self.environment.get_grid()
                for i in range(self.grid_size[0]):
                    for j in range(self.grid_size[1]):
                        cell = grid[i, j]
                        if cell == 0:
                            color = (255, 255, 255)
                        else:
                            color = (0, 0, 0)
                        pygame.draw.rect(self.window, color, (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))

                pygame.display.update()

                self.step()  # Pass the actions as an argument



if __name__ == "__main__":
    grid_size = (10, 10)  # Specify the size of the grid
    num_agents = 2  # Specify the number of agents

    simulation = TrafficSimulation(grid_size, num_agents)
    simulation.run(num_episodes=10)
