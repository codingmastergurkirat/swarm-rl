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

	def 	step(self,actions: dict[int,Action],) -> tuple[tuple[Position, ...],set[tuple[int,int]]]:
			current_positions = {
				agent.id: agent.position
				for agent in self.agents
			}
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
			final_positions,collisions = self._resolve_collisions(
				current_positions,
				proposed_positions
				)

			for agent in self.agents:
				agent.position = final_positions[agent.id]
			
			return self._get_state(), collisions

	def     _resolve_collisions(
			self,
			current_positions : dict[int,Position],
			proposed_positions : dict[int,Position]
		) -> tuple[dict[int,Position],set[tuple[int,int]]]:

			final_positions = proposed_positions.copy()
			collisions = set()

			while True:

				collision_agents = set()
				new_collisions = set()

				agent_ids = list(current_positions.keys())

				for i in range(len(agent_ids)):
					for j in range(i+1,len(agent_ids)):

						agent_a = agent_ids[i]
						agent_b = agent_ids[j]

						current_a = current_positions[agent_a]
						current_b = current_positions[agent_b]

						final_a = proposed_positions[agent_a]
						final_b = proposed_positions[agent_b]

						same_destination = final_a == final_b

						# if both want to swap positions 

						swapping_positions = (final_a == current_b and final_b == current_a and current_a != current_b)

						if same_destination or swapping_positions:
							collision_agents.add(agent_a)
							collision_agents.add(agent_b)

							new_collisions.add((min(agent_a, agent_b), max(agent_a, agent_b)))

				if not collision_agents:
					break

				collisions.update(new_collisions)

				for agent_id in collision_agents:
					final_positions[agent_id] = current_positions[agent_id]

			return final_positions, collisions



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

	
