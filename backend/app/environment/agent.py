from dataclasses import dataclass
from app.environment.models import Position

@dataclass
class Agent():
	id: int
	position: Position
	goal: Position

