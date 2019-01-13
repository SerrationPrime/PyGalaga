import socket
from PyGalaga.main_game import  GameController
from .server_change_data import ServerChangeData
from .player_change_data import PlayerChangeData
from .beginning_data import BeginningData
from .network import *


class Server():
    def __init__(self, ip, port, nb_clients):
        self.ip = ip
        self.port = port
        self.nb_clients = nb_clients
        self.connections = []
        self.game_controller = GameController()

    def start_server(self):
        self.socket = socket.socket()
        self.socket.bind((self.ip, self.port))
        self.socket.listen(5)
        self.accept_connections()
        self.start_game()

    def accept_connections(self):
        while len(self.connections) < self.nb_clients:
            conn, addr = self.socket.accept()
            print('{} connected'.format(addr))
            beginning_data = BeginningData(len(self.connections),
                                           self.game_controller.players[len(self.connections)].location)
            send_command_to_socket(NetworkCommand(beginning_data), conn)
            self.connections.append(conn)

    #poziva svaki put kad se stanje na ekranu promeni(na 1/2 sekunde)
    def send_command(self, network_command):
        for conn in self.connections:
            send_command_to_socket(network_command, conn)

    def get_client_steps(self):
        for i in range(len(self.connections)):
            conn = self.connections[i]
            command = get_command_from_socket(conn) # preuzmi network_command poslat od strane klijenta
                                                    # data ce biti tipa PlayerChangedData
                                                    # odatle pokupim keys tog player-a i radim update za njega
            self.update_player(command.data.keys)

    def update_player(self, keys):
        self.game_controller.update_player(keys)

    def send_game_update(self):
        for i in range(len(self.connections)):
            conn = self.connections[i]
            changes = self.game_controller.collect_changes()
            # changes je tipa ServerChangeData
            send_command_to_socket(NetworkCommand(changes), conn)

    def start_game(self):
        #for i in range(len(self.connections)):
        #    conn = self.connections[i]
        #    command = get_command_from_socket(conn) # client_data
        while True:
            self.send_game_update()
            sleep(0.1)
            self.get_client_steps()
            sleep(0.2)
