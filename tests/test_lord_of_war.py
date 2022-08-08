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
from lord_of_war import LordOfWar


class TestLordOfWar(unittest.TestCase):
    def setUp(self):
        self.lordgame = LordOfWar()
        self.default_boss_victories = 0
        self.default_player_victories = 0
        self.default_boss_strategy = {'navy': 0, 'airforce': 0, 'army': 0}
        self.default_player_strategy = {'navy': 0, 'airforce': 0, 'army': 0}

    def test_hangman_right_default_values(self):
        self.assertEqual(self.lordgame.boss_victories, self.default_boss_victories)
        self.assertEqual(self.lordgame.player_victories, self.default_player_victories)
        self.assertDictEqual(self.lordgame.boss_strategy, self.default_boss_strategy)
        self.assertDictEqual(self.lordgame.player_strategy, self.default_player_strategy)

    def test_play(self):
        '''
        Testing case of finishing game
        '''
        self.lordgame.player_victories = 2
        self.assertEqual(self.lordgame.play(), 'Player')

        self.lordgame.reset_game()

        self.lordgame.boss_victories = 2
        self.assertEqual(self.lordgame.play(), 'Boss')

    @unittest.skip("For printing only: skipping")
    def test_screen(self):
        self.fail("It shouldn't happen")

    def test_category_analyzer(self):
        categories = ['navy', 'airforce', 'army']

        for category in categories:
            self.lordgame.boss_strategy[category] = 3
            self.lordgame.player_strategy[category] = 6
            self.assertEqual(self.lordgame.category_analyzer(category), 'Player won')
            self.lordgame.boss_strategy[category] = 4
            self.lordgame.player_strategy[category] = 3
            self.assertEqual(self.lordgame.category_analyzer(category), 'Boss won')
            self.lordgame.boss_strategy[category] = 7
            self.lordgame.player_strategy[category] = 7
            self.assertEqual(self.lordgame.category_analyzer(category), 'Draw game')

    def test_round_analyzer(self):
        self.lordgame.boss_strategy['navy'] = 3
        self.lordgame.player_strategy['navy'] = 6
        self.lordgame.boss_strategy['airforce'] = 3
        self.lordgame.player_strategy['airforce'] = 6
        self.lordgame.boss_strategy['army'] = 6
        self.lordgame.player_strategy['army'] = 6
        self.assertEqual(self.lordgame.round_analyzer(), 'Player')

        self.lordgame.boss_strategy['navy'] = 6
        self.lordgame.player_strategy['navy'] = 3
        self.lordgame.boss_strategy['airforce'] = 5
        self.lordgame.player_strategy['airforce'] = 3
        self.lordgame.boss_strategy['army'] = 6
        self.lordgame.player_strategy['army'] = 6
        self.assertEqual(self.lordgame.round_analyzer(), 'Boss')

        self.lordgame.boss_strategy['navy'] = 3
        self.lordgame.player_strategy['navy'] = 4
        self.lordgame.boss_strategy['airforce'] = 3
        self.lordgame.player_strategy['airforce'] = 1
        self.lordgame.boss_strategy['army'] = 5
        self.lordgame.player_strategy['army'] = 5
        self.assertEqual(self.lordgame.round_analyzer(), 'Draw')

    def test_reset_game(self):
        self.lordgame.boss_victories = 3
        self.lordgame.player_victories = 4
        self.lordgame.boss_strategy['navy'] = 3
        self.lordgame.boss_strategy['airforce'] = 4
        self.lordgame.boss_strategy['army'] = 5
        self.lordgame.player_strategy['navy'] = 6
        self.lordgame.player_strategy['airforce'] = 7
        self.lordgame.player_strategy['army'] = 8

        self.assertNotEqual(self.lordgame.boss_victories, self.default_boss_victories)
        self.assertNotEqual(self.lordgame.player_victories, self.default_player_victories)
        self.assertNotEqual(self.lordgame.boss_strategy, self.default_boss_strategy)
        self.assertNotEqual(self.lordgame.player_strategy, self.default_player_strategy)

        self.lordgame.reset_game()

        self.assertEqual(self.lordgame.boss_victories, self.default_boss_victories)
        self.assertEqual(self.lordgame.player_victories, self.default_player_victories)
        self.assertDictEqual(self.lordgame.boss_strategy, self.default_boss_strategy)
        self.assertDictEqual(self.lordgame.player_strategy, self.default_player_strategy)

    def test_finished(self):
        self.lordgame.player_victories = 2
        self.assertTrue(self.lordgame.finished())

        self.lordgame.reset_game()

        self.lordgame.boss_victories = 2
        self.assertTrue(self.lordgame.finished())

        self.lordgame.reset_game()

        self.assertFalse(self.lordgame.finished())


if __name__ == '__main__':
    unittest.main(verbosity=2)

