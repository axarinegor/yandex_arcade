from abc import ABC
from physics import Physics, SHAPE, SPAWN_POSITION
from vector import Vector2, Vector2Int
from dataclasses import dataclass, field
import protocols as proto

@dataclass
class Player(proto.Player):
    physics: Physics = field(default_factory=Physics)
    _speed: float = 150.0
    
    @property
    def position(self) -> Vector2:
        return self.physics.position
    
    def set_direction(self, direction: Vector2) -> None:
        assert direction.length <= 1
        self.physics.move(direction, self._speed)
    
    def jump(self) -> None:
        self.physics.jump()
    
    def update(self, dt: float, platforms: list = None) -> None:
        self.physics.update(dt)

        if platforms:
            player_corners = [
                Vector2(self.physics.left, self.physics.bottom),
                Vector2(self.physics.right, self.physics.bottom),
                Vector2(self.physics.left, self.physics.bottom + 1),
                Vector2(self.physics.right, self.physics.bottom + 1)
            ]
            
            is_on_platform = False
            
            for platform in platforms:
                temp_physics = Physics(
                    position=platform.position,
                    width=platform.width,
                    height=platform.height
                )
                
                has_collision, side, overlap = self.physics.check_collision(temp_physics)
                
                if has_collision:
                    self.physics.resolve_collision(temp_physics, side, overlap)
                    if side == 'top':
                        is_on_platform = True
                        pass
                    
                for corner in player_corners:
                    corner_physics = Physics(
                        position=corner,
                        width=1.0,
                        height=1.0
                    )
                    corner_collision, corner_side, _ = corner_physics.check_collision(temp_physics)
                    if corner_collision and corner_side == 'top':
                        is_on_platform = True
                        break
            
            self.physics.on_ground = is_on_platform
        