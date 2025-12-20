from abc import abstractmethod
from dataclasses import dataclass
from physics import Physics
import protocols as proto
import arcade
from vector import Vector2, Vector2Int

BLOCK_COLOR = arcade.color.SKOBELOFF

@dataclass
class Platform(proto.Platform):
    physics: Physics
    color: tuple = BLOCK_COLOR
    
    def __post_init__(self):
        self.physics.is_active = False
    
    @property
    def position(self) -> Vector2:
        return self.physics.position
    
    @property
    def width(self) -> float:
        return self.physics.width
    
    @property
    def height(self) -> float:
        return self.physics.height
    
    def update(self, dt: float) -> None:
        if self.physics.is_active:
            self.physics.update(dt)
    

