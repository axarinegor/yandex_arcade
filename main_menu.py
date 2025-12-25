# main_menu.py
import arcade
from vector import Vector2
from button import Button
from save_sistem import SaveSystem

class MainMenu:
    """Главное меню игры"""
    
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.save_system = SaveSystem()
        self.buttons = self._create_buttons()
        
        # Тексты
        self.title_text = arcade.Text(
            "I LOVE THIS GAME",
            screen_width // 2, screen_height - 100,
            arcade.color.GOLD, 48,
            align="center", anchor_x="center", anchor_y="center",
            font_name=("Impact", "Arial Black"), bold=True
        )
    
    def _create_buttons(self) -> list[Button]:
        """Создаёт кнопки главного меню"""
        center_x = self.screen_width // 2
        buttons = []
        
        button_texts = ["Играть с начала", "Уровни", "Выход"]
        
        start_y = self.screen_height // 2 + 80
        spacing = 70
        
        for i, text in enumerate(button_texts):
            button = Button(
                text=text,
                position=Vector2(center_x, start_y - i * spacing),
                width=300,
                height=50
            )
            buttons.append(button)
        
        return buttons
    
    def handle_mouse_click(self, x: float, y: float):
        """Обрабатывает клик мыши и возвращает действие"""
        for i, button in enumerate(self.buttons):
            if button.is_clicked(x, y):
                if i == 0:  # "Играть с начала"
                    print("🎮 Начинаем новую игру")
                    self.save_system.reset_progress()
                    return {"action": "start_game", "level_num": 1}
                elif i == 1:  # "Уровни"
                    print("📁 Открываем выбор уровня")
                    return {"action": "open_level_select"}
                elif i == 2:  # "Выход"
                    print("👋 Выход из игры")
                    return {"action": "exit"}
        return None
    
    def draw(self):
        arcade.draw_lbwh_rectangle_filled(
            0, 0,
            self.screen_width, self.screen_height,
            (40, 40, 60)
        )
        self.title_text.draw()
        for button in self.buttons:
            button.draw()