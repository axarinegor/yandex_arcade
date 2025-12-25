from block import Platform
from draw import Draw, PLAYER_SIZE
from texts import *
from level_pattern import Lev_Patterns
from observer import Event, OnEventSubscriber
import arcade
from physics import BLOCK_HEIGHT, SHAPE, Physics
from vector import Vector2, Vector2Int
import protocols as proto
from door import Door
from gamerules import GameRules
from level_pattern import Lev_Patterns
#from block import Platform

from digit_block import DIGIT_BLOCK_WIDTH, DigitBlock, LetterBlock


class GameEngine_1(arcade.Window):
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 door_is_open: bool = True
                 ) -> None:
        super().__init__(screen_shape.x, screen_shape.y, title, vsync=True)
        self._platforms = [i for i in Lev_Patterns.get_default(1)]
        self.background_color = (213, 255, 202)
        self.block_texture = Lev_Patterns.get_default_block()
        self._exit_position = Vector2(SHAPE.x - 15, BLOCK_HEIGHT + PLAYER_SIZE.y // 2)


        if not door_is_open:
            _pos_x = SHAPE.x - BLOCK_HEIGHT + 5
            _width = 10
        else:
            _pos_x = SHAPE.x - BLOCK_HEIGHT // 2
            _width = BLOCK_HEIGHT
        door_physics = Physics(position=Vector2(_pos_x, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=_width,
                                    height=PLAYER_SIZE.y + 16
                                )
        left_door_physics = Physics(position=Vector2(BLOCK_HEIGHT // 2, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=BLOCK_HEIGHT,
                                    height=PLAYER_SIZE.y + 16
                                )
        self._door = Door(physics=door_physics, is_open=door_is_open)
        self._left_door = Door(physics=left_door_physics, is_open=True)
        self._player = player
        self._draw = draw
        self.pressed_keys = set[int]()

        #self._mouse_clicked_left = Event[Vector2, None]()
        self._keyboard_state_changed = Event[set[int], None]()
       

    '''@property
    def mouse_clicked(self) -> OnEventSubscriber[Vector2, None]:
        return self._mouse_clicked_left.subscriber'''

    '''def bounce(self, platform:Platform):
        player_hitbox = arcade.Sprite(..., hit_box_algorithm="Simple")
        collisions = arcade.check_for_collision(self._player, platform)
        collision_list = arcade.check_for_collision_with_list(self._player, platform_list)'''
    
    @property
    def keyboard_state_changed(self) -> OnEventSubscriber[set[int], None]:
        return self._keyboard_state_changed.subscriber

    def on_fixed_update(self, delta_time: float) -> None:
        if not self._door.is_open:
            all_collision_objects = self._platforms + [self._door]
            self._player.update(delta_time, all_collision_objects) 
            return
        self._player.update(delta_time, self._platforms) 
        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.exit_game()

    '''def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        self._mouse_clicked_left.invoke(Vector2(x, y))'''

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_draw(self) -> None:
        self.clear()
        self._draw.player(self._player)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self.block_texture)
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        self._draw.texts(LEVEL_1)
        

class GameEngine_2(arcade.Window):
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 door_is_open: bool
                 ) -> None:
        super().__init__(screen_shape.x, screen_shape.y, title, vsync=True)
        self.background_color = (213, 255, 202)
        self.block_texture = Lev_Patterns.get_default_block()
        self._exit_position = Vector2(SHAPE.x - 15, BLOCK_HEIGHT + PLAYER_SIZE.y // 2)
        if not door_is_open:
            _pos_x = SHAPE.x - BLOCK_HEIGHT + 5
            _width = 10
        else:
            _pos_x = SHAPE.x - BLOCK_HEIGHT // 2
            _width = BLOCK_HEIGHT
        door_physics = Physics(position=Vector2(_pos_x, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=_width,
                                    height=PLAYER_SIZE.y + 16
                                )
        left_door_physics = Physics(position=Vector2(BLOCK_HEIGHT // 2, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=BLOCK_HEIGHT,
                                    height=PLAYER_SIZE.y + 16
                                )
        self._door = Door(physics=door_physics, is_open=door_is_open)
        self._left_door = Door(physics=left_door_physics, is_open=True)
        self._player = player
        self._draw = draw
        self.pressed_keys = set[int]()

        #self._mouse_clicked_left = Event[Vector2, None]()
        self._keyboard_state_changed = Event[set[int], None]()


        self._platforms = [i for i in Lev_Patterns.get_default(2)]


       

    '''@property
    def mouse_clicked(self) -> OnEventSubscriber[Vector2, None]:
        return self._mouse_clicked_left.subscriber'''

    '''def bounce(self, platform:Platform):
        player_hitbox = arcade.Sprite(..., hit_box_algorithm="Simple")
        collisions = arcade.check_for_collision(self._player, platform)
        collision_list = arcade.check_for_collision_with_list(self._player, platform_list)'''
    
    @property
    def keyboard_state_changed(self) -> OnEventSubscriber[set[int], None]:
        return self._keyboard_state_changed.subscriber

    def on_fixed_update(self, delta_time: float) -> None:
        if not self._door.is_open:
            all_collision_objects = self._platforms + [self._door]
            self._player.update(delta_time, all_collision_objects) 
            return
        self._player.update(delta_time, self._platforms) 
        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.exit_game()

    '''def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        self._mouse_clicked_left.invoke(Vector2(x, y))'''

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_draw(self) -> None:
        self.clear()
        self._draw.player(self._player)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self.block_texture)
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        self._draw.texts(LEVEL_2)


DOOR_OPEN = True

class GameEngine_4(arcade.Window):
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player
                 ) -> None:
        super().__init__(screen_shape.x, screen_shape.y, title, vsync=True)
        self._platforms = [i for i in Lev_Patterns.get_default(4)]
        self.background_color = (213, 255, 202)
        self.block_texture = Lev_Patterns.get_default_block()
        self._exit_position = Vector2(SHAPE.x - 15, BLOCK_HEIGHT + PLAYER_SIZE.y // 2)

        _pos_x = SHAPE.x - BLOCK_HEIGHT + 5
        _width = 10
        
        self.door_physics = Physics(position=Vector2(_pos_x, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=_width,
                                    height=PLAYER_SIZE.y + 16
                                )
        left_door_physics = Physics(position=Vector2(BLOCK_HEIGHT // 2, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=BLOCK_HEIGHT,
                                    height=PLAYER_SIZE.y + 16
                                )
        self._door = Door(physics=self.door_physics)
        self._left_door = Door(physics=left_door_physics, is_open=True)
        self._player = player
        self._draw = draw
        self.pressed_keys = set[int]()
        self.ANSWER = [3, 0, 4]
        #self._mouse_clicked_left = Event[Vector2, None]()
        self._keyboard_state_changed = Event[set[int], None]()

        self.digit_blocks = []
        
        # Позиции для 3 блоков (рядом друг с другом)
        start_x = 500
        for i in range(3):
            block = DigitBlock(
                physics=Physics(
                    position=Vector2(start_x + i * (DIGIT_BLOCK_WIDTH + 30), 500),
                    width=DIGIT_BLOCK_WIDTH,
                    height=DIGIT_BLOCK_WIDTH,
                    is_active=False
                )
            )
            self.digit_blocks.append(block)
       


    '''@property
    def mouse_clicked(self) -> OnEventSubscriber[Vector2, None]:
        return self._mouse_clicked_left.subscriber'''

    '''def bounce(self, platform:Platform):
        player_hitbox = arcade.Sprite(..., hit_box_algorithm="Simple")
        collisions = arcade.check_for_collision(self._player, platform)
        collision_list = arcade.check_for_collision_with_list(self._player, platform_list)'''
    
    @property
    def keyboard_state_changed(self) -> OnEventSubscriber[set[int], None]:
        return self._keyboard_state_changed.subscriber

    def on_fixed_update(self, delta_time: float) -> None:
        if not self._door.is_open:
            all_collision_objects = self._platforms + [self._door] + [i for i in self.digit_blocks]
            self._player.update(delta_time, all_collision_objects) 
        else:
            self._player.update(delta_time, self._platforms + self.digit_blocks) 
        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.exit_game()
        
        digs = [i.get_digit for i in self.digit_blocks]
        if digs == self.ANSWER:
            self.change_door(self._door, True)
            self._door.set_position(Vector2(SHAPE.x - BLOCK_HEIGHT // 2, self._door.position.y))
            self._door.set_width(BLOCK_HEIGHT)
        else:
            self.change_door(self._door, False)
            self._door.set_position(Vector2(SHAPE.x - BLOCK_HEIGHT + 5, self._door.position.y))
            self._door.set_width(10)        


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button == arcade.MOUSE_BUTTON_LEFT:
            mouse_pos = Vector2(x, y)
            
            # Проверяем каждый блок
            for block in self.digit_blocks:
                left = block.position.x - block.width/2
                right = block.position.x + block.width/2
                bottom = block.position.y - block.height/2
                top = block.position.y + block.height/2
                
                if left <= x <= right and bottom <= y <= top:
                    block.increment()
                    break

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_draw(self) -> None:
        self.clear()
        self._draw.player(self._player)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self.block_texture)
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        for block in self.digit_blocks:
            self._draw.digit_block(block)
        self._draw.texts(LEVEL_4)
        self._draw.level_4()
    
    
    def change_door(self, door: Door, only: bool = None) -> None:
        if only == None:
            door.set_open(True if door.is_open == False else False)
            return
        door.set_open(only)
        

class GameEngine_12(arcade.Window):
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player
                 ) -> None:
        super().__init__(screen_shape.x, screen_shape.y, title, vsync=True)
        self._platforms = [i for i in Lev_Patterns.get_default(12)]
        self.background_color = (213, 255, 202)
        self.block_texture = Lev_Patterns.get_default_block()
        self._exit_position = Vector2(SHAPE.x - 15, BLOCK_HEIGHT + PLAYER_SIZE.y // 2)

        _pos_x = SHAPE.x - BLOCK_HEIGHT + 5
        _width = 10
        
        self.door_physics = Physics(position=Vector2(_pos_x, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=_width,
                                    height=PLAYER_SIZE.y + 16
                                )
        left_door_physics = Physics(position=Vector2(BLOCK_HEIGHT // 2, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=BLOCK_HEIGHT,
                                    height=PLAYER_SIZE.y + 16
                                )
        self._door = Door(physics=self.door_physics)
        self._left_door = Door(physics=left_door_physics, is_open=True)
        self._player = player
        self._draw = draw
        self.pressed_keys = set[int]()
        self.ANSWER = ['E', 'G', 'O', 'R']
        #self._mouse_clicked_left = Event[Vector2, None]()
        self._keyboard_state_changed = Event[set[int], None]()

        self.digit_blocks = []
        
        # Позиции для 3 блоков (рядом друг с другом)
        start_x = 500
        for i in range(4):
            block = LetterBlock(
                physics=Physics(
                    position=Vector2(start_x + i * (DIGIT_BLOCK_WIDTH + 30), 400),
                    width=DIGIT_BLOCK_WIDTH,
                    height=DIGIT_BLOCK_WIDTH,
                    is_active=False
                )
            )
            self.digit_blocks.append(block)
       


    '''@property
    def mouse_clicked(self) -> OnEventSubscriber[Vector2, None]:
        return self._mouse_clicked_left.subscriber'''

    '''def bounce(self, platform:Platform):
        player_hitbox = arcade.Sprite(..., hit_box_algorithm="Simple")
        collisions = arcade.check_for_collision(self._player, platform)
        collision_list = arcade.check_for_collision_with_list(self._player, platform_list)'''
    
    @property
    def keyboard_state_changed(self) -> OnEventSubscriber[set[int], None]:
        return self._keyboard_state_changed.subscriber

    def on_fixed_update(self, delta_time: float) -> None:
        if not self._door.is_open:
            all_collision_objects = self._platforms + [self._door] + [i for i in self.digit_blocks]
            self._player.update(delta_time, all_collision_objects) 
        else:
            self._player.update(delta_time, self._platforms + self.digit_blocks) 
        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.exit_game()
        
        digs = [i.get_digit for i in self.digit_blocks]
        if digs == self.ANSWER:
            self.change_door(self._door, True)
            self._door.set_position(Vector2(SHAPE.x - BLOCK_HEIGHT // 2, self._door.position.y))
            self._door.set_width(BLOCK_HEIGHT)
        else:
            self.change_door(self._door, False)
            self._door.set_position(Vector2(SHAPE.x - BLOCK_HEIGHT + 5, self._door.position.y))
            self._door.set_width(10)        


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button == arcade.MOUSE_BUTTON_LEFT:
            mouse_pos = Vector2(x, y)
            
            # Проверяем каждый блок
            for block in self.digit_blocks:
                left = block.position.x - block.width/2
                right = block.position.x + block.width/2
                bottom = block.position.y - block.height/2
                top = block.position.y + block.height/2
                
                if left <= x <= right and bottom <= y <= top:
                    block.increment()
                    break

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_draw(self) -> None:
        self.clear()
        self._draw.player(self._player)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self.block_texture)
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        for block in self.digit_blocks:
            self._draw.digit_block(block)
        self._draw.texts(LEVEL_12)
    
    
    def change_door(self, door: Door, only: bool = None) -> None:
        if only == None:
            door.set_open(True if door.is_open == False else False)
            return
        door.set_open(only)
        

class GameEngine_7(arcade.Window):
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 door_is_open: bool = True
                 ) -> None:
        super().__init__(screen_shape.x, screen_shape.y, title, vsync=True)
        self.background_color = (213, 255, 202)
        self.block_texture = Lev_Patterns.get_default_block()
        self._exit_position = Vector2(SHAPE.x - 15, BLOCK_HEIGHT + PLAYER_SIZE.y // 2)
        if not door_is_open:
            _pos_x = SHAPE.x - BLOCK_HEIGHT + 5
            _width = 10
        else:
            _pos_x = SHAPE.x - BLOCK_HEIGHT // 2
            _width = BLOCK_HEIGHT
        door_physics = Physics(position=Vector2(_pos_x, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=_width,
                                    height=PLAYER_SIZE.y + 16
                                )
        left_door_physics = Physics(position=Vector2(BLOCK_HEIGHT // 2, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=BLOCK_HEIGHT,
                                    height=PLAYER_SIZE.y + 16
                                )
        self._door = Door(physics=door_physics, is_open=door_is_open)
        self._left_door = Door(physics=left_door_physics, is_open=True)
        self._player = player
        self._draw = draw
        self.pressed_keys = set[int]()

        #self._mouse_clicked_left = Event[Vector2, None]()
        self._keyboard_state_changed = Event[set[int], None]()


        self._platforms = [i for i in Lev_Patterns.get_default(7)]
        self.is_dark = False


    '''@property
    def mouse_clicked(self) -> OnEventSubscriber[Vector2, None]:
        return self._mouse_clicked_left.subscriber'''

    '''def bounce(self, platform:Platform):
        player_hitbox = arcade.Sprite(..., hit_box_algorithm="Simple")
        collisions = arcade.check_for_collision(self._player, platform)
        collision_list = arcade.check_for_collision_with_list(self._player, platform_list)'''
    
    @property
    def keyboard_state_changed(self) -> OnEventSubscriber[set[int], None]:
        return self._keyboard_state_changed.subscriber

    def on_fixed_update(self, delta_time: float) -> None:
        if not self._door.is_open:
            all_collision_objects = self._platforms + [self._door]
            self._player.update(delta_time, all_collision_objects) 
            return
        self._player.update(delta_time, self._platforms) 
        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.exit_game()
        self.is_dark = self._player.physics.on_ground

    '''def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        self._mouse_clicked_left.invoke(Vector2(x, y))'''

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_draw(self) -> None:
        self.clear()
        self._draw.player(self._player)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self.block_texture)
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        self._draw.texts(LEVEL_7)
        if self.is_dark:
            arcade.draw_lbwh_rectangle_filled(
                0, 0,
                self.width, self.height, arcade.color.BLACK
            )


class GameEngineFactory:
    """Фабрика для создания уровней по номеру"""
    
    LEVEL_CLASSES = {
        1: GameEngine_1,
        2: GameEngine_2,
        4: GameEngine_4,
        7: GameEngine_7,
        12: GameEngine_12,
        # ... добавь остальные классы по мере создания
    }
    
    @staticmethod
    def create_level(level_num: int, title: str, screen_shape, draw, player, **kwargs):
        """Создаёт уровень по номеру"""
        if level_num in GameEngineFactory.LEVEL_CLASSES:
            level_class = GameEngineFactory.LEVEL_CLASSES[level_num]
            
            # Проверяем параметры конструктора
            import inspect
            params = inspect.signature(level_class.__init__).parameters
            
            # Создаём с правильными параметрами
            if 'door_is_open' in params:
                return level_class(title, screen_shape, draw, player, 
                                 door_is_open=kwargs.get('door_is_open', True))
            else:
                return level_class(title, screen_shape, draw, player)
        else:
            # Фолбэк - первый уровень
            return GameEngine_1(title, screen_shape, draw, player)
    
    @staticmethod
    def get_available_levels():
        """Возвращает список доступных уровней"""
        return sorted(GameEngineFactory.LEVEL_CLASSES.keys())
    

LEVEL_MAPPING = {
    1: GameEngine_1,
    2: GameEngine_2, 
    4: GameEngine_4,
    7: GameEngine_7,
    12: GameEngine_12,
}



def create_level(level_num: int, title: str, screen_shape, draw, player, **kwargs):
    level_class = LEVEL_MAPPING.get(level_num)
    
    if not level_class:
        level_class = GameEngine_1
        level_num = 1
    
    
    if level_num in [1, 2, 7]:
        door_open = kwargs.get('door_is_open', True)
        return level_class(title, screen_shape, draw, player, door_is_open=door_open)
    else: 
        return level_class(title, screen_shape, draw, player)


def get_available_levels() -> list[int]:
    return sorted(LEVEL_MAPPING.keys())


def is_level_available(level_num: int) -> bool:
    return level_num in LEVEL_MAPPING