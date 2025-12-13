from abc import ABC, abstractmethod
from typing import Callable
from vector import Vector2, Vector2Int


class Player(ABC):
    @property
    @abstractmethod
    def position(self) -> Vector2:
        ...

    @abstractmethod
    def set_direction(self, direction: Vector2) -> None:
        ...

    @abstractmethod
    def update(self, dt: float) -> None:
        ...


class Block(ABC):
    @property
    @abstractmethod
    def position(self) -> Vector2:
        ...

    @abstractmethod
    def update(self, dt: float) -> None:
        ...