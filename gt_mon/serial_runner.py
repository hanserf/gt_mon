import time
import serial
import sys
import numpy as np
import multiprocessing
import sqlite3
from gt_mon.helper_functions import ImportConfig
from gt_mon.helper_functions import ResultStructure


class SerialRunner(multiprocessing.Process):
    def __init__(self, ImportConfig):
        super(SerialRunner, self).__init__()
        self.my_config = ImportConfig
        
        
    def run(self) -> None:
        port = self.my_config.port
        baudrate = self.my_config.baudrate
        ser = serial.Serial(port, baudrate, timeout=.1)
        time.sleep(1)
        print(ser.name)
        monitor = True
        while True:
            # Capture serial output as a decoded string
            val = str(ser.readline().decode().strip('\r\n'))
            val = val.split("/")
            # print()
            if(monitor == True):
                print(val, end="\r", flush=True)
