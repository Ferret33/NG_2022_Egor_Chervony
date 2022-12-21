from flask import Flask, render_template, request, redirect, flash
from dbworker import *

app = Flask("Chat")
prepareDb("chat.db")

@app.route('/')
def index():
    rows = getMassage("chat.db")
    generatetable = HtmlTableGenerator(rows)
    return render_template("index.html", htmltable=generatetable)

@app.route('/sendmassage')
def sendmassage():
    user = request.args.get('username')
    massage = request.args.get('massagetext')
    if user == "" or user == " ":
        rows = getMassage("chat.db")
        generatetable = HtmlTableGenerator(rows)
        warn = "User name is empty. Please write corect input data" 
        return render_template("index.html", htmltable=generatetable,warning=warn )
    else:
        addMassageToDb("chat.db", user, massage)
        return redirect("/")
@app.route('/htmltableget')
def getHtmlTable():
    rows = getMassage("chat.db")
    return HtmlTableGenerator(rows)
app.run(host="0.0.0.0", port=8888)
