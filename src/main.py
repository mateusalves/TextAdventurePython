from engine import Engine
from maps import Map


if __name__ == "__main__":
    a_map = Map('boss_1')
    a_game = Engine(a_map)
    a_game.play()


