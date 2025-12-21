'''from dataclasses import dataclass
from vector import Vector2
import arcade
from pathlib import Path
from physics import BLOCK_HEIGHT
from draw import Draw

class TileSystem:
    _block_texture = None

    @classmethod
    def get_block_texture(cls, size: float = BLOCK_HEIGHT) -> arcade.Texture:
        texture_path = Path("data/block.png")
        if texture_path.exists():
            cls._block_texture = arcade.load_texture(texture_path)
        else:
            cls._block_texture = arcade.make_soft_square_texture(
                size, (120, 120, 120), outer_alpha=255
            )

        return cls._block_texture
    
    @staticmethod
    def draw_tiled_wall(
        center_x: float,
        center_y: float,
        width: float,
        height: float,
        texture: arcade.Texture = None
    ) -> None:
        tile_size = BLOCK_HEIGHT
        tiles_y_count = int(height / tile_size)
        tiles_x_count = int(width / tile_size)
        
        start_x = center_x - width / 2 + tile_size / 2
        start_y = center_y - height / 2 + tile_size / 2
    
        for j in range(tiles_x_count):
            for i in range(tiles_y_count):
                pos_x = start_x + j * tile_size
                pos_y = start_y + i * tile_size
                arcade.draw_texture_rect(
                    pos_x, pos_y,
                    tile_size, tile_size,
                    texture
                )
            '''