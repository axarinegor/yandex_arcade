import arcade
from player import Player
from vector import Vector2


class Move:
    @staticmethod
    def keys_to_direction(keys: set[int]) -> Vector2:
        a_pressed = arcade.key.A in keys
        d_pressed = arcade.key.D in keys
        x = 0
        if d_pressed and not a_pressed:
            x = 1
        elif a_pressed and not d_pressed:
            x = -1
        
        return Vector2(x, 0)
    
    @staticmethod
    def should_jump(keys: set[int]) -> bool:
        return arcade.key.SPACE in keys