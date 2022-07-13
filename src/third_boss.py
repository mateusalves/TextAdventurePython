from time import sleep
from random import randint
from characters import Character
from tictactoe import TicTacToe
import os


class ThirdBoss(Character):

    def __init__(self, name):
        self.name = name
        self.input = 'y'
        os.system("clear")
        # self.talk("I'm the first Boss. Do you want to play some game?")
        # # self.input = (input('[y/n]? > ')).lower()
        # self.talk("It's not like you have a choice! HAHAHAHA.")
        # self.talk("Behold the evil tic tac toe!")
        self.ticTacToe = TicTacToe()
        # self.talk("Did you love it? Isn't beautiful? I surely put a lot of effort into this.")
        # self.talk("Enough with this conversation! Choose your weapon!")
        # self.playerChoice = (input('[x/o]? > ')).lower()
        self.playerChoice ='x'
        # if self.playerChoice not in ['x', 'o']:
        #     # sleep(2)
        #     os.system("clear")
        #     self.talk("Are you trying to be funny?")
        #     self.talk("...")
        #     self.talk("I'll be 'o' and you'll be 'x'")
        #     self.playerChoice = 'x'
        #     self.talk("This way you'll remember to never 'cross' my way again hihihi")
        #     self.talk("HAHAHAHA", dramatic_pause=0.1)
        #     self.talk("Did you get it? HAHA I'm nailing it today!")
        #     self.ticTacToe.screen()
        # self.talk("I'll even let you start since I'm so great at this!")
        # print("Choose line and column in this order. Ex: '1a'")
        # self.play()

    def play(self):
        while(True):
            self.input = (input(' > '))
            try:

                if self.ticTacToe.moves[self.input] != '-':
                    raise  Exception

                self.ticTacToe.moves[self.input] = self.playerChoice
                os.system("clear")
                self.ticTacToe.screen()
                self.ticTacToe.movesLeft.remove(self.input)
                bossMove = self.ticTacToe.movesLeft[randint(0, len(self.ticTacToe.movesLeft)-1)]
                self.ticTacToe.moves[bossMove] = 'o' if self.playerChoice == 'x' else 'x'
                self.ticTacToe.movesLeft.remove(bossMove)
                sleep(2)
                os.system("clear")
                self.ticTacToe.screen()
                champz = self.ticTacToe.check_win()
                if champz is not None:
                    if champz == self.playerChoice:
                        return self.defeated()
                    else:
                        return self.victorious()

            except Exception:
                if not self.ticTacToe.movesLeft:
                    self.talk("You're better than I expected! Lets go again!")
                    self.ticTacToe.reset_game()
                    os.system("clear")
                    self.talk("This time I'll bring my A-game!")
                    self.ticTacToe.screen()
                    print("Choose line and column in this order. Ex: '1a'")
                    continue

                self.talk("You better play right, fool!")
                print("Choose line and column in this order. Ex: '1a'")
                continue

    def defeated(self):
        self.talk("Ohh nooo!!! I underestimated you!")
        self.talk("Next time I won't loose again!")
        self.talk("You might not have the same luck.")
        return 'boss_2'

    def victorious(self):
        self.talk("For one little moment I thought you worth my time.")
        self.talk("You better practice a thousand years before challenging me again")
        self.talk("HA HA HA HA HA HA HA HA", dramatic_pause=0.15)
        return 'game_over'

