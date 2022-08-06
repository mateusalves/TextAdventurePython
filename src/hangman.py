from random import randint, choice
from time import sleep
import string
import os


class HangMan():

    def __init__(self, lang='pt_br', starter='player'):
        self.body_parts = {'head': 'O', 'l_arm': '/', 'r_arm': '\\',
                           'body':  '|', 'l_leg': '/', 'r_leg': '\\'}
        self.lang = lang
        self.currently_playing = starter
        self.reset_game()

    def play(self):
        while not self.finished():
            self.screen()

            if self.currently_playing == 'player':
                result = self.guess(input('Take a guess > ').upper())
                if result is None:
                    continue
                elif result is True:
                    self.player_points += 1
                else:
                    self.player_points -= 0 if self.player_points == 0 else 1

                self.currently_playing = 'boss'
            else:
                boss_guess = self.boss_guess()
                print('Boss guess > ', end='', flush=True)
                sleep(2)
                print(boss_guess)

                result = self.guess(boss_guess.upper())
                if result is None:
                    continue
                elif result is True:
                    self.boss_points += 1
                else:
                    self.boss_points -= 0 if self.boss_points == 0 else 1

                self.currently_playing = 'player'

        if self.player_points > self.boss_points:
            victorious = 'player'
        elif self.player_points < self.boss_points:
            victorious = 'boss'
        else:
            print('Draw')
            victorious = 'draw'

        self.screen()
        return victorious

    def screen(self):
        os.system('clear')
        print(f'\t\tIt is the {self.currently_playing} turn')
        print("\t   _____      \n"
              "\t  |     |     \n"
              "\t  |     %s    \n"
              "\t  |    %s%s%s \n"
              "\t  |    %s %s  \n"
              "\t  |           \n"
              "\t__|__           " %
              (self.body_parts['head'] if (self.mistakes > 0) else ' ',
              self.body_parts['l_arm'] if (self.mistakes > 2) else ' ',
              self.body_parts['body'] if (self.mistakes > 1) else ' ',
              self.body_parts['r_arm'] if (self.mistakes > 3) else ' ',
              self.body_parts['l_leg'] if (self.mistakes > 4) else ' ',
              self.body_parts['r_leg'] if (self.mistakes > 5) else ' '), end='')

        if not self.guessed_letters:
            print((len(self.secret_word)) * '__ ')
        else:
            for letter in self.secret_word:
                if letter in self.guessed_letters:
                    print(f'{letter} ', end='')
                else:
                    print('__ ', end='')

        print('\n\n\n\tAlready chosen: ', end='')
        print(*self.chosen_letters, sep=", ")
        print('\n\n')
        print(f'\tPlayer points: {self.player_points}')
        print(f'\tBoss points: {self.boss_points}\n')

    def reset_game(self):
        self.secret_word = self.choose_random_word().replace("\n", "").upper()
        # print(self.secret_word)
        self.player_points = 0
        self.boss_points = 0
        self.guessed_letters = []
        self.chosen_letters = []
        self.mistakes = 0

    def guess(self, letter):
        if letter in self.chosen_letters:
            print('This letter was already chosen. Please, guess another one.')
            return None

        self.chosen_letters.append(letter)

        if letter in self.secret_word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.mistakes += 1
            return False

    def boss_guess(self):
        guess = choice(string.ascii_letters)
        # guess = choice(self.secret_word) #op boss
        if guess in self.chosen_letters:
            return self.boss_guess()
        return guess

    def choose_random_word(self):
        if self.lang == 'pt_br':
            with open('../words_pt.txt', 'r') as f:
                lines = f.readlines()
                f.close()
        else:
            with open('../words_en.txt', 'r') as f:
                lines = f.readlines()
                f.close()
        return lines[randint(0, len(lines)-1)]

    def finished(self):
        if set(self.guessed_letters) == set(list(self.secret_word)):
            return True
        if self.mistakes == 6:
            return True
        else:
            return False


if __name__ == "__main__":
    hgm = HangMan()
    hgm.play()
