def main():
    enterString= input("Type your string: ")
    setString= set(enterString)
    countletters(enterString, setString)


def countletters(enterString, setString):
    countList=list(map(lambda element: int(enterString.count(element)), setString))
    countdict = {}
    for element in range(len(setString)):
        countdict[list(setString)[element]] = countList[element]
    for element in countdict.keys():
        print(str(element)+":"+str(countdict[element]))
main()    