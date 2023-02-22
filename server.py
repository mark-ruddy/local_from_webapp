from flask import Flask
from launch_matlab import *

app = Flask(__name__)

@app.route('/')
def index():
    return "The launch matlab server is running here. Visit /launch_matlab to launch matlab"

@app.route('/launch_matlab')
def launch_matlab_api():
    launch_matlab_unix()
    return "Matlab should be launched"
