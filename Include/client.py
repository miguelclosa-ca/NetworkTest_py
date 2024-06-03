import socket

HOST = '192.168.0.110'
PORT = 9996



socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Because we are connecting **connect** to the host and port
socket.connect((HOST,PORT))

socket.send(input().encode('utf-8'))
socket.recv(1024)

