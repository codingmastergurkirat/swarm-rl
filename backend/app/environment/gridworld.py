from enum import Enum
from dataclasses import dataclass

class Action(Enum):
	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3

@dataclass(frozen=True)
class Position:
	row: int
	col: int

class GridWorld:
	def	__init__(
			self,
			row: int,
			col: int,
			obstacles: set[Position],
			start : Position,
			goal : Position
		):
			self.row = row
			self.col = col
			self.obstacles = obstacles
			self.start = start
			self.goal = goal
			self.agent_position = start
	
	def 	reset(self) -> Postion:
		self.agent_position = self.start
		return self.agent_position
	
	def 	step(self,action: Action) -> tuple[Position,float,bool]:
			current = self.agent_position
			next_position = self._get_next_position(current,action)
			if not self._is_valid_position(next_position):
				next_position = current
			self.agent_position = next_position
			if self.agent_position == self.goal:
				return self.agent_position,10.0,True
			return self.agent_position,-1.0,False

	def 	_get_next_position(self,position: Position,action: Action) -> Position:
			row = position.row
			col = position.col	
		
			if action == action.UP:
				row -= 1
			elif action == action.DOWN:
				row += 1
			elif action == action.LEFT:	
				col -= 1
			elif action == action.RIGHT:
				col += 1

			return Position(row,col)
	def 	_is_valid_position(self,position: Position) -> bool:
			row = position.row
			col = position.col
			
			if not (0 <= row < self.row):
				return False
			if not (0 <= col < self.col):
				return False
			if position in self.obstacles:
				return False
			return True

	
