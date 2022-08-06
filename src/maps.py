from sys import exit
from time import sleep
from first_boss import FirstBoss
from second_boss import SecondBoss
from third_boss import ThirdBoss
import os


class Scene():
    def enter(self):
        print('Must be override.')
        exit(1)


class Map():
    def __init__(self, first_room):
        self.rooms = {'boss_1': RoomBoss1(),
                      'boss_2': RoomBoss2(),
                      'boss_3': RoomBoss3(),
                      'game_over': GameOver(),
                      'room_finished': Finished()}

        self.current_room = first_room

    def enter_room(self):
        return self.next_room(self.current_room)

    def next_room(self, room_name):
        return self.rooms.get(room_name)


class RoomBoss1(Scene):
    def enter(self):
        boss = FirstBoss()
        os.system('clear')
        print(f"\t\tYou entered the {boss.name}'s room")
        print("\t\t     Get ready for battle!\n\n")
        sleep(2)
        boss.intro()
        return boss.battle()

class RoomBoss2(Scene):
    def enter(self):
        boss = SecondBoss()
        os.system('clear')
        print(f"\t\tYou entered the {boss.name}'s room")
        print("\t\t     Get ready for battle!\n\n")
        sleep(2)
        boss.intro()
        return boss.battle()

class RoomBoss3(Scene):
    def enter(self):
        boss = ThirdBoss()
        os.system('clear')
        print(f"\t\tYou entered the {boss.name}'s room")
        print("\t\t     Get ready for battle!\n\n")
        sleep(2)
        boss.intro()
        return boss.battle()

class GameOver(Scene):
    def enter(self):
        print("\tYou kinda suck at this, don't you? :(")
        return 'room_finished'

class Finished(Scene):
    def enter(self):
        print('\n\n\t\t    Game over.')
        print('\t\tThanks for playing.')
        exit(1)
