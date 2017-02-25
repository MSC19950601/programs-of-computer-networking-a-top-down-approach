from socket import *
serverName = 'localhost'
PORT = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, PORT))
sentence = raw_input('Input lowercase sentence')
clientSocket.send(sentence)
modifiedMessage = clientSocket.recv(1024)
print 'From server: ', modifiedMessage
clientSocket.close()
