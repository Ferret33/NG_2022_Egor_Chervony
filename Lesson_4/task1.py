from rich.console import Console
import platform
import psutil
import inquirer
import cpuinfo
import socket

console=Console()

def askoption():
    console.rule("[green][blink]What information you want to write into Info.txt[/blink]"+"\n"+"[green]Space - Select Enter - Pr")
    questions = [inquirer.Checkbox( 
        'options',
        choices=['CPU', 'CPU Cores','CPU Family', 'Architecture', 'Machine type', 'RAM','IP-Address','Disk Partitions', 'System','Computer name'],)]  
    optanswers = inquirer.prompt(questions)
    return optanswers

def cpuInfoWrite(dataFile): 
    dataFile.write("----------CPU----------\n\t"+str(cpuinfo.get_cpu_info()['brand_raw'])+"\n\n")
def ramInfoWrite(dataFile):
    dataFile.write("----------RAM----------\n\t"+str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"+"\n\n")
def architInfoWrite(dataFile):
    dataFile.write("----------Architecture----------\n\t"+str(platform.architecture())+"\n\n")
def sysInfoWrite(dataFile):
    dataFile.write("----------System----------\n\t"+str(platform.platform())+"\n\n")
def machinetypeInfoWrite(dataFile):
    dataFile.write("----------Machine type----------\n\t"+str(platform.machine())+"\n\n")
def cpuFamilyInfoWrite(dataFile):
    dataFile.write("----------CPU Family----------\n\t"+str(platform.processor())+"\n\n")
def compnameInfoWrite(dataFile):
    dataFile.write("----------Computer name----------\n\t"+str(platform.node())+"\n\n")
def cpuCoresInfoWrite(dataFile):
    dataFile.write("----------CPU Cores----------\n"+"\tPhysical cores: "+str(psutil.cpu_count(logical=False))+"\n")
    dataFile.write("\tLogical cores: "+str(psutil.cpu_count(logical=True))+"\n")
    dataFile.write("\tMax Frequency: "+str(psutil.cpu_freq().max)+"\n\n")
def ipInfoWrite(dataFile):
    dataFile.write("----------IP-Address----------\n\t" + str(socket.gethostbyname(socket.gethostname()))+"\n\n")
def macInfoWrite(dataFile):
    partitions = psutil.disk_partitions()
    dataFile.write("----------Disk Partitions----------\n")
    for partition in partitions:
        dataFile.write("\tDisk: " + str(partition.device)+"\n")
        dataFile.write("\tTotla size: " +str(round((psutil.disk_usage(partition.mountpoint).total)/ (1024.0 **3)))+" GB"+"\n")
    dataFile.write("\n")

def gatheroptions(optanswers, dataFile):
    with console.status("Gathering information...", spinner='dots6'):
        for options in optanswers['options']:
            if options == "CPU": 
                cpuInfoWrite(dataFile)
            if options == "RAM": 
                ramInfoWrite(dataFile)
            if options == "CPU Family":
                cpuFamilyInfoWrite(dataFile)
            if options == "System":
                sysInfoWrite(dataFile)
            if options == "Architecture":
                architInfoWrite(dataFile)
            if options == "Machine type":
                machinetypeInfoWrite(dataFile)
            if options == "Computer name":
                compnameInfoWrite(dataFile)
            if options == "CPU Cores":
                cpuCoresInfoWrite(dataFile)
            if options == "IP-Address":
                ipInfoWrite(dataFile)
            if options == "Disk Partitions":
                macInfoWrite(dataFile)
    console.rule("[green]All selected info was writen to (Info.txt)")

def main():  
    dataFile=open("Info.txt", "w")
    gatheroptions(askoption(), dataFile)
    dataFile.close
main()
