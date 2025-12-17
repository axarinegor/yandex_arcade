from dataclasses import dataclass

import arcade


from vector import Vector2, Vector2Int
from physics import SHAPE, Physics, BLOCK_HEIGHT


class Door(): 
    '''is_open: bool = False
    physics: Physics
    color: arcade.color = arcade.color.BLACK_OLIVE
    '''
    def position(self) -> Vector2:
        return self.physics.position 
    
    @property
    def width(self) -> float:
        return self.physics.width
    
    @property
    def height(self) -> float:
        return self.physics.height
    
    def update(self, dt: float) -> None:
        '''if self.is_open == True:
            self.physics = Physics(SHAPE.x - BLOCK_HEIGHT // 2, 100, BLOCK_HEIGHT, 100)'''
        ...