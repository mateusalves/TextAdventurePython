from maps import *



class Engine():

    def __init__(self, a_room):
        self.room = a_room

    def play(self):
        current_room = self.room.enter_room()
        last_room = self.room.next_room('room_finished')

        while current_room != last_room:
            next_room = current_room.enter()
            print(next_room)
            current_room = self.room.next_room(next_room)

        current_room.enter()


