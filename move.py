import arcade
from player import Player
from vector import Vector2


class Move:
    def keys_to_direction(keys: set[int]) -> Vector2:
        d_is_pressed = arcade.key.D in keys
        a_is_pressed = arcade.key.A in keys
        space_is_pressed = arcade.key.SPACE in keys
        x = d_is_pressed - a_is_pressed
        y = space_is_pressed
        direction = Vector2(x, y)
        return direction.normalize if direction.length > 0 else direction
    
    def player(self, player: Player) -> Vector2:
        self.keys_to_direction()