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
              _______  __  .__   __.      ___       __         .______        ___   .___________.___________. __       _______
             |   ____||  | |  \ |  |     /   \     |  |        |   _  \      /   \  |           |           ||  |     |   ____|
             |  |__   |  | |   \|  |    /  ^  \    |  |        |  |_)  |    /  ^  \ `---|  |----`---|  |----`|  |     |  |__
             |   __|  |  | |  . `  |   /  /_\  \   |  |        |   _  <    /  /_\  \    |  |        |  |     |  |     |   __|
             |  |     |  | |  |\   |  /  _____  \  |  `----.   |  |_)  |  /  _____  \   |  |        |  |     |  `----.|  |____
             |__|     |__| |__| \__| /__/     \__\ |_______|   |______/  /__/     \__\  |__|        |__|     |_______||_______|''')
        print(f'\n\n\t\tBoss {"V " * self.boss_victories}', end='')
        print(f'\t\t\t\t\t\t\t\t\t\t\t\t{"V " * self.player_victories} Player\n')
        print('''
                                  Navy                               Airforce                           Army

                                 __/___                                 |                               _____
                           _____/______|                            __-/_\-___                  !      /-----\============@
                   _______/_____\_______\_____          _____________/( . )\_____________       |_____/_______\_____
                   \              < < <       |        *    |    |  (  \_/  )  |    |    *     /____________________\\
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         *|*  *|*  \_-+-_/  *|*  *|*          \+__+__+__+__+__+__*/\n\n''')
        if not winner:
            print('Boss strategy:\t\t\t%s\t\t\t\t\t%s\t\t\t\t%s' %
                  (str(self.boss_strategy['navy']).zfill(2) if review_data else '**',
                   str(self.boss_strategy['airforce']).zfill(2) if review_data else '**',
                   str(self.boss_strategy['army']).zfill(2) if review_data else '**'))
            print('Player strategy:\t\t%s\t\t\t\t\t%s\t\t\t\t%s' %
                  (str(self.player_strategy['navy']).zfill(2) if review_data else '**',
                   str(self.player_strategy['airforce']).zfill(2) if review_data else '**',
                   str(self.player_strategy['army']).zfill(2) if review_data else '**'))

            if(review_data):
                sleep(3)
                print('\t\t\t     %s\t\t\t\t     %s\t\t\t     %s' %
                      (self.category_analyzer('navy'),
                       self.category_analyzer('airforce'),
                       self.category_analyzer('army')))
                sleep(3)
                round_winner = self.round_analyzer()
                if round_winner == 'Draw':
                    print('\n\n\t\t\t\t\t\t\t\t     **Draw game.**')
                    print('This round will not be counted.')
                else:
                    print(f'\n\n\t\t\t\t\t\t\t     **{round_winner} won this round.**')
                sleep(3)
                self.screen()
        else:
            print(f'\t\t\t\t\t\t\t    {winner} is the Lord of War.\n\n')

    def category_analyzer(self, category):
        if self.player_strategy[category] > self.boss_strategy[category]:
            category_winner = 'Player won'
        elif self.player_strategy[category] < self.boss_strategy[category]:
            category_winner = 'Boss won'
        else:
            category_winner = 'Draw game'
        return category_winner

    def round_analyzer(self):
        round_winner = ''
        player_round_victories = 0
        boss_round_victories = 0
        categories = ['navy', 'airforce', 'army']

        for category in categories:
            category_winner = self.category_analyzer(category)
            if category_winner == 'Player won':
                player_round_victories += 1
            elif category_winner == 'Boss won':
                boss_round_victories += 1
            else:
                #draw does not compute
                pass

        if player_round_victories > boss_round_victories:
            round_winner = 'Player'
            self.player_victories += 1
        elif player_round_victories < boss_round_victories:
            round_winner = 'Boss'
            self.boss_victories += 1
        else:
            round_winner = 'Draw'

        return round_winner

    def reset_game(self):
        self.boss_victories = 0
        self.player_victories = 0
        self.boss_strategy = {'navy': 0, 'airforce': 0, 'army': 0}
        self.player_strategy = {'navy': 0, 'airforce': 0, 'army': 0}

    def boss_strategy_generator(self):
        navy = randint(0, 100)
        airforce = randint(0, 100 - navy)
        army = 100 - navy - airforce
        self.boss_strategy = {'navy': navy, 'airforce': airforce, 'army': army}

    def finished(self):
        if self.boss_victories >= 2 or self.player_victories >= 2:
            return True
        else:
            return False


if __name__ == "__main__":
    war_game = LordOfWar()
    war_game.play()

