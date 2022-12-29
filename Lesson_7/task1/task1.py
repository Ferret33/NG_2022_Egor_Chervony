from flask import Flask, render_template, request, redirect, send_file
app = Flask("ImageAcquisition")
import requests
import os
import zipfile
from rich.console import Console
console = Console()

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
    site = Url.split("/")[2]
    print(site)
    req = requests.get(Url, headers=headers)
    img = [".img",".jpg", ".jpeg", ".gif", ".png",".svg"]
    links=[]
    html = req.text.split('"')
    if not os.path.exists("temp/"+site):
        os.mkdir("temp/"+site)
    path="temp/"+site
    for files in os.scandir(path):
        os.remove(files)
    with console.status("Downloading...", spinner="monkey"):
        for line in html:
            for ex in img:
                if ex in line:
                    if line[0:4] == "http" and line[-4:] == ex:
                        links.append(line)
                    elif line[0] == "/" and line[-4:] == ex:
                        if Url[-1] == "/":
                            links.append(Url+ line[1:])
                        else:
                            links.append(Url+line)   
                    elif line[0] != "/" and line[-4:] == ex:
                        if Url[-1] == "/":
                            links.append(Url+line)
                        else:
                            links.append(Url+"/"+line) 
                    for element in links:
                            try:
                                imgContent = requests.get(str(element)).content
                                if not os.path.exists("temp/"+site+"/"+str(line.split("/")[-1])):
                                    with open("temp/"+site+"/"+str(line.split("/")[-1]),"wb") as imgfile:
                                        imgfile.write(imgContent)
                                        imgfile.close
                            except:
                                pass
    
        message = "All images downloded successfully"
    if not os.path.exists("zips/"+site):
        with zipfile.ZipFile("zips/"+str(site)+".zip","w") as zip:
            for files in os.walk("temp/"+site):
                for elements in files[2]:
                    zip.write("temp/"+site+"/"+elements)
    else:
        os.remove("zips/"+site)
        with zipfile.ZipFile("zips/"+str(site)+".zip","w") as zip:
            for files in os.walk("temp/"+site):
                for elements in files[2]:
                    zip.write(elements)

    print("-----END-----")
    
    return send_file("zips/"+str(site)+".zip")

app.run(host="0.0.0.0", port=8888)