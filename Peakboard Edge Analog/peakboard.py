# simulates a peakboard connected to a peakboard edge analog box.
import socket
import threading

header = 64
port = 1234
format = "UTF-8"
disconnect_message = "!DISCONNECT"
server = "" # fill with ip address of rpi
addr = (server, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def send(msg):
    message = msg.encode(format)
    msg_length = len(message)
    send_length = str(msg_length).encode(format)
    send_length += b' ' * (header - len(send_length))
    client.send(send_length)
    client.send(message)

def listen():
    while True:
        print(client.revc(2048).decode(format))

t1 = threading.Thread(target=listen)
t1.start

send("12345")

t1.join()