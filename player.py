from abc import ABC
from vector import Vector2, Vector2Int
from dataclasses import dataclass, field
import protocols as proto

@dataclass
class Player(proto.Player):
    _position: Vector2
    _speed: float
    _direction: Vector2 = field(init=False, default=Vector2.zero())

    @property
    def position(self) -> Vector2:
        return self._position

    def set_direction(self, direction: Vector2) -> None:
        assert direction.length <= 1
        self._direction = direction

    def update(self, dt: float) -> None:
        velocity = self._direction * self._speed
        self._position += velocity * dt