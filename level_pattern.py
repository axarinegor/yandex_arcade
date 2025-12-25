from dataclasses import dataclass
from pathlib import Path
import arcade
from block import Platform
from draw import PLAYER_SIZE
from vector import Vector2
from physics import Physics, SHAPE, BLOCK_HEIGHT

default_pattern_1 = [
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
    def get_default(x: int = 1) -> list[Platform]:
        patterns = {
            1: default_pattern_1,
            2: default_pattern_2,
            4: default_pattern_4,
            6: default_pattern_6,
            12: default_pattern_12,
            7: default_pattern_7
        }
        
        return patterns.get(x, default_pattern_1)
    
    def get_default_block() -> arcade.Texture:
        texture_path = Path("data/block.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_default_door() -> arcade.Texture:
        texture_path = Path("data/door.jpg")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    

default_pattern_2 = [
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
                position=Vector2(800, -100),
                width=500,
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


default_pattern_4 = [
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
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
            ),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2 - 25, 300),
                width=450,
                height=BLOCK_HEIGHT)
            ),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2 - 340, 150),
                width=BLOCK_HEIGHT,
                height=BLOCK_HEIGHT)
            ),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2 + 340, 150),
                width=BLOCK_HEIGHT,
                height=BLOCK_HEIGHT)
            ),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2 - 225, 150),
                width=BLOCK_HEIGHT,
                height=300)
            ),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2 + 175, 150),
                width=BLOCK_HEIGHT,
                height=300)
            )
        ]


default_pattern_6 = [
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
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

default_pattern_12 = [
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
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
                color=arcade.color.CARIBBEAN_GREEN)
        ]


default_pattern_7 = [
            Platform(physics=Physics(
                position=Vector2(100, BLOCK_HEIGHT // 2),
                width=200,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 100, BLOCK_HEIGHT // 2),
                width=200,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(300, 200),
                width=100,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(900, 200),
                width=100,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
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
            ),
            Platform(physics=Physics(
                position=Vector2(150, 370),
                width=100,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(1050, 370),
                width=100,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(400, 465),
                width=100,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 200 + BLOCK_HEIGHT // 2, 175),
                width=BLOCK_HEIGHT,
                height=350
            ))
        ]