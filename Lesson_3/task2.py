def main():
    enterString=input("Enter string: ")
    print("===================================================\n"
          "\t\t Select action \n"
          "|1| - Sort string\n"
          "|2| - Count amount of elements\n"
          "|3| - Output only vowels or consonants letters\n"
          "|4| - Divide by words and show words from the end\n"
          "|5| - Show word by number\n"
          "|6| - Show string again\n"
          "|q| - Quit\n"
          "===================================================\n")
    action=input("Select operation: ")
    selectoperation(action,enterString)
    
def selectoperation(action,enterString):
    match action:
        case "1":
            sortString(enterString)
        case "2":
            countAmountLetters(enterString)
        case "3":
            vowelsOrConsonants(enterString)
        case "4":
            devideByWordsBackShow(enterString)
        case "5":
            showByNumber(enterString)
        case "6":
            showAgain(enterString)
        case "7":
            quit()
                
def sortString(enterString):
    enterString=list(map(str, enterString))
    enterString.sort()
    print("".join(enterString))
                
def countAmountLetters(enterString):
    countAmountLattersList={}
    for element in enterString: 
        if element in countAmountLattersList:
            countAmountLattersList[element]+=1                       
        else:
            countAmountLattersList[element]=1
    for element in countAmountLattersList:
        print ("Amount "+str(element) +" letter "+": " + str(countAmountLattersList[element]))

def vowelsOrConsonants(enterString):
    vowels="aeiouy"
    consonants="bcdfghjklmnpqrstvwxyz"
    count={"Vowels letter": 0,
           "Consonants letter": 0}
    for element in enterString:
        if  element in vowels:
            count["Vowels letter"]+=1
        elif element in consonants:
            count["Consonants letter"]+=1
    for element in count:
        print("Amount " + str(element)+" "+ str(count[element]))

def devideByWordsBackShow(enterString):
    enterString=enterString.split(" ")
    enterString.reverse()
    print(" ".join(enterString))

def showByNumber(enterString):
    number=int(input("Enter word number: "))
    enterString=enterString.split(" ")
    print("Word with index "+str(number)+" is "+ str(enterString[number-1]))

def showAgain(enterString):
    print("Your string is: "+str(enterString))
               
main()