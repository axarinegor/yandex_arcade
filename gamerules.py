from vector import Vector2
from player import Player
import arcade

class GameRules:
    @staticmethod
    def check_level_completion(player: Player, exit_position: Vector2, exit_radius: float = 10.0) -> bool:
        distance = (player.position - exit_position).length
        return distance < exit_radius
    
    @staticmethod
    def exit_game() -> None:
        arcade.close_window()
    
    '''@staticmethod
    def restart_level(player: Player, spawn_position: Vector2) -> None:
        player.physics.position = spawn_position
        player.physics.velocity = Vector2.zero()'''
