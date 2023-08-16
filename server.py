# Author: Brendan Cook
# Date: 06/08/2023
# Description: Defines the functions used in the UI on the server side for the chat game.


from serverSocket import serverSocket
from connectFour import connectFour
import json

HOST = 'localhost'
PORT = 33345
SERVER = serverSocket(HOST, PORT)


def chat():
    """Defines the chat side for the client"""
    while True:
        # Receive message
        recv_message = SERVER.receive()
        if recv_message == "/q":
            SERVER.disconnect()
            print("Client has requested shut down. Shutting down!")
            break
        elif recv_message == "Connect 4":
            print("Client wants to play Connect 4")
            playGame()
            continue
        else:
            print(recv_message)

        # Get user input
        message = userInput()

        # Check user input for different messages
        if message == "Connect 4":
            SERVER.send(message)
            playGame()
            continue
        elif message == "/q":
            SERVER.send(message)
            print("Shutting down!")
            SERVER.disconnect()
            break
        else:
            SERVER.send(message)


def userInput():
    """Gets user input message and sends back to chat"""
    print("Enter message to send, type /q to quit or type 'Connect 4' to start a game.")
    print("Enter message > ", end="")
    message = input()
    return message

def playGame():
    """Defines the client side of the game"""
    numMoves = 0
    game = connectFour()
    game.welcome()
    game.display()
    print("Your character is 'O'")
    while True:
        # Receive message and check
        recv_message = SERVER.receive()
        if recv_message == 'win':
            print("Client wins!")
            print("Game over! Returning to chat!")
            print("Waiting for message...")
            break
        elif recv_message == '/q':
            print("Client has quit game. Returning to chat.")
            print("Waiting for message...")
            break
        else:
            board = json.loads(recv_message)
            numMoves += 1
            game.setBoard(board, numMoves)
            game.display()
            pass

        message = game.oMove()
        numMoves += 1
        # Check results of move
        if message == 'bad move':
            print("That column is full, please try again.")
            continue
        elif message == 'win':
            SERVER.send(message)
            print("Game over! Returning to chat!")
            print("Waiting for message...")
            break
        elif message == '/q':
            print("Quitting game! Returning to chat.")
            print("Waiting for message...")
            SERVER.send(message)
            break
        else:
            board, numMoves = game.getBoard()
            message = json.dumps(board)
            SERVER.send(message)


def main():
    connected = SERVER.connect()
    if connected:
        chat()


if __name__ == "__main__":
    main()