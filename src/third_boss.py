from time import sleep
from random import randint
from characters import Character
from lord_of_war import LordOfWar
import os


class ThirdBoss(Character):

    def __init__(self, name="Boss#3"):
        self.name = name
        self.war_game = LordOfWar()

    def intro(self):
        self.talk(f"I am {self.name}. Your lucky ends here!")
        self.talk("Unlike the others, I'll challenge you to face me in a best-of-three game.")
        self.talk("The game is The Lord Of War.")
        self.talk("You'll receive 100 soldiers and you can allocate them as you wish between 3 forces: navy, airforce and army.")
        self.talk("Each battle the one who wins in at least two out of the three forces will score a round.")
        self.talk("Then, after I defeat you, you will wish to have stopped at the others.")
        sleep(2)

    def battle(self):
        battle_result = self.war_game.play()
        if battle_result == 'Player':
            return self.defeated()
        else:
            return self.victorious()

    def defeated(self):
        self.talk("I thought you were only lucky to defeat the others.")
        self.talk("Congratulations, I shall let you pass.")
        input("Press any key to continue... ")
        return 'room_finished'

    def victorious(self):
        self.talk("I don't have anything to say to you...")
        input("Press any key to continue... ")
        return 'game_over'

