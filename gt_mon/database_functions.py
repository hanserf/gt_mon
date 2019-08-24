import sqlite3
import serial
import sys
import numpy as np
import multiprocessing
#import ino
import sqlite3
from  gt_mon.helper_functions import ResultStructure


#function for converting between numpy type array to a binary blob 
def adapt_array(arr):
    return arr.tobytes()

#function for converting between binary blob to numpy array
def convert_array(text):
    return np.frombuffer(text)


class DatabaseFunctions(object):
    def __init__(self,ImportConfig):
        self.database_config = ImportConfig
        self.database_name = database_config.database_name
        
    def init_database(self):
        db = None
        try:
            sqlite3.register_adapter(np.array, adapt_array)
            sqlite3.register_converter(db_row_name, convert_array)
            db = sqlite3.connect(database_config.database , isolation_level=None, detect_types=sqlite3.PARSE_DECLTYPES)
            return db
        except Error as e:
            print(e)
            return None

    def create_table(self,db):
        con = db.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS ' + self.database_config.table_name 
        sql2= ' (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp INT, ' + self.database_config.row_name[0] + 'REAL, '+ self.database_config.row_name[1] + 'REAL ); '
        con.execute(sql)
        db.commit()
        con.close()

    def read_freshest_entry_in_database(self,db):
        con = db.cursor()
        sql = ' SELECT * FROM ' + db_table_name + ' ORDER BY id DESC LIMIT 1 '
        con.execute(sql)
        readout = con.fetchone()
        con.close()
        return readout

    def put_in_database(self,db,ResultStructure):
        con = db.cursor()
        raw_dump = self.convert_array(ResultPackage.data_mean)
        sql = 'INSERT INTO ' + self.db_table_name + ' VALUES(?,?,?) '
        con.execute(sql,(None, ResultPackage.timestamp, raw_dump))
        con.close()
        db.commit()
