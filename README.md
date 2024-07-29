# Blackjack with Q-Learning

![Blackjack](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.crownperth.com.au%2Fcasino%2Ftable-games%2Fblackjack&psig=AOvVaw0LxiEB222d-EFcv3By4jiM&ust=1722358201248000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPjZ-rvazIcDFQAAAAAdAAAAABAx)

## Introduction
Welcome to the [blackjack-qlearning](cci:4://c:/Users/Carlos/dev/Repos/blackjack-qlearning/README.md:0:0-2:0) project! This repository contains an implementation of a Blackjack game using Q-learning, a type of reinforcement learning. The goal is to train an agent to play Blackjack optimally.

## Features
- **Q-learning Agent**: Learn and adapt strategies to maximize rewards.
- **Customizable Parameters**: Adjust learning rate, discount factor, epsilon-greedy strategy, and training epochs.
- **Simulation and Benchmarking**: Run simulations and benchmark the agent's performance.
- **Visualization**: Visualize the agent's learning progress and policy.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/blackjack-qlearning.git
   ```

2. Navigate into the project directiory
    ```sh
    cd blackjack-qlearning
    ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Open the Notebook:
    ```sh
    jupyter notebook blackjack_qlearning.ipynb
    ```

2. Run the cells to train the agent and visualize the results

## Configuration
You can adjust the training parameters in the *Agent* class in `blackjack_qlearning.ipynb`:
    ```python
    agent = Agent(
        learning_rate=0.1,
        discount_factor=0.9,
        epsilon_greedy
    )
    ```

## Project Structure

The project structure is organized as follows:

- `blackjack`: Folder containing the implementation of the Blackjack game and its components.
  - `card.py`: Class representing a card in the game.
  - `deck.py`: Class representing a deck of cards.
  - `hand.py`: Class representing a hand of cards.
  - `player.py`: Class representing a player in the game.
  - `simulation.py`: Functions for running simulations of the game.
- `blackjack_qlearning.ipynb`: Jupyter Notebook for training the Q-learning agent and visualizing the results.
- `LICENSE`: MIT license file.
- `README.md`: This file.
- `requirements.txt`: List of required Python packages.



