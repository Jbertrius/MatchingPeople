from flask import Flask, render_template
from data import *

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('home.html')


@app.route('/matching')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
