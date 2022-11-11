from rich.console import Console
import platform
import psutil
import inquirer
import cpuinfo
from inquirer.themes import Default

console=Console()

#Custom theme [YES]/[NO] for inquirer checkboxes
class CustomYesNo(Default):

    def __init__(self):
        super().__init__()
        self.Checkbox.selected_icon = "[YES]"
        self.Checkbox.unselected_icon = "[NO]"
        self.Checkbox.selection_icon = " "
        self.List.selection_cursor = " "

def askoption():
    console.rule("[green][blink]What information you want to write into Info.txt[/blink]"+"\n"+"[green]Space - Select Enter - Pr")

    questions = [inquirer.Checkbox( 
        'options',
        choices=['CPU', 'RAM', 'Architecture', 'CPU Family', 'Machine type', 'System','Computer name'],
    )]
    
    optanswers = inquirer.prompt(questions, theme=CustomYesNo())
    return optanswers


def cpuinfowrite(dataFile): 
    dataFile.write("CPU: "+str(cpuinfo.get_cpu_info()['brand_raw'])+"\n")
def raminfowrite(dataFile):
    dataFile.write("RAM: "+str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"+"\n")
def architinfowrite(dataFile):
    dataFile.write("Architecture: "+str(platform.architecture())+"\n")
def sysinfowrite(dataFile):
    dataFile.write("System: "+str(platform.platform())+"\n")
def machinetypeinfowrite(dataFile):
    dataFile.write("Machine type: "+str(platform.machine())+"\n")
def cpufamily(dataFile):
    dataFile.write("CPU Family: "+str(platform.processor())+"\n")
def compnameinfowrite(dataFile):
    dataFile.write("Computer name: "+str(platform.node())+"\n")


def gatheroptions(optanswers, dataFile):
    with console.status("Gathering information...", spinner='dots6'):
        for options in optanswers['options']:
            if options == "CPU": 
                    cpuinfowrite(dataFile)
            if options == "RAM": 
                    raminfowrite(dataFile)
            if options == "CPU Family":
                    cpufamily(dataFile)
            if options == "System":
                    sysinfowrite(dataFile)
            if options == "Architecture":
                    architinfowrite(dataFile)
            if options == "Machine type":
                    machinetypeinfowrite(dataFile)
            if options == "Computer name":
                    compnameinfowrite(dataFile)

    console.rule("[green]All selected info was writen to (Info.txt)")

def main():
    
    dataFile=open("Info.txt", "w")
    gatheroptions(askoption(), dataFile)
    dataFile.close
main()
