from dataclasses import dataclass

import arcade


from vector import Vector2, Vector2Int
from physics import SHAPE, Physics, BLOCK_HEIGHT

@dataclass
class Door(): 
    physics: Physics
    is_open: bool = False
    color: arcade.color = (98, 181, 65)
    
    @property
    def position(self) -> Vector2:
        return self.physics.position 
    
    def set_position(self, position: Vector2) -> None:
        self.physics.position = position
    
    @property
    def width(self) -> float:
        return self.physics.width
    
    def set_width(self, width: Vector2) -> None:
        self.physics.width = width
    
    @property
    def height(self) -> float:
        return self.physics.height
    
    def update(self, dt: float) -> None:
        if self.is_open == True:
            self.physics = Physics(SHAPE.x - BLOCK_HEIGHT // 2, 100, BLOCK_HEIGHT, 100)
    
    def set_open(self, value: bool) -> None:
        self.is_open = value

    @property
    def get_open(self) -> bool:
        return self.is_open