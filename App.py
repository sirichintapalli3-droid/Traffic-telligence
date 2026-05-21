from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
