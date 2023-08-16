# Author: Brendan Cook
# Date: 06/08/2023
# Description: Defines the class used by the client side to control the socket.


import socket


BUFFER_SIZE = 4096  # Max number of bytes that can be sent or received


class clientSocket:
    """Create the socket for the client and defines common functions needed."""
    def __init__(self, host, port):
        """Initiates variables needed for the socket. Takes host and port as arguments"""
        self._host = host
        self._port = port
        self.socket = None
    
    def connect(self):
        """Creates and connects the socket to the server."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self._host, self._port))
        print(f"Client connected to {self._host}:{self._port}")

    def send(self, message):
        """Sends the user input to the server. Takes a string as an argument for message."""
        encoded_data = message.encode()
        if self.socket and len(encoded_data) < BUFFER_SIZE:
            self.socket.sendall(encoded_data)
        elif encoded_data > BUFFER_SIZE:
            print("Error: Unable to send message. Message is too long.")
        else:
            print("Error: Unable to send message")
    
    def receive(self):
        """Receives message from the server"""
        if self.socket:
            message = self.socket.recv(BUFFER_SIZE)
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