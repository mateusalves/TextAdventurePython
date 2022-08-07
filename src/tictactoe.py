from time import sleep
from random import randint
from challenges import Challenge
import os


class TicTacToe(Challenge):

    def __init__(self, player_choice='x'):
        self.set_player_choice(player_choice)
        self.reset_game()

    def set_player_choice(self, new_player_choice):
        self.player_choice = new_player_choice
        self.boss_choice = 'o' if self.player_choice == 'x' else 'x'

    def play(self):
        while not self.champz:
            self.screen()
            self.next_movement(input('Your turn > '))
            self.champz = self.finished()

        self.screen()
        if self.champz == self.player_choice:
            print('player victory')
            return 'player_victory'
        elif self.champz == self.boss_choice:
            print('boss victory')
            return 'boss_victory'
        else:
            print('draw')
            return 'draw'

    def screen(self):
        os.system('clear')
        print("""\n\t\t   a     b     c
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

    def reset_game(self):
        self.moves = {'1a': '-', '1b': '-', '1c': '-',
                      '2a': '-', '2b': '-', '2c': '-',
                      '3a': '-', '3b': '-', '3c': '-'}
        self.moves_left = ['1a', '1b', '1c',
                          '2a', '2b', '2c',
                          '3a', '3b', '3c']
        self.champz = None

    def next_movement(self, player_movement):
        try:
            if self.moves[player_movement] != '-':
                raise Exception

            self.moves[player_movement] = self.player_choice
            self.moves_left.remove(player_movement)
            self.screen()

            if self.finished():
                return

            boss_move = self.moves_left[randint(0, len(self.moves_left)-1)]
            print('Boss turn > ', end="", flush=True)
            sleep(2)
            print(boss_move)
            self.moves[boss_move] = self.boss_choice
            self.moves_left.remove(boss_move)

        except Exception:
            print("Wrong movement. Please, select another one.")
            print("Choose line and column in this order. Ex: '1a'")
            input('Press any key to continue...')


    def finished(self):
        if(self.moves['1a'] != '-' and self.moves['1a'] == self.moves['1b'] and
           self.moves['1a'] == self.moves['1c']):
            return self.moves['1a']
        elif(self.moves['2a'] != '-' and self.moves['2a'] == self.moves['2b'] and
             self.moves['2a'] == self.moves['2c']):
            return self.moves['2a']
        elif(self.moves['3a'] != '-' and self.moves['3a'] == self.moves['3b'] and
             self.moves['3a'] == self.moves['3c']):
            return self.moves['3a']

        elif(self.moves['1a'] != '-' and self.moves['1a'] == self.moves['2a'] and
           self.moves['1a'] == self.moves['3a']):
            return self.moves['1a']
        elif(self.moves['1b'] != '-' and self.moves['1b'] == self.moves['2b'] and
             self.moves['1b'] == self.moves['3b']):
            return self.moves['1b']
        elif(self.moves['1c'] != '-' and self.moves['1c'] == self.moves['2c'] and
             self.moves['1c'] == self.moves['3c']):
            return self.moves['1c']

        elif(self.moves['1a'] != '-' and self.moves['1a'] == self.moves['2b'] and
           self.moves['1a'] == self.moves['3c']):
            return self.moves['1a']
        elif(self.moves['1c'] != '-' and self.moves['1c'] == self.moves['2b'] and
             self.moves['1c'] == self.moves['3a']):
            return self.moves['1c']
        elif not self.moves_left:
            return 'draw'
        else:
            return None

if __name__ == "__main__":
    ticTacToe = TicTacToe()
    ticTacToe.player_choice = 'o'
    ticTacToe.play()
