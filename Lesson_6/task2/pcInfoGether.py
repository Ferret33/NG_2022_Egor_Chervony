from rich.console import Console
import platform
import psutil
import cpuinfo
import socket
from dbworker import *
from flask import request


console=Console()
def askoption():
    optionsList= []
    for element in request.args:
        optionsList.append(element)
    return optionsList

def cpuInfoWrite(db):
    info = str(cpuinfo.get_cpu_info()['brand_raw'])
    addOneOptinToDb(db, "cpu", info)
def ramInfoWrite(db):
    info = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    addOneOptinToDb(db, "ram", info)
def architInfoWrite(db):
    info = str(platform.architecture()[0])
    addOneOptinToDb(db, "architecture", info)
def sysInfoWrite(db):
    info =str(platform.platform())
    addOneOptinToDb(db,"system", info)
def machinetypeInfoWrite(db):
    info = str(platform.machine())
    addOneOptinToDb(db, "machinetype", info)
def cpuFamilyInfoWrite(db):
    info = str(platform.processor())
    addOneOptinToDb(db, "cpufamily", info)
def compnameInfoWrite(db):
    info = str(platform.node())
    addOneOptinToDb(db,"computername",info)
def cpuCoresInfoWrite(db):
    info =str(psutil.cpu_count(logical=False))+"/"+str(psutil.cpu_count(logical=True))+"| Max freq: "+str(psutil.cpu_freq().max)
    addOneOptinToDb(db, "cpucors", info)
def ipInfoWrite(db):
    info = str(socket.gethostbyname(socket.gethostname()))
    addOneOptinToDb(db,"ipadress", info)
def diskInfoWrite(db):
    info=""
    partitions = psutil.disk_partitions()
    for partition in partitions:
        info+="Disk: " + str(partition.device)+"\n"
        info+="Totla size: " +str(round((psutil.disk_usage(partition.mountpoint).total)/ (1024.0 **3)))+" GB"+"\n"
    addOneOptinToDb(db,"diskpartition", info)

def gatheroptions(optionsList, db):
    with console.status("Gathering information...", spinner='dots6'):
        for option in optionsList:
            if option == "cpu": 
                cpuInfoWrite(db)
            if option == "cpucors": 
                cpuCoresInfoWrite(db)
            if option == "cpufamily":
                cpuFamilyInfoWrite(db)
            if option == "architecture":
                architInfoWrite(db)
            if option == "machinetype":
                machinetypeInfoWrite(db)
            if option == "ram":
                ramInfoWrite(db)
            if option == "ipadress":
                ipInfoWrite(db)
            if option == "diskpartition":
                diskInfoWrite(db)
            if option == "system":
                sysInfoWrite(db)
            if option == "computername":
                compnameInfoWrite(db)
    console.rule("[green]All selected info was writen to DB")
