from socket import *
serverName = 'localhost'
PORT = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = raw_input('Input lowercase sentence:')
    clientSocket.sendto(message, (serverName, PORT))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print modifiedMessage
clientSocket.close()