import socket

# create listening socket from client
listening_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connect socket to port
listening_sock.bind(('127.0.0.1', 2000))

while True:
    # receive data from client
    client_data, client_address = listening_sock.recvfrom(1024)

    print('The client sent: ' + str(client_data) + " client address: " + str(client_address))

    # send message to client
    message = client_data
    listening_sock.sendto(message, client_address)

# close socket
listening_sock.close()
