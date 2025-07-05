from flask import Flask, request, jsonify
app = Flask(__name__)

history=[]

@app.route('/add', methods=['GET'])
def add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    history.append("Addition of "+str(a)+" and "+str(b)+" is "+str(a+b))
    return jsonify(result=a + b)

@app.route('/subtract', methods=['GET'])
def subtract():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    history.append("Subtraction of "+str(a)+" and "+str(b)+" is "+str(a-b))
    return jsonify(result=a - b)

@app.route('/multiply', methods=['GET'])
def multiply():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    history.append("Multiplication of "+str(a)+" and "+str(b)+" is "+str(a*b))
    return jsonify(result=a * b)

@app.route('/divide', methods=['GET'])
def divide():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    if b == 0:
        return jsonify(error="Division by zero is not allowed"), 400
    history.append("Division of "+str(a)+" and "+str(b)+" is "+str(a/b))
    return jsonify(result=a / b)

@app.route('/exponent', methods=['GET'])
def exponentiation():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    history.append("Exponent of "+str(a)+" and "+str(b)+" is "+str(a**b))
    return jsonify(result=a ** b)

@app.route('/sqrt', methods=['GET'])
def sqrt():
    a = float(request.args.get('a'))
    history.append("Square root of "+str(a)+" is "+str(a**0.5))
    return jsonify(result=a ** 0.5)


@app.route('/history',methods=['GET'])
def history_function():
    return jsonify(history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)