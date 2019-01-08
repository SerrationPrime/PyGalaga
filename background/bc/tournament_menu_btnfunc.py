import ctypes


def action_create_tournament():
    ctypes.windll.user32.MessageBoxW(0, "You just lost... the game", "The Game", 1)


def action_join_tournament():
    ctypes.windll.user32.MessageBoxW(0, "You just lost... the game", "The Game", 1)
