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
                self.player_strategy = {'navy': int(navy), 'airforce': (air), 'army': (army)}
                self.screen()
                print('\n\nRegistered')
                input("Press enter when you're ready to review...")
                self.screen(review_data=True)

                #TODO: create alrogithm to select randomly the boss strategy

            except Exception:
                print('When choosing your strategy, please inform the 3 numbers separated by space')
                print('Follow the order below')
                print('Please, try again...')


        if self.player_points == 2:
            victorious = 'player'
        else:
            victorious = 'boss'

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
