from multiplayer_menu import *
from main_game import *


def action_signal_single():
    p = Process(target=initialize_game, args=[False])
    p.start()


def action_open_multi():
    p = Process(target=initialize_game, args=[True])
    p.start()