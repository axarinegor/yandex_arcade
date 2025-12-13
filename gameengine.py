from draw import Draw
from observer import Event, OnEventSubscriber
import arcade
from vector import Vector2, Vector2Int
import protocols as proto



class GameEngine(arcade.Window):
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player
                 ) -> None:
        super().__init__(screen_shape.x, screen_shape.y, title, vsync=True)
        self.background_color = arcade.color.CARIBBEAN_GREEN
        self._player = player
        self._draw = draw
        self.pressed_keys = set[int]()

        #self._mouse_clicked_left = Event[Vector2, None]()
        self._keyboard_state_changed = Event[set[int], None]()

    '''@property
    def mouse_clicked(self) -> OnEventSubscriber[Vector2, None]:
        return self._mouse_clicked_left.subscriber'''

    @property
    def keyboard_state_changed(self) -> OnEventSubscriber[set[int], None]:
        return self._keyboard_state_changed.subscriber

    def on_fixed_update(self, delta_time: float) -> None:
        self._player.update(delta_time)

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
