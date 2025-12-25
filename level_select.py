# level_select.py
import arcade
from vector import Vector2
from button import Button
from save_sistem import SaveSystem

class LevelSelect:
    """Меню выбора уровня"""
    
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.save_system = SaveSystem()
        self.level_buttons = self._create_level_buttons()
        self.back_button = self._create_back_button()
    
    def _create_level_buttons(self) -> list[Button]:
        """Создаёт кнопки уровней (30 уровней)"""
        buttons = []
        buttons_per_row = 6
        button_size = 70
        spacing = 10
        margin = 100
        
        start_x = margin + button_size // 2
        start_y = self.screen_height - margin - button_size // 2
        
        for level in range(1, 31):
            row = (level - 1) // buttons_per_row
            col = (level - 1) % buttons_per_row
            
            x = start_x + col * (button_size + spacing)
            y = start_y - row * (button_size + spacing)
            
            # Определяем, открыт ли уровень
            is_unlocked = self.save_system.is_level_unlocked(level)
            
            if is_unlocked:
                text = str(level)
                color = (100, 180, 100)  # Зелёный - открыт
            else:
                text = "?"
                color = (100, 100, 100)  # Серый - закрыт
            
            button = Button(
                text=text,
                position=Vector2(x, y),
                width=button_size,
                height=button_size,
                color=color,
                font_size=20
            )
            button.level_num = level
            button.is_unlocked = is_unlocked
            buttons.append(button)
        
        return buttons
    
    def _create_back_button(self) -> Button:
        """Кнопка "Назад" """
        return Button(
            text="Назад",
            position=Vector2(80, 40),
            width=120,
            height=40
        )
    
    def handle_mouse_click(self, x: float, y: float):
        """Обрабатывает клик мыши"""
        # Проверяем кнопку "Назад"
        if self.back_button.is_clicked(x, y):
            return {"action": "back"}
        
        # Проверяем кнопки уровней
        for button in self.level_buttons:
            if button.is_clicked(x, y) and button.is_unlocked:
                print(f"🎯 Выбран уровень {button.level_num}")
                return {"action": "start_game", "level_num": button.level_num}
        
        return None
    
    def draw(self):
        """Рисует меню выбора уровня"""
        # Фон
        arcade.draw_lbwh_rectangle_filled(
            0, 0,
            self.screen_width, self.screen_height,
            (50, 50, 70)
        )
        
        # Заголовок
        arcade.draw_text(
            "ВЫБОР УРОВНЯ",
            self.screen_width // 2, self.screen_height - 60,
            arcade.color.WHITE, 36,
            align="center", anchor_x="center", anchor_y="center",
            bold=True
        )
        
        # Информация
        unlocked = self.save_system.get_unlocked_levels_count()
        arcade.draw_text(
            f"Открыто уровней: {unlocked}/30",
            self.screen_width // 2, self.screen_height - 100,
            arcade.color.LIGHT_GRAY, 20,
            align="center", anchor_x="center", anchor_y="center"
        )
        
        # Кнопки уровней
        for button in self.level_buttons:
            button.draw()
        
        # Кнопка "Назад"
        self.back_button.draw()