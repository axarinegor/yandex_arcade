#import arcade
from move import Move
from physics import Physics, SHAPE, SPAWN_POSITION
from sprite import Sprite
from vector import Vector2, Vector2Int
from dataclasses import dataclass, field
import protocols as proto
from animation import Animation


@dataclass
class Player(proto.Player):
    physics: Physics = field(default_factory=Physics)
    _speed: float = 150.0
    _walk_animation: Animation = field(default=None, init=False)
    facing_right: bool = field(default=True, init=False)
    _is_moving: bool = field(default=False, init=False)
    _is_jumping: bool = field(default=False, init=False)
    
    def __post_init__(self):
        self._walk_animation = Animation.load(frames_count=4, period=0.4)
        self._stay_sprite = Sprite.load_raw_image("stay.png", Vector2Int.zero())
        self._jump_sprites = Sprite.load_raw_image("jump.png", Vector2Int.zero())

    def set_direction(self, direction: Vector2) -> None:
        assert direction.length <= 1
        self.physics.move(direction, self._speed)
        self._is_moving = direction.x != 0
        if direction.x > 0:
            self.facing_right = True
        elif direction.x < 0:
            self.facing_right = False
        
    def update(self, dt: float, platforms: list = None) -> None:
        self.physics.update(dt)
        if platforms:
            Move.player_update(platforms, self.physics)
        if self._is_jumping:
            if self.physics.on_ground:
                self._is_jumping = False
        self._walk_animation.update(dt) if not self._is_jumping and self._is_moving else self._walk_animation.reset() 
    
    def texture(self):
        if self._is_jumping:
            return self._jump_sprites.get()
        return self._stay_sprite.get() if not self._is_moving else self._walk_animation.current_frame.get()
    
    @property
    def position(self) -> Vector2:
        return self.physics.position
    
    def jump(self) -> None:
        if self.physics.on_ground:
            self._is_jumping = True
            self._is_moving = False
            self.physics.jump()
    
    @property
    def position(self) -> Vector2:
        return self.physics.position
    
    @property
    def width(self) -> float:
        return self.physics.width
    
    @property
    def height(self) -> float:
        return self.physics.height
