from dataclasses import dataclass
from pathlib import Path
import arcade
from block import Platform
from draw import PLAYER_SIZE
from vector import Vector2
from physics import Physics, SHAPE, BLOCK_HEIGHT

default_pattern = [
            Platform(physics=Physics(
                position=Vector2(200, BLOCK_HEIGHT // 2),
                width=400,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 200, BLOCK_HEIGHT // 2),
                width=400,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(500, 200),
                width=100,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(700, 200),
                width=100,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(2, BLOCK_HEIGHT * 2),
                width=4,
                height=PLAYER_SIZE.y + 16
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                width=2,
                height=PLAYER_SIZE.y + 16),
                color=arcade.color.CARIBBEAN_GREEN
            )
        ]


@dataclass
class Lev_Patterns:
    def get_default() -> list[Platform]:
        return default_pattern
    
    def get_default_block() -> arcade.Texture:
        texture_path = Path("data/block.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_default_door() -> arcade.Texture:
        texture_path = Path("data/door.jpg")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    
    
