class HangMan():

    def __init__(self):
        # TODO: escolher a palavra aleatoriamente de acordo com o input do user
        # TODO: Vai ser melhor de 3?
        self.body_parts = {'head': 'O', 'l_arm': '/', 'r_arm': '\\',
                           'body':  '|', 'l_leg': '/', 'r_leg': '\\'}
        self.mistakes = 6
        self.secret_word = 'test'
        self.guessed_letters = ['t', 'e', '']
        self.chosen_letters = ['e', 't', 'M', 'x', 'i']

    def screen(self):
        print("\n\t\tYour turn\n")
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
            print(len(self.secret_word) * '__ ')

        for letter in self.secret_word:
            if letter in self.guessed_letters:
                print(f'{letter} ', end='')
            else:
                print('__ ', end='')
        print('\n\n\n\tAlready chosen: ', end='')
        print(*self.chosen_letters, sep=", ")


    def reset_game(self):
        # TODO: Vai ser melhor de 3?
        # TODO: escolher nova palavra e zerar mistakes e outras variaveis
        self.secret_word = 'test'
        self.guessed_letters = []
        self.chosen_letters = []
        self.mistakes = 0
        pass

    def finished(self):
        pass

    def choose_random_word(self, lang):
        if lang == 'pt_br':
            pass
            # with open(text, 'r') as f:
            #     lines = f.readlines()
            #     f.close()


if __name__ == "__main__":
    hgm = HangMan()
    hgm.screen()

