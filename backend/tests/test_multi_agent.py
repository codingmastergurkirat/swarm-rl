from app.environment.models import (
    Action,
    Position,
)
from app.environment.gridworld import GridWorld
from app.environment.agent import Agent


def test_multiple_agents_can_move():
    agents = [
        Agent(
            id=0,
            position=Position(0, 0),
            goal=Position(4, 4),
        ),
        Agent(
            id=1,
            position=Position(4, 4),
            goal=Position(0, 0),
        ),
    ]

    env = GridWorld(
        row=5,
        col=5,
        obstacles=set(),
        agents=agents,
    )

    state = env.reset()

    assert state == (
        Position(0, 0),
        Position(4, 4),
    )

    state = env.step({
        0: Action.RIGHT,
        1: Action.LEFT,
    })

    assert state == (
        Position(0, 1),
        Position(4, 3),
    )