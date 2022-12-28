from flask import Flask, render_template, request, redirect
app = Flask("ImageAcquisition")
import requests
import os

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process')
def process():
    Url = request.args.get('URL')
    headers = {
    'User-Agent': '...',
    'referer': 'https://...'
    }
    req = requests.get(Url, headers=headers)
    img = [".img",".jpg", ".jpeg", ".gif", ".png",".svg"]
    links=[]
    html = req.text.split('"')
    # os.rmdir('temp/')
    path="temp"
    for files in os.scandir(path):
        os.remove(files)
    # os.mkdir('temp')
    for line in html:
        for ex in img:
            if ex in line:
                if line[0:4] == "http" and line[-4:] == ex:
                    links.append(line)
                    for element in links:
                        imgContent = requests.get(str(element)).content
                        imgfile = open("temp/"+str(line.split("/")[-1]),"wb")
                        imgfile.write(imgContent)
                        imgfile.close
                        # print("Img : "+str(line.split("/")[-1])+" was saved!")
    print("---------End---------")
    return redirect('/')


app.run(host="0.0.0.0", port=8888)