
# https://youtu.be/YwWfKitB8aA

import socket

host = socket.gethostbyname(socket.gethostname())
HOST = '192.168.0.110'
PORT = 9996

# Define an internet socket (AF_INET)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Because we are hosting, **bind** the host and port
server.bind((HOST, PORT))

server.listen(5)

while True:
    communicationSocket, address = server.accept()
    print("Connected to {} " .format(address))
    msg = communicationSocket.recv(1024).decode('utf-8')
    print("{} Said: {}" .format(address, msg))
    communicationSocket.send("Received".encode('utf-8'))

    # communicationSocket.close()
    # print("Ended communication with {}".format(address))