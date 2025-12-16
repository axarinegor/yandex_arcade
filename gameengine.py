from block import Platform
from draw import Draw, PLAYER_SIZE
from observer import Event, OnEventSubscriber
import arcade
from physics import Physics
from vector import Vector2, Vector2Int
import protocols as proto
#from block import Platform

SHAPE = Vector2Int(1250, 650)
BLOCK_HEIGHT = 50

class GameEngine(arcade.Window):
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player
                 ) -> None:
        super().__init__(screen_shape.x, screen_shape.y, title, vsync=True)
        self._platforms = [
            Platform(physics=Physics(
                position=Vector2(200, BLOCK_HEIGHT // 2),
                width=400,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 200, BLOCK_HEIGHT // 2),
                width=400,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(500, 200),
                width=100,
                height=BLOCK_HEIGHT // 2
            )),
            Platform(physics=Physics(
                position=Vector2(700, 200),
                width=100,
                height=BLOCK_HEIGHT // 2
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            ))
        ]
        self.background_color = arcade.color.CARIBBEAN_GREEN
        
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
        self._player.update(delta_time, self._platforms)

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
