from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    version = sys.version
    return f'Hello, python version: {version}'
