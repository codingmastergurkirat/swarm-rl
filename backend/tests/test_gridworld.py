from app.environment.gridworld import (
	Action,
	Position,
	GridWorld
	)
def test_agent_moves():
	env = GridWorld(
		row = 5,
		col = 5,
		obstacles = set(),
		start = Position(0,0),
		goal = Position(4,4)
		)
	state = env.reset()

	assert state == Position(0,0)

	state,reward,done = env.step(Action.RIGHT)

	assert state == Position(0,1)
	assert reward == -1.0
	assert done is False 