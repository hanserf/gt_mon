import time
import numpy as np
import multiprocessing

class SerialRunner(multiprocessing.Process):
    def __init__(self, config_file_path):
        super(SerialRunner, self).__init__()
        
    def run(self) -> None:
        print("Serial port runner initialized")      
        time.sleep(1)


