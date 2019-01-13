import socket
from PyGalaga.networking.network import *

class Client:
    def __init__(self, ip, port):
        self.host = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.ip, self.port))

    def get_command(self):
        return get_command_from_socket(self.socket)

    # send player change data
    def send_steps(self, keys):
        send_command_to_socket(NetworkCommand(keys), self.socket)
        # NetworkCommand.data je tipa PlayerChangeData