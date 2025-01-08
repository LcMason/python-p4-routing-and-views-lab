#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<parameter>")
def print_message(parameter):
    print(parameter)
    return parameter

@app.route("/count/<int:parameter>")
def count(parameter):
    result = "\n".join(str(i) for i in range(parameter)) + "\n"
    return result

@app.route("/math/<int:x>/<op>/<int:y>")
def math(x, op, y):
    if op == '+':
        return str(x + y)
    elif op == '-':
        return str(x - y)
    elif op == '*':
        return str(x * y)
    elif op == 'div':
        return str(x / y)
    elif op == '%':
        return str(x % y)
    else:
        return "Unsupported operator"






if __name__ == '__main__':
    app.run(port=5555, debug=True)

