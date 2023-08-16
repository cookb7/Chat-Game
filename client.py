# Author: Brendan Cook
# Date: 06/08/2023
# Description: Defines the functions used in the UI on the client side for the chat game.


from clientSocket import clientSocket
from connectFour import connectFour
import json

HOST = 'localhost'
PORT = 33345
CLIENT = clientSocket(HOST, PORT)


def chat():
    """Defines the chat side for the client"""
    while True:
        # Get user input
        message = userInput()

        # Check user input for different messages
        if message == "Connect 4":
            CLIENT.send(message)
            playGame()
            continue
        elif message == "/q":
            CLIENT.send(message)
            print("Shutting down!")
            CLIENT.disconnect()
            break
        else:
            CLIENT.send(message)

        # Receive message
        recv_message = CLIENT.receive()
        if recv_message == "/q":
            CLIENT.disconnect()
            print("Server has requested shut down. Shutting down!")
            break
        elif recv_message == "Connect 4":
            print("Server wants to play Connect 4")
            playGame()
        else:
            print(recv_message)


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
    print("Your character is 'X'")
    while True:
        message = game.xMove()
        numMoves += 1
        # Check results of move
        if message == 'bad move':
            print("That column is full, please try again.")
            continue
        elif message == 'win':
            CLIENT.send(message)
            print("Game over! Returning to chat!")
            break
        elif message == '/q':
            print("Quitting game! Returning to chat.")
            CLIENT.send(message)
            break
        else:
            board, numMoves = game.getBoard()
            message = json.dumps(board)
            CLIENT.send(message)
        
        # Receive message and check
        recv_message = CLIENT.receive()
        if recv_message == 'win':
            print("Server wins!")
            print("Game over! Returning to chat!")
            break
        elif recv_message == '/q':
            print("Server has quit game. Returning to chat.")
            break
        else:
            board = json.loads(recv_message)
            numMoves += 1
            game.setBoard(board, numMoves)
            game.display()
            pass


def main():
    CLIENT.connect()
    chat()



if __name__ == "__main__":
    main()