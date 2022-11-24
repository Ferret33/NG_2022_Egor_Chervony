from flask import Flask, render_template, request, redirect

app = Flask("Calculator")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/pls')
def pls():
    res= float(float(request.args.get('firstvalue'))+float(request.args.get('secondvalue')))
    return render_template("index.html", res =res)

@app.route('/min')
def min():
    res= float(float(request.args.get('firstvalue'))-float(request.args.get('secondvalue')))
    return render_template("index.html", res =res)

@app.route('/multy')
def multy():
    res= float(float(request.args.get('firstvalue'))*float(request.args.get('secondvalue')))
    return render_template("index.html", res =res)

@app.route('/dev')
def dev():
    if int(request.args.get('secondvalue'))==0:
        res="ERROER devide by 0"
    else:
        res= float(float(request.args.get('firstvalue'))/float(request.args.get('secondvalue')))
    return render_template("index.html", res =res)

@app.route('/square')
def square():
    res= float(float(request.args.get('firstvalue'))**float(request.args.get('secondvalue')))
    return render_template("index.html", res =res)

@app.route('/squareroot')
def squareroot():
    if int(request.args.get('secondvalue'))==0:
        res="ERORR no 0 root"
    else:
        res= float(float(request.args.get('firstvalue'))**(1/float(request.args.get('secondvalue'))))
    return render_template("index.html", res =res)

app.run(host="0.0.0.0", port=8888)
