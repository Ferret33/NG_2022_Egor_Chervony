from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask("NewsLine")

@app.route('/')
def index():
    content = ""
    file = open("News.txt","r")
    for line in file.readlines():
        content+= line
    return render_template("index.html", content = content)
@app.route('/editor')
def editor():
    return render_template("editor.html")

@app.route('/edit')
def edit():
    file = open("News.txt","a")
    time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    file.write("<h1>"+str(request.args.get('newstitle'))+"</h1>\n"+"<h5>"+time+"</h5>\n"+"<h2>"+str(request.args.get('newstext'))+"</h2>\n"+"<hr>\n")
    file.close()
    return redirect('/editor')


app.run(host="0.0.0.0", port=8888)
