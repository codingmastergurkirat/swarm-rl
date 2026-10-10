from app.environment.agent import Agent
from app.environment.models import Position

class GridWorld:
	def	__init__(
			self,
			row: int,
			col: int,
			obstacles: set[Position],
			agents: list[Agents]
		):
			self.row = row
			self.col = col
			self.obstacles = obstacles
			self.agents = agents
			self.initial_positions = {
			agent.id: agent.position
			for agent in self.agents
			}
	
	def 	reset(self) -> Postion:
			for agent in self.agents:
				agent.position = self.initial_positions[agent.id]
			return self._get_state()

	def 	_get_state(self):
			return tuple(
				agent.position
				for agent in self.agents
			)

	def 	step(self,actions: Action):
			proposed_positions = {}

			for agent in self.agents:
				action = actions[agent.id]

				proposed_position = self._get_next_position(
					agent.position,
					action
					)
				if not self._is_valid_position(proposed_position):
					proposed_positions[agent.id] = agent.position
				proposed_positions[agent.id] = proposed_position

			# Colliosion handling will write here later

			for agent in self.agents:
				agent.position = proposed_positions[agent.id]
			
			return self._get_state()

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

	
