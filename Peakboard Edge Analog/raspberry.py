import threading
import random
import time

class Raspberry:
    def __init__(self):
        self.input_value_changed_event = threading.Event()
        self.input_values = {"IN0": "0", "IN1": "0", "IN2": "0", "IN3": "0"}
        self.changed_inputs = []

    def begin_reading_inputs(self):
        #Hardware SPI configuration
        SPI_PORT = 0
        SPI_DEVICE = 0
        mcp = Adafruit_MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

        while(True):
            for i in range(4):
                input_value = str(mcp.read_adc(i))
                if self.input_values.get(f"IN{i}") != input_value:
                    self.input_values[f"IN{i}"] = input_value
                    self.changed_inputs.append(ValueChange(str(i), input_value))
                    self.input_value_changed_event.set()

    # method to simulate input when not connected to a real sensor. Use only for developement.
    def simulate_sensors(self):
        print("starting to read input values")

        wait_time = 0
        while(True):
            time.sleep(wait_time)
            wait_time = random.randint(1,25)

            # deciders
            input_decider = str(random(0,3))
            value_decider = str(random(0,1024))

            if self.input_values.get(f"IN{input_decider}") != value_decider:
                #update
                self.input_values[f"IN{input_decider}"] = value_decider
                self.changed_inputs.append(ValueChange(input_decider, value_decider))

                #trigger event
                self.input_value_changed_event.set()

    def report(self):
        json = "{"
        requires_comma = False
        for change in changed_inputs:
            pair = f"\"{change.input}\": \"{change.value}\""
            json += pair
            if requires_comma:
                json += ","
            requires_comma = True
        
        json += "}"

        return json

    def reset(self):
        self.changed_inputs.clear()

# class representing the information of a value changed event
class ValueChange:
    def __init__(self, i, v):
        self.input = i
        self.value = v