from flask import Flask, render_template
from data import *

app = Flask(__name__)

from data.data import peoples
from utils.random_matching import random_matching

Peoples = peoples()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/matching')
def result():
    return render_template('result.html', peoples=random_matching(Peoples, 5))


if __name__ == '__main__':
    app.run(debug=True)
