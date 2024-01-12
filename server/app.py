# app/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string_param>')
def print_string(string_param):
    print(string_param)
    return f'<p>String printed: {string_param}</p>'

@app.route('/count/<int_param>')
def count(int_param):
    numbers = '\n'.join(map(str, range(int_param + 1)))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation'

    return f'<p>Result of {num1} {operation} {num2} is: {result}</p>'

if __name__ == '__main__':
    app.run(port=5555)
