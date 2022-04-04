import socket

# create listening socket from client
listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect socket to port
listening_sock.bind(('127.0.0.1', 2000))

# put the socket into listening mode
listening_sock.listen()

while True:

    # Establish connection with client.
    connection, address = listening_sock.accept()

    # receive data from client
    client_data = connection.recv(1024)

    print('The client sent: ' + str(client_data) + " client address: " + str(address))

    # send message to client
    connection.sendall(b'Hello')

# close socket
listening_sock.close()
