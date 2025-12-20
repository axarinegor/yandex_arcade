from vector import Vector2Int
import arcade
from dataclasses import dataclass
import protocols as proto


PLAYER_SIZE = Vector2Int(40, 68)
PLAYER_COLOR = arcade.color.SILVER_CHALICE
PLAYER_BORDER_COLOR = arcade.color.BLACK

@dataclass
class Draw:
    def player(self, player: dict) -> None:
        if not player.facing_right:
            arcade.draw_texture_rect(
                texture=player.texture, 
                rect=arcade.rect.XYWH(x=player.position.x, 
                                      y=player.position.y, 
                                      width=-player.width, 
                                      height=player.height))
        else:
            arcade.draw_texture_rect(
                texture=player.texture, 
                rect=arcade.rect.XYWH(x=player.position.x, 
                                      y=player.position.y, 
                                      width=player.width, 
                                      height=player.height))

    def platform(self, platform: proto.Platform) -> None:
        arcade.draw_lbwh_rectangle_filled(
            left=platform.position.x - platform.width // 2,
            bottom=platform.position.y - platform.height // 2,
            width=platform.width,
            height=platform.height,
            color=platform.color
        )

    def door(self, door: proto.Door) -> None:
        arcade.draw_lbwh_rectangle_filled(
            left=door.position.x - door.width // 2,
            bottom=door.position.y - door.height // 2,
            width=door.width,
            height=door.height,
            color=door.color
        )

