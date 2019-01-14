import ctypes
from multiplayer_menu import *


def action_start_multi():
    ctypes.windll.user32.MessageBoxW(0, "You just lost... the game", "The Game", 1)


def action_back_to_multi():
    multiplayer_menu()
