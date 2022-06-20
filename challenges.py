from textwrap import dedent


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
        self.print_screen()

    def print_screen(self):
        print("""\t\t   a     b     c
                      |     |
                1  -  |  -  |  -
                 _____|_____|_____
                      |     |
                2  -  |  -  |  -
                 _____|_____|_____
                      |     |
                3  -  |  -  |  -
                      |     |     """)


if __name__ == "__main__":
    ticTacToe = TicTacToe()
