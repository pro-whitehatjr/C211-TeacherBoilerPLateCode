import socket
from  threading import Thread
from pynput.mouse import Button, Controller
from screeninfo import get_monitors
import autopy




SERVER = None
PORT = 8000
IP_ADDRESS = input("Enter your computer IP ADDR : ").strip()
screen_width = None
screen_height = None


mouse = Controller()



def getDeviceSize():
   






def acceptConnections():
    global SERVER

    while True:
        client_socket, addr = SERVER.accept()

        print(f"Connection established with {client_socket} : {addr}")

       


def setup():
    print("\n\t\t\t\t\t*** Welcome To Remote Mouse ***\n")


    global SERVER
    global PORT
    global IP_ADDRESS


    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...\n")

    
    acceptConnections()

setup()
