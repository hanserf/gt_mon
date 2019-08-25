import os
import sys
import json
import sqlite3
from sqlite3 import Error
import numpy as np
import multiprocessing
from flask import Flask, render_template, send_file, send_from_directory
from flask import Flask, request, redirect, url_for, flash
from flask import jsonify, g
from flask import stream_with_context, request, Response
from werkzeug.utils import secure_filename
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import serial_runner


current_directory = os.path.dirname(__file__)
path_to_config_file = os.path.join(current_directory, 'static','config.json')
with open(path_to_config_file) as config_file:
    gt_config = serial_runner.ImportConfig(config_file)
database_path = os.path.join(current_directory, gt_config.database)
print(database_path)



UPLOAD_FOLDER = '/upload'
ALLOWED_EXTENSIONS = set('csv')
db_table_name = 'GT_MON'
app = Flask(__name__)
app.config.from_object(__name__)  # load config from this file , flaskr.py
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = '33'

def main():
    runner_process = serial_runner.SerialRunner(gt_config)
    runner_process.daemon = True
    runner_process.start()

    app.run(debug=True, use_reloader=False)



if __name__ == "__main__":
    main()
