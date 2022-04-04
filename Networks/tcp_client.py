import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 2000        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))     # connect to the server on local computer

s.sendall(b'Hello, world')  # send message to server

data = s.recv(1024)         # receive message from server

print('Received', str(data))

s.close()
