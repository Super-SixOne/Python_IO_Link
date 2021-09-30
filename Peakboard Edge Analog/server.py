import socket
import threading
import time
import raspberry

class DataServer:
    
    def __init__(self, rpi):
        self.header = 64
        self.format = "UTF-8"
        self.password = "12345"
        self.disconnect_message = "!DISCONNECT"
        self.running = False
        self.raspberry = rpi

    def run(self):
        print("starting data server...")
        port = 1234
        server_address = socket.gethostbyname(socket.gethostname())
        full_address = (server_address, port)
        print(f"ip address: {server_address}:{port}")

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        server.bind(full_address)
        server.listen()
        print("listening...")
        self.running = True

        while self.running:
            connection, address = server.accept()
            print(f"new client with address: {address}")

            #message = "connected".encode(self.format)
            #connection.send(message)
            handle_thread = threading.Thread(target=self.handle_Client, args=(connection, address))
            handle_thread.start()

    def handle_Client(self, connection, address):
        connected = True
        data_thread = None

        while connected:
            message_length = int(connection.recv(self.header).decode(self.format))
            if message_length:    
                message = connection.recv(message_length).decode(self.format)
                print(message)
                if message == self.disconnect_message:
                    connected = False
                    continue

                if message != password
                    connection.send("access denied!").encode(self.format)
                else:
                    connection.send("access granted!").encode(self.format)
                    data_thread = threading.Thread(target=self.data_Sender, args=(connection, address))
                    data_thread.start()

        connection.send("closing connection...").encode(self.format)        
        connection.close()           

    def data_Sender(self, connection, address):
        while True:
            self.raspberry.input_value_changed_event.wait()

            connection.send(self.raspberry.report().encode(self.format))
            self.raspberry.reset()
            self.raspberry.input_value_changed_event.clear()

class InfoServer:
    def __init__(self):
        self.running = False

    def run(self):
        pass