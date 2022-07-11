from screens import Screens


class Challenge():

    def start(self):
        pass

    def next_turn(self):
        pass

    def end(self):
        pass

    def players(self):
        pass

    def score_board(self):
        pass

class TicTacToe(Challenge):

    def __init__(self):
        self.screen = Screens()
        self.screen.ticTacToeGame()

    def play(self):

        self.screen.ticTacToeGame()

        self.screen.moves['1a'] = '0'
        self.screen.ticTacToeGame()

    def resetGame(self):
        self.moves = {'1a': '-', '1b': '-', '1c': '-',
                      '2a': '-', '2b': '-', '2c': '-',
                      '3a': '-', '3b': '-', '3c': '-'}
        self.movesLeft = ['1a', '1b', '1c',
                          '2a', '2b', '2c',
                          '3a', '3b', '3c']

    def check_win(self):
        pass

if __name__ == "__main__":
    ticTacToe = TicTacToe()
