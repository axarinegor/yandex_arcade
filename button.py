from dataclasses import dataclass
from vector import Vector2
import arcade

@dataclass
class Button:
    text: str
    position: Vector2
    width: float = 200
    height: float = 60
    color: tuple = (100, 100, 180)
    text_color: tuple = (255, 255, 255)
    font_size: int = 24
    
    def __post_init__(self):
        self.text_obj = arcade.Text(
            text=self.text,
            x=self.position.x,
            y=self.position.y,
            color=self.text_color,
            font_size=self.font_size,
            anchor_x="center",
            anchor_y="center"
        )
    
    def is_clicked(self, mouse_x: float, mouse_y: float) -> bool:
        left = self.position.x - self.width / 2
        right = self.position.x + self.width / 2
        bottom = self.position.y - self.height / 2
        top = self.position.y + self.height / 2
        
        return left <= mouse_x <= right and bottom <= mouse_y <= top
    
    def draw(self) -> None:
        arcade.draw_lbwh_rectangle_filled(
            self.position.x - self.width // 2, self.position.y - self.height // 2,
            self.width, self.height,
            self.color
        )
        
        arcade.draw_lbwh_rectangle_outline(
            self.position.x - self.width // 2, self.position.y - self.height // 2,
            self.width, self.height,
            (255, 255, 255), 2
        )
        
        self.text_obj.draw()