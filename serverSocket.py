# Author: Brendan Cook
# Date: 06/08/2023
# Description: Defines the class used by the server side to control the socket.


import socket


BUFFER_SIZE = 4096  # Max number of bytes that can be sent or received


class serverSocket:
    """Create the socket for the server and defines common functions needed."""
    def __init__(self, host, port):
        """Initiates variables needed for the socket. Takes host and port as arguments."""
        self._host = host
        self._port = port
        self.socket = None
        self._client_socket = None
        self._client_address = None

    def connect(self):
        """Connects to the client socket and sets option for server socket."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self._host, self._port))
        self.socket.listen(1)
        print(f"Server listening on: {self._host} on port: {self._port}")
        self._client_socket, self._client_address = self.socket.accept()
        print(f"Connected by {self._client_address}")
        print("Waiting for message...")
        return True

    def send(self, message):
        """Sends the user input to the client. Takes a string as an argument for message."""
        encoded_data = message.encode()
        if self._client_socket and len(encoded_data) < BUFFER_SIZE:
            self._client_socket.sendall(encoded_data)
        elif encoded_data > BUFFER_SIZE:
            print("Error: Unable to send message. Message is too long.")
        else:
            print("Error: Unable to send message")

    def receive(self):
        """Receives message from the client"""
        if self._client_socket:
            message = self._client_socket.recv(BUFFER_SIZE)
            return message.decode()
        else:
            print("Error: Unable to receive message")

    def disconnect(self):
        """Closes the socket"""
        if self.socket:
            self.socket.close()
            self.socket = None
        else:
            print("Error: Unable to close socket")