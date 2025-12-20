from dataclasses import dataclass
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
                height=BLOCK_HEIGHT // 2
            )),
            Platform(physics=Physics(
                position=Vector2(700, 200),
                width=100,
                height=BLOCK_HEIGHT // 2
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
                height=BLOCK_HEIGHT * 2
            ))
        ]


@dataclass
class Lev_Patterns:
    def get_default() -> list[Platform]:
        return default_pattern
    
    
    
