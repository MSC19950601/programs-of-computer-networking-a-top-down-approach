from socket import *

PORT = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', PORT))
print "The server is ready to receive"
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = bytes.upper(message)
    serverSocket.sendto(modifiedMessage, clientAddress)
