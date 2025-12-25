from dataclasses import dataclass, field
from vector import Vector2, Vector2Int

JUMP_VELOCITY = 1100
SHAPE = Vector2Int(1250, 650)
SPAWN_POSITION = Vector2(100, 300)
BLOCK_HEIGHT = 50

@dataclass
class Physics:
    
    position: Vector2 = field(default_factory=Vector2.zero)
    velocity: Vector2 = field(default_factory=Vector2.zero)
    
    width: float = 32.0
    height: float = 48.0
    
    on_ground: bool = False 
    is_active: bool = True 
    
    gravity: float = 800.0
    max_fall_speed: float = 1000.0
    
    @property
    def bounds(self) -> tuple[float, float, float, float]:
        return (
            self.position.x - self.width / 2,
            self.position.x + self.width / 2,
            self.position.y - self.height / 2,
            self.position.y + self.height / 2
        )
    
    @property
    def left(self) -> float:
        return self.position.x - self.width / 2
    
    @property
    def right(self) -> float:
        return self.position.x + self.width / 2
    
    @property
    def bottom(self) -> float:
        return self.position.y - self.height / 2
    
    @property
    def top(self) -> float:
        return self.position.y + self.height / 2
    
    def apply_force(self, force: Vector2) -> None:
        self.velocity += force 
    
    def jump(self, jump_strength: float = JUMP_VELOCITY) -> bool:
        if self.on_ground and self.is_active:
            self.velocity = Vector2(self.velocity.x, jump_strength)
            self.on_ground = False
            return True
        return False
    
    def move(self, direction: Vector2, speed: float) -> None:
        if self.is_active:
            self.velocity = Vector2(direction.x * speed, self.velocity.y)
    
    def update(self, dt: float) -> None:
        if not self.is_active:
            return
        
        self.velocity = Vector2(
            self.velocity.x,
            self.velocity.y - self.gravity * dt
        )
        
        if self.velocity.y < -self.max_fall_speed:
            self.velocity = Vector2(self.velocity.x, -self.max_fall_speed)
        
        self.position += self.velocity * dt
        if (self.position.y < -600):
            self.position = SPAWN_POSITION
    
    def check_collision(self, other: 'Physics') -> tuple[bool, str, float]:
        left1, right1, bottom1, top1 = self.bounds
        left2, right2, bottom2, top2 = other.bounds
        
        if not (right1 > left2 and left1 < right2 and 
                top1 > bottom2 and bottom1 < top2):
            return False, "none", 0.0
        
        overlaps = {
            'left': right1 - left2,
            'right': right2 - left1,
            'top': top2 - bottom1,
            'bottom': top1 - bottom2
        }
        
        min_side = min(overlaps.items(), key=lambda x: x[1] if x[1] > 0 else float('inf'))
        
        return True, min_side[0], min_side[1]
    
    def resolve_collision(self, other: 'Physics', side: str, overlap: float) -> None:
        other_left, other_right, other_bottom, other_top = other.bounds
        '''
        is_falling_fast = self.velocity.y > 30
        is_jumping = self.velocity.y > 10
        '''

        if side == 'top':
            self.position = Vector2(
                self.position.x,
                other_top + self.height / 2 + 0.5
            )
            if self.velocity.y < 0:
                self.velocity = Vector2(self.velocity.x, 0)
                self.on_ground = True
                
        elif side == 'left':
            self.position = Vector2(
                other_left - self.width / 2,
                self.position.y
            )

                    
        elif side == 'right':
            self.position = Vector2(
                other_right + self.width / 2,
                self.position.y
            )

                    
        elif side == 'bottom':
            self.position = Vector2(
                self.position.x,
                other_bottom - self.height / 2 - 1.0
            )
            if self.velocity.y > 0:
                self.velocity = Vector2(self.velocity.x, 0)



