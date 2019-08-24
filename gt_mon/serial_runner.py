import time
import serial
import sys
import numpy as np
import multiprocessing
#import ino
import json

class ImportConfig(object):
    def __init__(self, config):
        self.__dict__ = json.loads(config)


class SerialRunner(multiprocessing.Process):
    def __init__(self, config_file_path,ImportConfig):
        super(SerialRunner, self).__init__()
        self.config_file = config_file_path
        self.my_config = ImportConfig
        
        
    def run(self) -> None:
        port = self.my_config.port
        baudrate = self.my_config.serialbaudrate
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
