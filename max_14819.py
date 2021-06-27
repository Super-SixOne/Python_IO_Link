import threading
import random
import time

class Max14819:

    # default constructor
    def __init__(self, spi_address):
        self.spi_address = spi_address
        self.port_value_changed_event = threading.Event()
        self.port_values = {"P0": "0", "P1": "0"}
        self.changed_ports = {}

    def configure_sio_mode(self):
        pass

    def get_port_values(self):
        pass

    def set_port_values(self):
        pass

    def begin_reading_ports(self):
        # trigger event each time an input value has changed.
        print("starting to read port values...")
        # randomly decide if port value has changed.
        while(True):
            time.sleep(1)
            decider = random.randint(0,5)
            if(decider == 1):
                port = random.randint(0,1)
                if(port == 0):
                    value = self.port_values.get("P0")
                    if value == "0":
                        self.port_values["P0"] = "1"
                    else:
                        self.port_values["P0"] = "0"
                    self.changed_ports["P0"] = self.port_values["P0"]
                    self.port_value_changed_event.set()
                else:
                    value = self.port_values.get("P1") 
                    if value == "0":
                        self.port_values["P1"] = "1"
                    else:
                        self.port_values["P1"] = "0"

                    self.changed_ports["P1"] = self.port_values["P1"]
                    self.port_value_changed_event.set() 
        
    def reset_change_state(self):
        self.changed_ports.clear()
