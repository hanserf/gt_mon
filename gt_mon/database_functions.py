import sqlite3
import serial
import sys
import numpy as np
import multiprocessing
from sqlite3 import Error
from  helper_functions import ResultStructure
from helper_functions import ImportConfig


#function for converting between numpy type array to a binary blob 
def adapt_array(arr):
    return arr.tobytes()

#function for converting between binary blob to numpy array
def convert_array(text):
    return np.frombuffer(text)


class DatabaseFunctions(object):
    def __init__(self,ImportConfig):
        self.database_config = ImportConfig
        self.num_rows_in_config = len(self.database_config.db_rows)

    def init_database(self):
        db = None
        try:
            db = sqlite3.connect(self.database_config.database , isolation_level=None)
            return db
        except Error as e:
            print(e)
            return None

    def create_table(self,db):
        con = db.cursor()
        #See static/config.json
        sql = []
        sql.append('CREATE TABLE IF NOT EXISTS ' + self.database_config.table_name)
        sql.append(' ( ')
        sql.append(self.database_config.db_rows[0] + ' INTEGER PRIMARY KEY AUTOINCREMENT, ')
        sql.append(self.database_config.db_rows[1] + ' DATETIME, ')
        sql.append(self.database_config.db_rows[2] + ' INT , ')
        sql.append(self.database_config.db_rows[3] + ' TEXT , ')
        sql.append(self.database_config.db_rows[4] + ' REAL , ')
        sql.append(self.database_config.db_rows[5] + ' TEXT , ')
        sql.append(self.database_config.db_rows[6] + ' TEXT , ')
        sql.append(self.database_config.db_rows[7] + ' REAL , ')
        sql.append(self.database_config.db_rows[8] + ' REAL , ')
        sql.append('; ')
        print("Will create the following table:")
        print(sql)
        for query in sql:
            con.execute(query)

        db.commit()
        con.close()

    def read_freshest_entry_in_database(self,db):
        con = db.cursor()
        sql = ' SELECT * FROM ' + self.database_config.table_name + ' ORDER BY id DESC LIMIT 1 '
        con.execute(sql)
        readout = con.fetchone()
        con.close()
        return readout

    def put_in_database(self,db,ResultStructure):
        con = db.cursor()
        sql = []
        sql.append('INSERT INTO ' + self.database_config.table_name + ' VALUES(')
        for rows in self.num_rows_in_config:
            if rows == self.num_rows_in_config:
                sql.append('?')
            else:
                sql.append('?,')
        sql.append(' ) ')
        print('Number of rows in db :', self.num_rows_in_config)
        print("Will generate Table :")
        print(sql)
        res = []
        res.append(None)
        res.append(ResultStructure.datetime)
        res.append(ResultStructure.unixtime)
        res.append(ResultStructure.ds18b20_id)
        res.append(ResultStructure.temp)
        res.append(self.database_config.lamps)
        res.append(ResultStructure.light_states)
        res.append(ResultStructure.pwm_value)
        res.append(ResultStructure.power_consumption)

        con.execute(sql,res)
        con.close()
        db.commit()
