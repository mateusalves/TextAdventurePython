from sys import exit
from bosses import *


class Scene():
    def enter(self):
        print('Must be override.')
        exit(1)


class Map():
    def __init__(self, first_room):
        self.rooms = {'boss_1': RoomBoss1(),
                      'boss_2': 'RoomBoss2()',
                      'boss_3': 'RoomBoss3()',
                      'death': 'Death()',
                      'room_finished': 'Finished()'}

        self.current_room = first_room

    def enter_room(self):
        return self.next_room(self.current_room)

    def next_room(self, room_name):
        return self.rooms.get(room_name)


class RoomBoss1(Scene):
    def enter(self):
        boss = FirstBoss()
        boss.talk()
