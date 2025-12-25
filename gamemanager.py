from game_state import GameState
from save_sistem import SaveSystem
from button import Button
from vector import Vector2
import arcade

class GameManager:    
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.state = GameState.MAIN_MENU
        self.save_system = SaveSystem()
        self.current_level = 1
        
        # Кнопки главного меню
        self.main_menu_buttons = self._create_main_menu_buttons()
        
        # Кнопки выбора уровня
        self.level_buttons = self._create_level_buttons()
        self.back_button = None
    
    def _create_main_menu_buttons(self) -> list[Button]:
        """Создаёт кнопки главного меню"""
        center_x = self.screen_width // 2
        buttons = []
        
        button_texts = [
            ("Играть с начала", self._start_new_game),
            ("Уровни", self._open_level_select),
            ("Выход", self._exit_game)
        ]
        
        start_y = self.screen_height // 2 + 80
        spacing = 70
        
        for i, (text, _) in enumerate(button_texts):
            button = Button(
                text=text,
                position=Vector2(center_x, start_y - i * spacing),
                width=300,
                height=50
            )
            buttons.append(button)
        
        return buttons
    
    def _create_level_buttons(self) -> list[Button]:
        """Создаёт кнопки выбора уровней (30 уровней)"""
        buttons = []
        buttons_per_row = 6
        button_size = 70
        spacing = 10
        margin = 50
        
        start_x = margin + button_size // 2
        start_y = self.screen_height - margin - button_size // 2
        
        for level in range(1, 31):
            row = (level - 1) // buttons_per_row
            col = (level - 1) % buttons_per_row
            
            x = start_x + col * (button_size + spacing)
            y = start_y - row * (button_size + spacing)
            
            # Определяем текст кнопки
            if self.save_system.is_level_unlocked(level):
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
            button.level_num = level  # Сохраняем номер уровня
            button.is_unlocked = self.save_system.is_level_unlocked(level)
            buttons.append(button)
        
        # Кнопка "Назад"
        self.back_button = Button(
            text="Назад",
            position=Vector2(80, 40),
            width=120,
            height=40
        )
        
        return buttons
    
    def _start_new_game(self) -> None:
        """Начинает новую игру (сброс прогресса)"""
        self.save_system.reset_progress()
        self.current_level = 1
        self.state = GameState.PLAYING
    
    def _open_level_select(self) -> None:
        """Открывает выбор уровня"""
        self.state = GameState.LEVEL_SELECT
    
    def _exit_game(self) -> None:
        """Выход из игры"""
        arcade.close_window()
    
    def handle_mouse_click(self, x: float, y: float) -> None:
        """Обрабатывает клик мыши в зависимости от состояния"""
        if self.state == GameState.MAIN_MENU:
            for button in self.main_menu_buttons:
                if button.is_clicked(x, y):
                    # Находим соответствующее действие
                    if button.text == "Играть с начала":
                        self._start_new_game()
                    elif button.text == "Уровни":
                        self._open_level_select()
                    elif button.text == "Выход":
                        self._exit_game()
                    break
        
        elif self.state == GameState.LEVEL_SELECT:
            # Проверяем кнопку "Назад"
            if self.back_button and self.back_button.is_clicked(x, y):
                self.state = GameState.MAIN_MENU
                return
            
            # Проверяем кнопки уровней
            for button in self.level_buttons:
                if button.is_clicked(x, y) and button.is_unlocked:
                    self.current_level = button.level_num
                    self.state = GameState.PLAYING
                    break
    
    def draw(self) -> None:
        """Рисует текущее состояние"""
        if self.state == GameState.MAIN_MENU:
            self._draw_main_menu()
        elif self.state == GameState.LEVEL_SELECT:
            self._draw_level_select()
    
    def _draw_main_menu(self) -> None:
        """Рисует главное меню"""
        # Фон
        arcade.draw_lbwh_rectangle_filled(
            0, 0,
            self.screen_width, self.screen_height,
            (40, 40, 60)
        )
        
        # Заголовок
        arcade.draw_text(
            "I LOVE THIS GAME",
            self.screen_width // 2, self.screen_height - 100,
            arcade.color.GOLD, 48,
            align="center", anchor_x="center", anchor_y="center",
            font_name=("Impact", "Arial Black"), bold=True
        )
        
        # Кнопки
        for button in self.main_menu_buttons:
            button.draw()
    
    def _draw_level_select(self) -> None:
        """Рисует выбор уровня"""
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
        
        # Подсказка
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