from dataclasses import dataclass
from enum import Enum

class Action(Enum):
	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3

@dataclass(frozen=True)
class Position:
	row: int
	col: int