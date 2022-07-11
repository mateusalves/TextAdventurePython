from time import sleep
import sys, select, os
import select


class Character():
    def __init__(self, name):
        self.name = name

    def talk(self, msg):
        print(f"[{self.name}]: ", end='')
        for char in msg:
            print(char, end='')
            sys.stdout.flush()
            sleep(0.05)
            if char in ['?', '.', '!']:
                sleep(0.4)
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                os.system('clear') #unix only
                _line = input()
                print(f"[{self.name}]: ", end='')
                print(msg, end='')
                break
        print('\n')
        sleep(1)

    def play(self):
        pass

    def win(self):
        pass

    def loose(self):
        pass


