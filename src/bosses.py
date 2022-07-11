from time import sleep
from random import randint
from characters import Character
from challenges import TicTacToe
import os


class FirstBoss(Character):

    def __init__(self, name):
        self.name = name
        self.input = 'y'
        os.system("clear")
        self.talk("I'm the first Boss. Do you want to play some game?")
        self.input = (input('[y/n]? > ')).lower()
        self.talk("It's not like you have a choice! HAHAHAHA.")
        self.talk("Behold the evil tic tac toe!")
        self.ticTacToe = TicTacToe()
        self.talk("Did you love it? Isn't beautiful? I surely put a lot of effort into this.")
        self.talk("Enough with this conversation! Choose your weapon!")
        self.playerChoice = (input('[x/o]? > ')).lower()
        self.talk("I'll even let you start since I'm so great at this!")
        print("Choose line and column in this order. Ex: '1a'")
        self.play()

    def play(self):
        while(True):
            self.input = (input(' > '))
            # TODO: preciso fazer o sistema para entender o fim do jogo
            try:
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
            except Exception:
                if not self.ticTacToe.movesLeft:
                    self.talk("You're better than I expected! Lets go again!")
                    self.ticTacToe.resetGame()
                    os.system("clear")
                    self.talk("This time I'll bring my A-game!")
                    self.ticTacToe.screen()
                    print("Choose line and column in this order. Ex: '1a'")
                    continue

                self.talk("You better play right, fool!")
                print("Choose line and column in this order. Ex: '1a'")
                continue


class SecondBoss(Character):

    def __init__(self):
        pass

    def play(self):
        print("I'm the second Boss.")

class ThirdBoss(Character):

    def __init__(self):
        pass

    def play(self):
        print("I'm the third Boss.")

