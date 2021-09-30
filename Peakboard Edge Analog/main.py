from datetime import datetime
import threading
from server import *
from raspberry import Raspberry

def main():
    time = datetime.now().strftime("%H:%M:%S")
    print(f"Started Peakboard Edge.\nStarttime : {time}")

    rpi = Raspberry()
    #input_read_thread = threading.Thread(target=rpi.begin_reading_inputs)

    # For Dev
    input_read_thread = threading.Thread(target=rpi.simulate_sensors)
    input_read_thread.start()

    data_server = DataServer(rpi)
    data_server_thread = threading.Thread(target=data_server.run)
    data_server_thread.start()

    data_server_thread.join()

    print("finished")
    
if __name__ == '__main__':
    main()