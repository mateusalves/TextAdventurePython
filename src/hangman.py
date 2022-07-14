from random import randint
import os


class HangMan():
    def __init__(self, lang='pt_br'):
        self.body_parts = {'head': 'O', 'l_arm': '/', 'r_arm': '\\',
                           'body':  '|', 'l_leg': '/', 'r_leg': '\\'}
        self.lang = lang
        self.reset_game()

    def screen(self):
        # print("\n\t\tYour turn\n")
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
            print((len(self.secret_word) - 1) * '__ ')

        else:
            for letter in self.secret_word:
                if letter in self.guessed_letters:
                    print(f'{letter} ', end='')
                else:
                    print('__ ', end='')

        print('\n\n\n\tAlready chosen: ', end='')
        print(*self.chosen_letters, sep=", ")
        print('\n\n')


    def reset_game(self):
        self.secret_word = self.choose_random_word()
        print(self.secret_word)
        self.guessed_letters = []
        self.chosen_letters = []
        self.mistakes = 0

    def guess(self, letter):
        if letter in self.chosen_letters:
            print('This letter was already chosen. Please, guess another one.')
            return

        self.chosen_letters.append(letter)

        if letter in self.secret_word:
            self.guessed_letters.append(letter)
        else:
            self.mistakes += 1

    def finished(self):
        pass

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


if __name__ == "__main__":
    hgm = HangMan()
    hgm.screen()
    hgm.guess('a')
    hgm.screen()
    hgm.guess('k')
    hgm.screen()
    hgm.guess('k')
    hgm.screen()
