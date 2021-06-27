import socket
PORT = 1234
SERVER_ADDRESS = socket.gethostbyname(socket.gethostname())
FULL_ADDRESS = (SERVER_ADDRESS, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(FULL_ADDRESS)

while True:
    message = client.recv(2048).decode("UTF-8")
    print(message)

