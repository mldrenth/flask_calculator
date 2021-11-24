from flask import render_template
from app import app
from modules.calculator import *

@app.route('/add/<number_1>/<number_2>')
def add_numbers(number_1,number_2):
    return render_template('index.html', result = add(int(number_1),int(number_2)))

@app.route('/subtract/<number_1>/<number_2>')
def subtract_numbers(number_1,number_2):
    return render_template('index.html', result = subtract(int(number_1),int(number_2)))

@app.route('/multiply/<number_1>/<number_2>')
def multiply_numbers(number_1,number_2):
    return render_template('index.html', result = multiply(int(number_1),int(number_2)))

@app.route('/divide/<number_1>/<number_2>')
def divide_numbers(number_1,number_2):
    return render_template('index.html', result = divide(int(number_1),int(number_2)))