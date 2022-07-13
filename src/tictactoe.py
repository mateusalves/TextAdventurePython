class TicTacToe():

    def __init__(self):
        self.moves = {'1a': '-', '1b': '-', '1c': '-',
                      '2a': '-', '2b': '-', '2c': '-',
                      '3a': '-', '3b': '-', '3c': '-'}
        self.moves_left = ['1a', '1b', '1c',
                           '2a', '2b', '2c',
                           '3a', '3b', '3c']
        self.screen()

    def screen(self):
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
        else:
            return None

if __name__ == "__main__":
    ticTacToe = TicTacToe()
