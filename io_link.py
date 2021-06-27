from datetime import datetime
import threading
from max_14819 import Max14819
from server import DataServer
from server import ManagementServer

def main():
    time = datetime.now().strftime("%H:%M:%S")
    print(f"Started Peakboard Edge IO Link.\nStarttime : {time}")

    # Configure MAX14819 chip to operate sensor in SIO mode.
    chip = Max14819(0)
    chip.configure_sio_mode()
    input_read_thread = threading.Thread(target=chip.begin_reading_ports)
    input_read_thread.start()

    # TODO: Initialize management server in new thread

    # Initialize data server in new thread
    data_server = DataServer()
    data_server.register_Chip(chip)
    data_server_thread = threading.Thread(target=data_server.run)
    data_server_thread.start()

    data_server_thread.join()

    print("finished.")


if __name__ == '__main__':
    main()