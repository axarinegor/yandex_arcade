from dataclasses import dataclass
from physics import Physics
from vector import Vector2
import arcade
import protocols as proto
from texts import pixel_font

DIGIT_BLOCK_WIDTH = 65
@dataclass
class DigitBlock(proto.Platform):
    """Блок с цифрой, которая меняется при клике"""
    physics: Physics
    current_digit: int = 0  # Текущая цифра (0-9)
    color: tuple = (213, 255, 202)  # Цвет блока
    text_color: tuple = (0, 0, 0) # Цвет цифры
    font_size: int = DIGIT_BLOCK_WIDTH // 3
    
    def __post_init__(self):
        self.physics.is_active = False
    
    @property
    def position(self) -> Vector2:
        return self.physics.position
    
    @property
    def width(self) -> float:
        return self.physics.width
    
    @property
    def height(self) -> float:
        return self.physics.height
    
    def update(self, dt: float) -> None:
        # Статичный блок, не обновляется
        pass
    
    def increment(self) -> None:
        """Увеличивает цифру (0→1→2...→9→0)"""
        self.current_digit = (self.current_digit + 1) % 10

    
    def decrement(self) -> None:
        """Уменьшает цифру (9→8→7...→0→9)"""
        self.current_digit = (self.current_digit - 1) % 10
    
    def set_digit(self, digit: int) -> None:
        """Устанавливает конкретную цифру"""
        self.current_digit = max(0, min(9, digit))
    
    def to_draw(self) -> arcade.Text:
        return arcade.Text(
            str(self.current_digit),
            self.position.x, self.position.y,
            self.text_color, self.font_size,
            align="center", anchor_x="center", anchor_y="center",
            font_name=pixel_font, bold=True
        )
    
    @property
    def get_digit(self) -> int:
        return self.current_digit
    

@dataclass
class LetterBlock:
    physics: Physics
    letter: str = 'A'  # Текущая цифра (0-9)
    color: tuple = (213, 255, 202)  # Цвет блока
    text_color: tuple = (0, 0, 0) # Цвет цифры
    font_size: int = DIGIT_BLOCK_WIDTH // 3

    def __post_init__(self):
        self.text = arcade.Text(
                text="A",
                x=self.physics.position.x,
                y=self.physics.position.y,
                color=(255, 255, 255),
                font_size=self.font_size,
                anchor_x="center",
                anchor_y="center",
                bold=True
            )
    
    def is_clicked(self, mouse_x, mouse_y):
        left = self.physics.left
        right = self.physics.right
        bottom = self.physics.bottom
        top = self.physics.top
        
        return (left <= mouse_x <= right and bottom <= mouse_y <= top)
    
    def increment(self):
        current_ord = ord(self.letter)
        if current_ord == ord('Z'):
            self.letter = 'A'
        else:
            self.letter = chr(current_ord + 1)
        self.text.text = self.letter
    
    @property
    def position(self):
        return self.physics.position
    
    @property
    def get_digit(self) -> int:
        return self.letter
    
    def to_draw(self) -> arcade.Text:
        return arcade.Text(
            str(self.letter),
            self.position.x, self.position.y,
            self.text_color, self.font_size,
            align="center", anchor_x="center", anchor_y="center",
            font_name=pixel_font, bold=True
        )
    
    @property
    def position(self) -> Vector2:
        return self.physics.position
    
    @property
    def width(self) -> float:
        return self.physics.width
    
    @property
    def height(self) -> float:
        return self.physics.height