import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8003))

data = input()
client_socket.sendall(data.encode())

modified_data = client_socket.recv(1024).decode()
print('Received modified data:', modified_data)

client_socket.close()