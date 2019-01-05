import ctypes


def action_hostgame():
    ctypes.windll.user32.MessageBoxW(0, "You just lost... the game", "The Game", 1)


def action_connectgame():
    ctypes.windll.user32.MessageBoxW(0, "You just lost... the game", "The Game", 1)
