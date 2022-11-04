def main():
    creditCard= input("Enter your card number: ")
    banksystem= creditCard[0:2]
    oddNumber= list(map(int, creditCard[-1::-2]))
    evenNumber= list(map(int, creditCard[-2::-2]))
    show(checkvalidation(evenNumber, oddNumber),checkbanksystem(banksystem))

def checkvalidation(evenNumber, oddNumber):
    multyEvenElement=[]
    newMultyEvenElems=[]
    for element in evenNumber:
        element *=2
        multyEvenElement.append(element)
    for element in multyEvenElement: 
        if element<10:
             newMultyEvenElems.append(element)
        elif element>=10:
            newMultyEvenElems.append(element//10)
            newMultyEvenElems.append(element%10)       
    finalsum=str(int(sum(oddNumber))+ int(sum(newMultyEvenElems)))
    return finalsum
        
def checkbanksystem(banksystem):
    mastercard=["51","52","53","54","55"]
    amex=["34","37"]
    visa=["4"]
    
    for element in mastercard:
        if element==banksystem:
            bank="MASTERCARD"
    for element in amex:
        if element==banksystem:
            bank="AMEX"
    for element in visa:
        if element==banksystem[0]:
            bank="VISA"
    return bank
    
def show(finalsum, bank):
    if finalsum[-1]=="0":
        print(bank)
    else:
        print("INVALID")

main()