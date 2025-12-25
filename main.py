'''#from block import Platform
from draw import Draw, PLAYER_SIZE
from gameengine import *
from move import Move
from physics import SHAPE, Physics, SPAWN_POSITION
from player import Player
#from vector import Vector2, Vector2Int
#from door import Door
import arcade


TITLE = 'I love this game'

GRAVITY = 3000
PLAYER_VELOCITY = 400


def main() -> None:
    player_physics = Physics(
            position=SPAWN_POSITION,
            width=PLAYER_SIZE.x + 2,
            height=PLAYER_SIZE.y + 2,
            gravity=GRAVITY
        )

    player = Player(player_physics, PLAYER_VELOCITY)
    game = GameEngine_12(TITLE, SHAPE, Draw(), player)
    game.keyboard_state_changed.subscribe(lambda keys: player.set_direction(Move.keys_to_direction(keys)))
    game.keyboard_state_changed.subscribe(
        lambda keys: player.jump() if Move.should_jump(keys) else None
    )
    arcade.run()



if __name__ == '__main__':
    main()
'''


import arcade
from vector import Vector2Int
from draw import Draw, PLAYER_SIZE
from move import Move
from physics import SHAPE, Physics, SPAWN_POSITION
from player import Player
from gameengine import create_level
from main_menu import MainMenu
from level_select import LevelSelect


TITLE = 'I love this game'
GRAVITY = 3000
PLAYER_VELOCITY = 400
LEVEL_CLOSED_DOOR = [4, 12]

class GameApp(arcade.Window):    
    def __init__(self):
        super().__init__(SHAPE.x, SHAPE.y, TITLE, vsync=True)
        self.states = {
            "main_menu": MainMenu(SHAPE.x, SHAPE.y),
            "level_select": LevelSelect(SHAPE.x, SHAPE.y),
            "playing": None
        }
        
        self.current_state = "main_menu"
        self.player = None
        self.drawi = Draw()
        self.current_level_game = None
        self.current_level_num = 1
    
    def switch_state(self, new_state: str):
        self.current_state = new_state
    
    def start_game_level(self, level_num: int):
        player_physics = Physics(
            position=SPAWN_POSITION,
            width=PLAYER_SIZE.x + 2,
            height=PLAYER_SIZE.y + 2,
            gravity=GRAVITY
        )
        self.player = Player(player_physics, PLAYER_VELOCITY)
        self.current_level_num = level_num
        
        self.current_level_game = create_level(
            level_num=level_num,
            title=TITLE,
            screen_shape=SHAPE,
            draw=self.drawi,
            player=self.player,
            door_is_open=level_num not in LEVEL_CLOSED_DOOR
        )
        
        self.current_level_game.keyboard_state_changed.subscribe(
            lambda keys: self.player.set_direction(Move.keys_to_direction(keys))
        )
        self.current_level_game.keyboard_state_changed.subscribe(
            lambda keys: self.player.jump() if Move.should_jump(keys) else None
        )
        
        self.switch_state("playing")
    
    def handle_action(self, action_result):
        if not action_result:
            return
        
        action = action_result.get("action")
        
        if action == "start_game":
            level_num = action_result.get("level_num", 1)
            self.start_game_level(level_num)
        
        elif action == "open_level_select":
            self.switch_state("level_select")
        
        elif action == "back":
            self.switch_state("main_menu")
        
        elif action == "exit":
            arcade.close_window()
    
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        
        if self.current_state == "playing" and self.current_level_game:
            self.current_level_game.on_mouse_press(x, y, button, modifiers)
            return
        
        current_menu = self.states.get(self.current_state)
        if current_menu:
            action_result = current_menu.handle_mouse_click(x, y)
            self.handle_action(action_result)
    
    def on_fixed_update(self, delta_time: float):
        if self.current_state == "playing" and self.current_level_game:
            self.current_level_game.on_fixed_update(delta_time)
    
    def on_draw(self):
        self.clear()
        if self.current_state == "playing" and self.current_level_game:
            self.current_level_game.on_draw()
        else:
            current_menu = self.states.get(self.current_state)
            if current_menu:
                current_menu.draw()
    
    def on_key_press(self, symbol: int, modifiers: int):
        if self.current_state == "playing" and self.current_level_game:
            self.current_level_game.on_key_press(symbol, modifiers)
    
    def on_key_release(self, symbol: int, modifiers: int):
        if self.current_state == "playing" and self.current_level_game:
            self.current_level_game.on_key_release(symbol, modifiers)


def main():
    game = GameApp()
    arcade.run()


if __name__ == '__main__':
    main()