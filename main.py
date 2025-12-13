from draw import Draw
from gameengine import GameEngine
from move import Move
from player import Player
from vector import Vector2, Vector2Int
import arcade


TITLE = 'I love this game'
SHAPE = Vector2Int(1500, 700)


def main() -> None:
    player = Player(Vector2(100, 100), 100)
    game = GameEngine(TITLE, SHAPE, Draw(), player)
    game.keyboard_state_changed.subscribe(lambda keys: player.set_direction(Move.keys_to_direction(keys)))
    arcade.run()



if __name__ == '__main__':
    main()