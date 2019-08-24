import os
import sys
import json
import sqlite3
from sqlite3 import Error
import numpy as np
import multiprocessing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, render_template, send_file, send_from_directory
from flask import Flask, request, redirect, url_for, flash
from flask import jsonify, g
from flask import stream_with_context, request, Response
from werkzeug.utils import secure_filename
import gt_mon.serial_runner


current_directory = os.path.dirname(__file__)
gt_config = gt_mon.serial_runner.ImportConfig(path_to_config_file)
database_path = os.path.join(current_directory, ????)
path_to_config_file = os.path.join(current_directory, 'static','config.json')

UPLOAD_FOLDER = '/upload'
ALLOWED_EXTENSIONS = set('csv')
db_table_name = 'GT_MON'
db_row_name
app = Flask(__name__)
app.config.from_object(__name__)  # load config from this file , flaskr.py
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = '33'


#function for converting between numpy type array to a binary blob 
def adapt_array(arr):
    return arr.tobytes()

#function for converting between binary blob to numpy array
def convert_array(text):
    return np.frombuffer(text)


def init_database():
    db = None
    try:
        sqlite3.register_adapter(np.array, adapt_array)
        sqlite3.register_converter(db_row_name, convert_array)
        db = sqlite3.connect(database_path, isolation_level=None, detect_types=sqlite3.PARSE_DECLTYPES)
        return db
    except Error as e:
        print(e)
    return None


def read_freshest_entry_in_database(db):
    con = db.cursor()
    sql = ' SELECT * FROM ' + db_table_name + ' ORDER BY id DESC LIMIT 1 '
    con.execute(sql)
    readout = con.fetchone()
    con.close()
    return readout


def main():
    runner_process = gt_mon.serial_runner.SerialRunner(path_to_config_file)
    runner_process.daemon = True
    runner_process.start()

    app.run(debug=True, use_reloader=False)



if __name__ == "__main__":
    main()
