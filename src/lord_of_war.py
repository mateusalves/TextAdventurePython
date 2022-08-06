from random import randint, choice
from time import sleep
import string
import os


class LordOfWar():

    def __init__(self):
        self.reset_game()

    def play(self):
        self.screen()
        while not self.finished():
            try:
                navy, air, army = input("\n\nEnter your strategy separated by space > ").split()
                self.player_strategy = {'navy': int(navy), 'airforce': int(air), 'army': int(army)}
                self.screen()

                if (int(navy) + int(air) + int(army)) != 100:
                    print('\n\nYou must select exactly 100 soldiers to your forces')
                    continue

                print('\n\nRegistered')
                self.boss_strategy_generator()
                print('Boss is ready for battle')
                print('Get ready...')
                sleep(3)
                self.screen(review_data=True)

            except Exception as e:
                print('When choosing your strategy, please inform the 3 numbers separated by space')
                print('Follow the order in the screen')
                print('Please, try again...')

        if self.player_victories == 2:
            victorious = 'Player'
        else:
            victorious = 'Boss'

        self.screen(winner=victorious)
        return victorious

    def screen(self, review_data=False, winner=None):
        os.system('clear')
        print('''
                                  Navy                               Airforce                           Army

                                 __/___                                 |                               _____
                           _____/______|                            __-/_\-___                  !      /-----\============@
                   _______/_____\_______\_____          _____________/( . )\_____________       |_____/_______\_____
                   \              < < <       |        *    |    |  (  \_/  )  |    |    *     /____________________\\
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         *|*  *|*  \_-+-_/  *|*  *|*          \+__+__+__+__+__+__*/\n\n''')
        if not winner:
            print('Boss strategy:\t\t\t%s\t\t\t\t%s\t\t\t\t%s' %
                  (str(self.boss_strategy['navy']).zfill(2) if review_data else '**',
                   str(self.boss_strategy['airforce']).zfill(2) if review_data else '**',
                   str(self.boss_strategy['army']).zfill(2) if review_data else '**'))
            print('Player strategy:\t%s\t\t\t\t%s\t\t\t\t%s' %
                  (str(self.player_strategy['navy']).zfill(2) if review_data else '**',
                   str(self.player_strategy['airforce']).zfill(2) if review_data else '**',
                   str(self.player_strategy['army']).zfill(2) if review_data else '**'))

            if(review_data):
                sleep(3)
                print('\t\t     %s Won\t\t\t     %s Won\t\t\t     %s Won' %
                      ('Player' if (0) else 'Boss',
                      'Player' if (1) else 'Boss',
                      'Player' if (1) else 'Boss'))
                sleep(3)
                print('')
        else:
            pass

    def reset_game(self):
        self.boss_victories = 0
        self.player_victories = 0
        self.boss_strategy = {'navy': 0, 'airforce': 0, 'army': 0}
        self.player_strategy = {'navy': 0, 'airforce': 0, 'army': 0}

    def boss_strategy_generator(self):
        guess = choice(string.ascii_letters)
        # guess = choice(self.secret_word) #op boss
        if guess in self.chosen_letters:
            return self.boss_guess()
        return guess

    def finished(self):
        if self.boss_victories >= 2 or self.player_victories >= 2:
            return True
        else:
            return False


if __name__ == "__main__":
    war_game = LordOfWar()
    war_game.play()
