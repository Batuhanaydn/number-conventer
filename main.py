from flask import Flask, request, render_template
from conventer import Binary, Hexedecimal, CustomBase, Octal


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/binary' , methods=['GET', 'POST'])
def binary():
    if request.method == "GET":
        return render_template("binary.html")

    if request.method == "POST":
        number = request.form.get('number')
        number = int(number)
        result = Binary.binary_converter(number)
        return render_template('result.html', result=result)
    


@app.route('/hex', methods=['GET', 'POST'])
def hexedeciaml():
    if request.method == "GET":
        return render_template("hexadecimal.html")


    if request.method == "POST":
        number = request.form.get('number')
        number = int(number)
        result = Hexedecimal.hexedecimal_converter(number)
        return render_template('result.html', result=result)

@app.route('/octal', methods=['GET', 'POST'])
def octal():
    if request.method == "GET":
        return render_template("octal.html")


    if request.method == "POST":
        number = request.form.get('number')
        number = int(number)
        result = Octal.octal_converter(number)
        return render_template('result.html', result=result)


@app.route('/CustomBase', methods=['GET', 'POST'])
def customBase():
    if request.method == "GET":
        return render_template("custom.html")


    if request.method == "POST":
        number = request.form.get('number')
        base = request.form.get('base')

        number = int(number)
        base = int(base)
        result = CustomBase.custom_base_converter(number, base)
        return render_template('result.html' , result=result)



if __name__ == "__main__":
    app.run(debug=True)