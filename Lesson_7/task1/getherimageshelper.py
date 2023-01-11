from flask import request, send_file, redirect
from rich.console import Console
import requests
console = Console()
import os
import zipfile
import threading

def downloadImg(site,Url):
    headers = {
    'User-Agent': '...',
    'referer': 'https://...'
    }
    req = requests.get(Url, headers=headers)
    img = [".img",".jpg", ".jpeg", ".gif", ".png",".svg"]
    links=[]
    html = req.text.split('"')
    if not os.path.exists("temp/"+site):
        os.mkdir("temp/"+site)
    path="temp/"+site
    for files in os.scandir(path):
        os.remove(files)
    # if not req:
    #     print ("Error, no conection with site")
    # else:
    #     pass
    print("Conecting to site...")
    if req.status_code == 200:
        print(site)
        print("200")
        for line in html:
            for ex in img:
                if ex in line:
                    if line[0:4] == "http" and line[-4:] or line[-5:]  == ex:
                        links.append(line)
                    elif line[0] == "/" and line[-4:] or line[-5:] == ex:
                        if Url[-1] == "/":
                            links.append(Url+ line[1:])
                        else:
                            links.append(Url+line)   
                    elif line[0] != "/" and line[-4:] or line[-5:] == ex:
                        if Url[-1] == "/":
                            links.append(Url+line)
                        else:
                            links.append(Url+"/"+line) 
        print ("Find "+str(len(links))+" image(s)" )
        # print("Start downloading...")
        imgcounter=1
        with console.status("Downloading...", spinner="monkey"):
            for element in links:
                try:
                    with open("temp/"+site+"/"+str(element.split("/")[-1]),"wb") as imgfile:
                        imgContent = requests.get(str(element)).content
                        imgfile.write(imgContent)
                        imgfile.close
                        print("Image "+ str(element.split("/")[-1])+ " was saved!")
                    print(str(imgcounter)+"/"+str(len(links)))
                    imgcounter+=1    
                except:
                    pass

    else:
        print ("wrong")
    
def zippingImg(site):
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

def downloadZippingInThreads(site,Url):
    threads=[]
    threads.append(threading.Thread(target=downloadImg(site,Url)))
    threads.append(threading.Thread(target=zippingImg(site)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("-----END-----")
    