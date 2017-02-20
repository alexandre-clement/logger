from main import *
from main.keystroke import printer, press
from main.log import my_log


class Game:
    def __init__(self, path, name):
        self.name = name
        self.path = path


def la_ligue_des_légendes(log):
    game = Game(r"C:/Rito Gaming/La Ligue des Légendes", "LigueLyncheur.exe")
    os.chdir(game.path)
    run(game.name)
    time.sleep(15)
    printer(log.pseudo)
    press("tab")
    printer(log.password)
    press("enter")


if __name__ == '__main__':
    la_ligue_des_légendes(my_log)
