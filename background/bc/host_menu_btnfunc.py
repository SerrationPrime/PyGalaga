import ctypes


def action_start_multi():
    ctypes.windll.user32.MessageBoxW(0, "You just lost... the game", "The Game", 1)
