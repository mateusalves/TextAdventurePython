import os

class Screens():
    def __init__(self):
        self.moves = {'1a': '-', '1b': '-', '1c': '-',
                      '2a': '-', '2b': '-', '2c': '-',
                      '3a': '-', '3b': '-', '3c': '-'}
        self.movesLeft = ['1a', '1b', '1c',
                          '2a', '2b', '2c',
                          '3a', '3b', '3c']

    def borders(self):
        print("===============================================================================")

    def ticTacToeGame(self):
        # os.system("clear")
        print("""\n\n\t\t   a     b     c
                      |     |
                1  %s  |  %s  |  %s
                 _____|_____|_____
                      |     |
                2  %s  |  %s  |  %s
                 _____|_____|_____
                      |     |
                3  %s  |  %s  |  %s
                      |     |     \n\n""" %
              (self.moves['1a'], self.moves['1b'], self.moves['1c'],
              self.moves['2a'], self.moves['2b'], self.moves['2c'],
              self.moves['3a'], self.moves['3b'], self.moves['3c']))
        # input() #tests purposes

    def resetGame(self):
        self.moves = {'1a': '-', '1b': '-', '1c': '-',
                      '2a': '-', '2b': '-', '2c': '-',
                      '3a': '-', '3b': '-', '3c': '-'}
        self.movesLeft = ['1a', '1b', '1c',
                          '2a', '2b', '2c',
                          '3a', '3b', '3c']
