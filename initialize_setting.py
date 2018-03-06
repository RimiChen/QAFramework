####R Author information:
# Author: Yi-Chun Chen (RimiChen)
# Github original link: https://github.com/RimiChen/QAFramework
####

####R Descriptions:
# This file will initialize the framework settings, including:
# 1. create settings.json in setting folder,\
#    which contains variables to control interface can project paths
# 2. 
#
####


####R import libraries:
import sys
import os
from flask import Flask, flash, redirect, render_template, request, session, abort, send_file, send_from_directory
from file_functions import *

app = Flask(__name__)

####R URL routing:
## root directory:  /
@app.after_request
def add_header(r):
    ####
    # no cache
    ####
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

####R project loading page
@app.route("/")
def render_index():
    return render_template(
        'Index.html')

####R project file path
@app.route("/<path:path>")
def root_folder_file(path):
    return send_from_directory('/', path)

####R POST: chosen text file
@app.route('/folder_operation', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    input_file = jsdata
    file_function(jsdata)

    return jsdata    

####R app starts from here
if __name__ == "__main__":
    # record tool log for tracking the system
    app.run(host='0.0.0.0', port=int(sys.argv[1]))



