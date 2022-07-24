from time import sleep
from random import randint
from characters import Character
from tictactoe import TicTacToe
import os


class FirstBoss(Character):

    def __init__(self, name="Boss#1"):
        self.name = name
        self.ticTacToe = TicTacToe()

    def intro(self):
        self.talk(f"I'm the {self.name}. Do you want to play some game?")
        self.input = (input('[y/n]? > ')).lower()
        self.talk("It's not like you have a choice! HAHAHAHA.")
        self.talk("Behold the evil tic tac toe!")
        self.ticTacToe.screen()
        self.talk("Did you love it? Isn't beautiful? I surely put a lot of effort into this.")
        self.talk("Enough with this conversation! Choose your weapon!")
        self.player_choice = (input('[x/o]? > ')).lower()

        if self.player_choice not in ['x', 'o']:
            sleep(2)
            os.system("clear")
            self.talk("Are you trying to be funny?")
            self.talk("...")
            self.talk("I'll be 'o' and you'll be 'x'")
            self.talk("This way you'll remember to never 'cross' my way again hihihi")
            self.talk("HAHAHAHA", dramatic_pause=0.1)
            self.talk("Did you get it? HAHA I'm nailing it today!")
        else:
            self.ticTacToe.set_player_choice(self.player_choice)

        self.talk("I'll even let you start since I'm so great at this!")
        print("Choose line and column in this order. Ex: '1a'")

    def battle(self):
        battle_result = self.ticTacToe.play()
        if battle_result == 'draw':
            self.talk("You're better than I expected! Lets go again!")
            self.ticTacToe.reset_game()
            os.system("clear")
            self.talk("This time I'll bring my A-game!")
            print("Choose line and column in this order. Ex: '1a'")
            return self.battle()
        elif battle_result == 'player_victory':
            return self.defeated()
        else:
            return self.victorious()

    def defeated(self):
        os.system('clear')
        self.ticTacToe.screen()
        self.talk("Ohh nooo!!! I underestimated you!")
        self.talk("Next time I won't loose again!")
        input("Press any key to continue... ")
        return 'boss_2'

    def victorious(self):
        os.system('clear')
        self.ticTacToe.screen()
        self.talk("For one little moment I thought you worth my time.")
        self.talk("You better practice a thousand years before challenging me again")
        self.talk("HA HA HA HA HA HA HA HA", dramatic_pause=0.15)
        input("Press any key to continue... ")
        return 'game_over'

