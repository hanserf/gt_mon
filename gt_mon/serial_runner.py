import time
import serial
import sys
import numpy as np
import multiprocessing
import sqlite3
from helper_functions import ImportConfig
from helper_functions import ResultStructure
import re


class SerialRunner(multiprocessing.Process):
    def __init__(self, ImportConfig):
        super(SerialRunner, self).__init__()
        self.my_config = ImportConfig

    def run(self) -> None:
        #Init Serial Port
        port = self.my_config.port
        baudrate = self.my_config.baudrate
        ser = serial.Serial(port, baudrate, timeout=.1)
        time.sleep(1)
        monitor = True
        print(ser.name)
        #Init Logger
        num_sensors = int(self.my_config.num_sensors)
        num_lights = int(self.my_config.num_lights)
        ds18b20_list = []
        lights_list = []
        lights_state_list = []
        pwm_values = []

        for i in range(num_sensors):
            ds18b20_list.append(self.my_config.row_name[i])

        for i in range(num_lights) :
            lights_list.append(self.my_config.led[i])
            lights_state_list.append(self.my_config.light_states[i])
        print(ds18b20_list)
        print(lights_list)
        print(lights_state_list)
        while True:
            # Capture serial output as a decoded string
            val = str(ser.readline().decode().strip('\r\n'))
            if(monitor == True):
                print(val) #Prints live terminal data