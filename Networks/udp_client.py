import socket

"""
we will create an socket object
when we use UDP connection we need 
at the second parameter select SOCK_DGRAM
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data to server
server_address = ("127.0.0.1", 2000)
sock.sendto(b'Hi', server_address)

# receive the data from the server
data, remote_address = sock.recvfrom(1024)

print('The server sent: ' + str(data))

while True:

    message = input("Enter a message: ")
    sock.sendto(message.encode('utf-8'), server_address)

    receive_data = sock.recv(1024)
    print(str(receive_data))

# close the socket object
sock.close()
