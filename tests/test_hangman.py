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
from hangman import HangMan


class TestHangMan(unittest.TestCase):
    def setUp(self):
        self.hangman = HangMan()
        self.default_body_parts = {'head': 'O', 'l_arm': '/', 'r_arm': '\\',
                                   'body': '|', 'l_leg': '/', 'r_leg': '\\'}
        self.default_lang = 'pt_br'
        self.default_currently_playing = 'player'
        self.default_player_points = 0
        self.default_boss_points = 0
        self.default_mistakes = 0
        self.default_guessed_letters = []
        self.default_chosen_letters = []

    def test_hangman_right_default_values(self):
        self.assertDictEqual(self.hangman.body_parts, self.default_body_parts)
        self.assertEqual(self.hangman.lang, self.default_lang)
        self.assertEqual(self.hangman.currently_playing, self.default_currently_playing)
        self.assertEqual(self.hangman.player_points, self.default_player_points)
        self.assertEqual(self.hangman.boss_points, self.default_boss_points)
        self.assertEqual(self.hangman.mistakes, self.default_mistakes)
        self.assertListEqual(self.hangman.guessed_letters, self.default_guessed_letters)
        self.assertListEqual(self.hangman.chosen_letters, self.default_chosen_letters)

    def test_play(self):
        '''
        Testing case of finishing game
        '''
        self.hangman.mistakes = 6
        self.hangman.player_points = 3
        self.hangman.boss_points = 0
        self.assertEqual(self.hangman.play(), 'player')

        self.hangman.reset_game()

        self.hangman.mistakes = 6
        self.hangman.player_points = 0
        self.hangman.boss_points = 3
        self.assertEqual(self.hangman.play(), 'boss')

        self.hangman.reset_game()

        self.hangman.mistakes = 6
        self.hangman.player_points = 0
        self.hangman.boss_points = 0
        self.assertEqual(self.hangman.play(), 'draw')

    @unittest.skip("For printing only: skipping")
    def test_screen(self):
        self.fail("It shouldn't happen")

    def test_reset_game(self):
        self.hangman.player_points = 6
        self.hangman.boss_points = 3
        self.hangman.guessed_letters.append('a')
        self.hangman.guessed_letters.append('b')
        self.hangman.guessed_letters.append('c')
        self.hangman.chosen_letters.append('d')
        self.hangman.chosen_letters.append('e')
        self.hangman.chosen_letters.append('f')
        self.hangman.mistakes = 3
        self.assertNotEqual(self.hangman.player_points, self.default_player_points)
        self.assertNotEqual(self.hangman.boss_points, self.default_boss_points)
        self.assertNotEqual(self.hangman.mistakes, self.default_mistakes)
        self.assertNotEqual(self.hangman.guessed_letters, self.default_guessed_letters)
        self.assertNotEqual(self.hangman.chosen_letters, self.default_chosen_letters)

        self.hangman.reset_game()

        self.assertEqual(self.hangman.player_points, self.default_player_points)
        self.assertEqual(self.hangman.boss_points, self.default_boss_points)
        self.assertEqual(self.hangman.mistakes, self.default_mistakes)
        self.assertListEqual(self.hangman.guessed_letters, self.default_guessed_letters)
        self.assertListEqual(self.hangman.chosen_letters, self.default_chosen_letters)

    def test_guess(self):
        self.hangman.chosen_letters.append('a')
        self.assertIsNone(self.hangman.guess('a'), 'letter already chosen')

        self.hangman.secret_word = 'test'
        self.assertFalse(self.hangman.guess('b'), 'Letter not chosen yet, but not in secret_word')

        self.assertTrue(self.hangman.guess('e'), 'Letter not chosen yet and in secret_word')

    def test_boss_guess(self):
        self.assertIsInstance(self.hangman.boss_guess(), str)

    def test_choose_random_word(self):
        self.assertIsInstance(self.hangman.choose_random_word(), str)

    def test_finished(self):
        self.hangman.guessed_letters = 'test_word'
        self.hangman.secret_word = 'test_word'
        self.assertTrue(self.hangman.finished())

        self.hangman.reset_game()

        self.hangman.mistakes = 6
        self.assertTrue(self.hangman.finished())

        self.hangman.reset_game()
        self.assertFalse(self.hangman.finished())


if __name__ == '__main__':
    unittest.main(verbosity=2)

