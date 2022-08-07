try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except Exception as e:
    print('Exception', e)

import unittest
from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.ticTacToe = TicTacToe()
        self.default_moves = {'1a': '-', '1b': '-', '1c': '-',
                              '2a': '-', '2b': '-', '2c': '-',
                              '3a': '-', '3b': '-', '3c': '-'}
        self.default_moves_left = ['1a', '1b', '1c',
                                   '2a', '2b', '2c',
                                   '3a', '3b', '3c']

    def test_tictactoe_right_default_values(self):
        self.assertEqual(self.ticTacToe.player_choice, 'x')
        self.assertEqual(self.ticTacToe.boss_choice, 'o')
        self.assertIsNone(self.ticTacToe.champz)
        self.assertDictEqual(self.ticTacToe.moves, self.default_moves)
        self.assertListEqual(self.ticTacToe.moves_left, self.default_moves_left)

    def test_set_player_choice(self):
        '''
        This method should assign a new value to player and toggle the boss value accordingly

        '''
        self.ticTacToe.set_player_choice('x')
        self.assertEqual(self.ticTacToe.player_choice, 'x')
        self.assertEqual(self.ticTacToe.boss_choice, 'o')

        self.ticTacToe.set_player_choice('o')
        self.assertEqual(self.ticTacToe.player_choice, 'o')
        self.assertEqual(self.ticTacToe.boss_choice, 'x')

    def test_play(self):
        '''
        Testing case of finishing game
        '''

        self.ticTacToe.set_player_choice('x')

        self.ticTacToe.champz = 'x'
        self.assertEqual(self.ticTacToe.play(), 'player_victory')

        self.ticTacToe.champz = 'o'
        self.assertEqual(self.ticTacToe.play(), 'boss_victory')

        self.ticTacToe.champz = 'draw'
        self.assertEqual(self.ticTacToe.play(), 'draw')

    @unittest.skip("For printing only: skipping")
    def test_screen(self):
        self.fail("It shouldn't happen")

    def test_reset_game(self):
        self.ticTacToe.moves['1a'] = 'x'
        self.ticTacToe.moves['2b'] = 'o'
        self.assertNotEqual(self.ticTacToe.moves, self.default_moves)

        self.ticTacToe.moves_left.remove('1a')
        self.ticTacToe.moves_left.remove('2b')
        self.assertNotEqual(self.ticTacToe.moves_left, self.default_moves_left)

        self.ticTacToe.champz = 'x'
        self.assertIsNotNone(self.ticTacToe.champz)

        self.ticTacToe.reset_game()
        self.assertDictEqual(self.ticTacToe.moves, self.default_moves)
        self.assertListEqual(self.ticTacToe.moves_left, self.default_moves_left)
        self.assertIsNone(self.ticTacToe.champz)

    def test_next_movement(self):
        '''
        This method will replace moves dict with player choice at the desired position
        Boss will automatically choose a value and replace in 'moves'
        Both player and boss movement should be removed from moves_left list
        '''
        self.ticTacToe.reset_game()
        self.assertDictEqual(self.ticTacToe.moves, self.default_moves)
        self.assertListEqual(self.ticTacToe.moves_left, self.default_moves_left)

        self.ticTacToe.next_movement('1b')

        self.assertEqual(self.ticTacToe.moves['1b'], self.ticTacToe.player_choice)
        self.assertNotEqual(self.ticTacToe.moves, self.default_moves)
        self.assertNotEqual(self.ticTacToe.moves_left, self.default_moves_left)

    def test_finished(self):
        self.ticTacToe.moves['1a'] = 'x'
        self.ticTacToe.moves['2b'] = 'x'
        self.ticTacToe.moves['3c'] = 'x'
        self.assertEqual(self.ticTacToe.finished(), 'x', 'Case of "x" winning')

        self.ticTacToe.reset_game()
        self.ticTacToe.moves['3a'] = 'o'
        self.ticTacToe.moves['2b'] = 'o'
        self.ticTacToe.moves['1c'] = 'o'
        self.assertEqual(self.ticTacToe.finished(), 'o', 'Case of "o" winning')

        self.ticTacToe.reset_game()
        self.ticTacToe.moves_left = []
        self.assertEqual(self.ticTacToe.finished(), 'draw', 'Case "draw"')


if __name__ == '__main__':
    unittest.main(verbosity=2)

