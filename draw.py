from vector import Vector2Int
import arcade
from dataclasses import dataclass
import protocols as proto

PLAYER_RADIUS = 20
PLAYER_COLOR = arcade.color.SILVER_CHALICE
PLAYER_BORDER_COLOR = arcade.color.BLACK

@dataclass
class Draw:
    def player(self, player: proto.Player) -> None:
        arcade.draw_lrbt_rectangle_filled(player.position.x - PLAYER_RADIUS,
                                          player.position.x + PLAYER_RADIUS,
                                          player.position.y - PLAYER_RADIUS,
                                          player.position.y + PLAYER_RADIUS,
                                          PLAYER_COLOR)
        arcade.draw_lrbt_rectangle_outline(player.position.x - PLAYER_RADIUS,
                                          player.position.x + PLAYER_RADIUS,
                                          player.position.y - PLAYER_RADIUS,
                                          player.position.y + PLAYER_RADIUS,
                                          PLAYER_BORDER_COLOR,
                                          3)
        #arcade.draw_rectangle_filled(*player.position.tuple, PLAYER_RADIUS, PLAYER_COLOR)
        #arcade.draw_circle_outline(*player.position.tuple, PLAYER_RADIUS, PLAYER_BORDER_COLOR, 3)