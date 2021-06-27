import socket
import threading
from max_14819 import Max14819
import time

class DataServer:
    
    # default constructor
    def __init__(self):
        self.running = False
        self.chips = []

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
            message = "connection accepted".encode("UTF-8")
            connection.send(message)
            handle_thread = threading.Thread(target=self.handle_Client, args=(connection, address))
            handle_thread.start()

    def handle_Client(self, connection, address):
        connected = True
        while connected:
            chip = self.chips[0]
            chip.port_value_changed_event.wait()
            
            for key in chip.changed_ports:
                message = f"Value of {key} changed to {chip.changed_ports[key]}".encode("UTF-8")
                connection.send(message)

            chip.reset_change_state()
            chip.port_value_changed_event.clear()

        connection.close();            

    def terminate(self):
        pass

    def register_Chip(self, chip: Max14819):  
        self.chips.append(chip)

class ManagementServer:
    pass

