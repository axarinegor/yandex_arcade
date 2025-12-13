from abc import abstractmethod
from dataclasses import dataclass
import protocols as proto
import arcade
from vector import Vector2, Vector2Int

BLOCK_RADIUS = 30
@dataclass
class Block:
    position: Vector2Int
    radius: int = BLOCK_RADIUS
    color: arcade.color = arcade.color.SKOBELOFF

    @property
    @abstractmethod
    def position(self) -> Vector2:
        ...

    def dis_to_player(self, player: proto.Player) -> Vector2:
        return max(Vector2(0, 0), Vector2(*(self.position - player.position).tuple))
        

    @abstractmethod
    def update(self, dt: float) -> None:
        ...