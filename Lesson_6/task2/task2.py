from flask import Flask, render_template, request, redirect
from dbworker import *
from pcInfoGether import *

app = Flask("Gether info about pc")
prepareDb("pcinfo.db")

@app.route('/')
def index():
    rows = getMassage("pcinfo.db")
    generatetable = HtmlTableGenerator(rows)
    return render_template("index.html", htmltable=generatetable)

@app.route('/sendmassage')
def sendmassage():
    addOptColumToDb("pcinfo.db")
    gatheroptions(askoption(), "pcinfo.db")
    return redirect("/")
@app.route('/htmltableget')
def getHtmlTable():
    rows = getMassage("pcinfo.db")
    return HtmlTableGenerator(rows)
app.run(host="0.0.0.0", port=8888)
