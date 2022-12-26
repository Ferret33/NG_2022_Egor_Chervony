
def prepareFile(name):
    file = open(str(name),"r")
    return file
def prepareNewslist(name):
    file = prepareFile(name)
    newslst = []
    for lines in file.readlines():
        newslst.append(lines)
    file.close
    return newslst

def optionsNewsGenerator(name):
    file = prepareFile(name)
    newslst = []
    newsoptions=""
    for lines in file.readlines():
        newslst.append(lines)
    line = 1
    iteration = 0
    while iteration < len(newslst)/4:
        newsoptions+="<option>"+str(newslst[line][4:-6])+"</option>\n"
        line+=4
        iteration+=1
    file.close
    return newsoptions

def searchNews(data, name):
    newslst=[]
    file = prepareFile(name)
    for line in file.readlines():
         newslst.append(line)
    for element in newslst:
        if str(element)==str(data)+"\n":
            iteration = 0
            news=""
            ind=-1
            while iteration<4:
                news+=str(newslst[newslst.index(data+"\n")+ind])
                ind+=1
                iteration+=1
            return news
