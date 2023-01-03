from flask import Flask, render_template, request, redirect, send_file
app = Flask("ImageAcquisition")
from rich.console import Console
from getherimageshelper import *
console = Console()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process')
def process():
    Url = request.args.get('URL')
    site = Url.split("/")[2]
    downloadZippingInThreads(site,Url)
    return send_file("zips/"+str(site)+".zip")

app.run(host="0.0.0.0", port=8888)