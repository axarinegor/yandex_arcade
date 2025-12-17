from block import Platform
from draw import Draw, PLAYER_SIZE
from gameengine import GameEngine, SHAPE
from move import Move
from physics import Physics, SPAWN_POSITION
from player import Player
from vector import Vector2, Vector2Int
from door import Door
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
    #door = Door()
    game = GameEngine(TITLE, SHAPE, Draw(), player)
    game.keyboard_state_changed.subscribe(lambda keys: player.set_direction(Move.keys_to_direction(keys)))
    game.keyboard_state_changed.subscribe(
        lambda keys: player.jump() if Move.should_jump(keys) else None
    )
    arcade.run()



if __name__ == '__main__':
    main()