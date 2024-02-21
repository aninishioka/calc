from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# TODO: use variable to get op

@app.get('/add')
@app.get('/math/add')
def add_nums():
    """Return sum of a and b (from query string)."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{add(a,b)}"

@app.get('/sub')
@app.get('/math/sub')
def subtract_nums():
    """Return difference of a and b (from query string)."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{sub(a,b)}"

@app.get('/mult')
@app.get('/math/mult')
def multiply_nums():
    """Return product of a and b (from query string)."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{mult(a,b)}"

@app.get('/div')
@app.get('/math/div')
def divide_nums():
    """Return division of a and b (from query string)."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{div(a,b)}"