import pyglet
from physics import BLOCK_HEIGHT
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

    def door(self, door: proto.Door, texture) -> None:
        if door.width > 10:
            arcade.draw_texture_rect(
                    texture=texture,
                    rect=arcade.rect.LBWH(left=door.position.x - door.width // 2, 
                                        bottom=door.position.y - door.height // 2, 
                                        width=door.width, 
                                        height=door.height)
                )
        else:    
            arcade.draw_lbwh_rectangle_filled(
                left=door.position.x - door.width // 2,
                bottom=door.position.y - door.height // 2,
                width=door.width,
                height=door.height,
                color=door.color
            )

    def texture_wall(self, platform: proto.Platform, texture: arcade.Texture) -> None:
        tiles_y_count = int(platform.height / BLOCK_HEIGHT)
        tiles_x_count = int(platform.width / BLOCK_HEIGHT)
        
        start_x = platform.position.x - platform.width / 2 + BLOCK_HEIGHT / 2
        start_y = platform.position.y - platform.height / 2 + BLOCK_HEIGHT / 2
    
        for j in range(tiles_x_count):
            for i in range(tiles_y_count):
                pos_x = start_x + j * BLOCK_HEIGHT
                pos_y = start_y + i * BLOCK_HEIGHT
                arcade.draw_texture_rect(
                    texture=texture,
                    rect=arcade.rect.XYWH(x=pos_x, 
                                        y=pos_y, 
                                        width=BLOCK_HEIGHT, 
                                        height=BLOCK_HEIGHT)
                )
    def texts(self, texts: list[arcade.Text]) -> None:
        for text in texts:
            text.draw()



            

