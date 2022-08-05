from time import sleep
from random import randint
from characters import Character
from tictactoe import TicTacToe
import os


class ThirdBoss(Character):

    def __init__(self, name="Boss#3"):
        self.name = name

    def intro(self):
        self.talk(f"My name is {self.name}. I'll certify that you regret entering my room")

    def battle(self):
        print('For each correct letter the player will win 1 point.')
        print('For each incorrect letter the player will loose 1 point.')
        print('At the end the points will be compared to determine the winner.\n\n')
        battle_result = self.hangman.play()
        if battle_result == 'draw':
            self.talk("You're better than I expected! Lets go again!")
            self.hangman.reset_game()
            os.system("clear")
            self.talk("This time I'll bring my A-game!")
            return self.battle()
        elif battle_result == 'player':
            return self.defeated()
        else:
            return self.victorious()

    def defeated(self):
        os.system("clear")
        self.hangman.screen()
        self.talk("Ohh nooo!!! I can't believe you defeated me!")
        input("Press any key to continue... ")
        return 'boss_3'

    def victorious(self):
        os.system("clear")
        self.hangman.screen()
        self.talk("This result was set the moment you decided to challenge me.")
        input("Press any key to continue... ")
        return 'game_over'

