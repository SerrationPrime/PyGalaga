from PyGalaga.networking.client import Client
from PyGalaga.networking.network import *
from pygame import *
from PyGalaga.main_game import GameController
from PyGalaga.networking.player_change_data import PlayerChangeData


def get_keys():
    return key.get_pressed()


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 9999
    client = Client(ip, port)
    client.connect()
    gc = GameController()

    command = client.get_command()  # iz game_data dobijamo playerID i location
    gc.initialize_player(command.data.player_id, command.data.location)

    command = client.get_command()  # iz server_change_data dobijem :
                                    # enemy_coordinates
                                    # projectile_coordinates
                                    # player_projectile_coordinates
                                    # player_coordinates
                                    # player_lives

    gc.apply_changes(command.data)
    client.send_steps(NetworkCommand(PlayerChangeData(get_keys())))


