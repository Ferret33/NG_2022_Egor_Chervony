
def prepareFile(name):
    file = open(str(name),"r")
    return file
def prepareNewslist(name):
    newslst = []
    for lines in prepareFile(name).readlines():
        newslst.append(lines)
    return newslst

def optionsNewsGenerator(name):
    file = prepareFile(name)
    newslst = []
    newsoptions=""
    for lines in file.readlines():
        newslst.append(lines)
    line = 1
    iteration = 1
    while iteration < len(newslst)/4:
        newsoptions+="<option>"+str(newslst[line][4:-6])+"</option>\n"
        line+=4
        iteration+=1
    file.close
    # print(newsoptions)
    return newsoptions

def searchNews(data, name):
    newslst = []
    for lines in prepareFile(name).readlines():
        newslst.append(lines)
    print(newslst)
    if data in newslst:
        return "ok"
            
