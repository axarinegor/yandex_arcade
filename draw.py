from vector import Vector2Int
import arcade
from dataclasses import dataclass
import protocols as proto


PLAYER_SIZE = Vector2Int(35, 80)
PLAYER_COLOR = arcade.color.SILVER_CHALICE
PLAYER_BORDER_COLOR = arcade.color.BLACK

@dataclass
class Draw:
    def player(self, player: proto.Player) -> None:
        arcade.draw_lrbt_rectangle_filled(player.position.x - PLAYER_SIZE.x // 2,
                                          player.position.x + PLAYER_SIZE.x // 2,
                                          player.position.y - PLAYER_SIZE.y // 2,
                                          player.position.y + PLAYER_SIZE.y // 2,
                                          PLAYER_COLOR)
        arcade.draw_lrbt_rectangle_outline(player.position.x - PLAYER_SIZE.x // 2,
                                          player.position.x + PLAYER_SIZE.x // 2,
                                          player.position.y - PLAYER_SIZE.y // 2,
                                          player.position.y + PLAYER_SIZE.y // 2,
                                          PLAYER_BORDER_COLOR,
                                          3)
        
    def platform(self, platform: proto.Platform) -> None:
        arcade.draw_lbwh_rectangle_filled(
            left=platform.position.x - platform.width // 2,
            bottom=platform.position.y - platform.height // 2,
            width=platform.width,
            height=platform.height,
            color=platform.color
        )
