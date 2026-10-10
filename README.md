# Swarm RL Simulator

A multi-agent reinforcement learning simulator built from scratch using **Python and Next.js** (If I will use any new technologies later in future then I will update Readme accordingly).

The project focuses on training multiple independent agents to navigate a custom gridworld, find their goals, avoid collisions, and learn efficient paths using **Independent Q-Learning**.

---

## Project Goals

- Build a custom discrete gridworld environment
- Simulate 3–5 independent agents
- Implement Independent Q-Learning from scratch
- Experiment with reward shaping
- Minimize agent collisions
- Measure path efficiency and convergence
- Visualize training progress
- Build an interactive web interface using Next.js
- Expose the Python simulation through an API

---

## Tech Stack

### Backend

- Python
- NumPy
- Pytest
- FastAPI
- Uvicorn

### Frontend

- Next.js
- React
- TypeScript

### Reinforcement Learning

- Independent Q-Learning
- Epsilon-greedy exploration
- Reward shaping
- Q-tables
- Multi-agent coordination

---

## Project Structure

```text
swarm-rl/
│
├── backend/
│   ├── app/
│   │   ├── environment/
│   │   │   ├── gridworld.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── rl/
│   │   ├── simulation/
│   │   ├── api/
│   │   └── __init__.py
│   │
│   ├── tests/
│   │   └── test_gridworld.py
│   │
│   ├── pytest.ini
│   └── requirements.txt
│
├── frontend/
│
└── README.md
```

---

# Backend Setup

## 1. Clone the repository

```bash
git clone <repository-url>
cd swarm-rl
```

## 2. Move into the backend

```bash
cd backend
```

## 3. Create a Python virtual environment

Linux/macOS:

```bash
python3 -m venv venv
```

Windows:

```powershell
python -m venv venv
```

## 4. Activate the virtual environment

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

The backend uses **pytest** for unit testing.


```bash
pytest
```

The project contains a `pytest.ini` configuration file so Python can correctly find the `app` package.

You should see output similar to:

```text
============================= test session starts =============================
collected 1 item

tests/test_gridworld.py .                                               [100%]

============================== 1 passed =======================================
```

---

The agent currently supports four actions:

```text
UP
DOWN
LEFT
RIGHT
```

---

# Reinforcement Learning Roadmap

The project will be developed incrementally.

## Milestone 1 — Gridworld

- [x] Create project structure
- [x] Create `Position`
- [x] Create `Action`
- [x] Create basic `GridWorld`
- [x] Implement movement
- [x] Implement obstacles
- [x] Implement goal detection
- [x] Add unit tests

## Milestone 2 — Multi-Agent Environment

- [x] Create `Agent`
- [x] Support 3–5 agents
- [x] Add individual goals
- [x] Implement simultaneous actions
- [x] Detect agent collisions
- [x] Handle invalid movements
- [x] Add multi-agent tests

## Milestone 3 — Reward System

- [ ] Movement penalty
- [ ] Goal reward
- [ ] Collision penalty
- [ ] Distance-based reward shaping
- [ ] Configurable reward parameters
- [ ] Compare different reward strategies

## Milestone 4 — Independent Q-Learning

- [ ] Implement Q-table
- [ ] Implement epsilon-greedy policy
- [ ] Implement Q-learning update
- [ ] Implement training episodes
- [ ] Add exploration decay
- [ ] Train multiple independent agents

## Milestone 5 — Training Experiments

- [ ] Train for 5,000+ episodes
- [ ] Track episode rewards
- [ ] Track success rate
- [ ] Track collision rate
- [ ] Track path length
- [ ] Analyze convergence
- [ ] Compare reward configurations

## Milestone 6 — Python API

- [ ] Create FastAPI application
- [ ] Add simulation endpoints
- [ ] Add training endpoints
- [ ] Add experiment configuration
- [ ] Add simulation state endpoint
- [ ] Add WebSocket support for live training

## Milestone 7 — Next.js Frontend

- [ ] Create Next.js application
- [ ] Build grid visualization
- [ ] Display agents
- [ ] Display goals
- [ ] Display obstacles
- [ ] Add training controls
- [ ] Add reward charts
- [ ] Add collision statistics
- [ ] Add convergence visualization

## Milestone 8 — Production-Quality Project

- [ ] Improve test coverage
- [ ] Add configuration management
- [ ] Add reproducible experiments
- [ ] Add Docker support
- [ ] Improve performance
- [ ] Document architecture
- [ ] Document experiments
- [ ] Add final project demo

---

# Learning Objectives

### Python

- Object-oriented programming
- Dataclasses
- Enums
- Type hints
- NumPy
- Package structure
- Unit testing
- API development
- Async programming

### Reinforcement Learning

- Markov decision processes
- State representation
- Action spaces
- Reward functions
- Q-learning
- Bellman equations
- Exploration vs exploitation
- Multi-agent reinforcement learning
- Reward shaping
- Convergence analysis

### Next.js

- React
- TypeScript
- Next.js App Router
- Component architecture
- API integration
- WebSockets
- Data visualization
- Client-side state management

---

The project is actively being developed milestone by milestone.
