import ctypes


def action_signal_single():
    ctypes.windll.user32.MessageBoxW(0, "You just lost... the game", "The Game", 1)


def action_open_multi():
    ctypes.windll.user32.MessageBoxW(0, "You just lost... the game", "The Game", 1)
