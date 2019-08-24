import time
import numpy as np
import multiprocessing
import ino 


class SerialRunner(multiprocessing.Process):
    def __init__(self, config_file_path):
        super(SerialRunner, self).__init__()
        
    def run(self) -> None:
                
        while True :
            print("Serial port runner initialized")      
            time.sleep(1)


