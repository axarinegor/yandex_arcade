from abc import ABC, abstractmethod
from typing import Callable
from vector import Vector2, Vector2Int


class Player(ABC):
    @property
    @abstractmethod
    def position(self) -> Vector2:
        return self.physics.position
    
    @abstractmethod
    def set_direction(self, direction: Vector2) -> None:
        ...
    
    @abstractmethod
    def jump(self) -> None:
        ...
    
    @abstractmethod
    def update(self, dt: float, platforms: list = None) -> None:
        ...


class Platform(ABC):
    @abstractmethod
    def __post_init__(self):
        ...
    
    @property
    @abstractmethod
    def position(self) -> Vector2:
        ...
    
    @property
    @abstractmethod
    def width(self) -> float:
        ...
    
    @property
    @abstractmethod
    def height(self) -> float:
        ...
    
    @abstractmethod
    def update(self, dt: float) -> None:
        ...
