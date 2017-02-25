from socket import *
serverName = 'localhost'
PORT = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', PORT))
serverSocket.listen(1)
print "The server is ready to receive"
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = bytes.upper(sentence)
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()