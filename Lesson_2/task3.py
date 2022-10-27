numb= int(input("Enter your number: "))
numberlist=[]
i=0
while i<numb:
    numberlist.insert(i, str(i+1))
    i+=1
numberlist.reverse()  
k=0

while k<numb:
    print(" ".join(numberlist))
    numberlist.remove(numberlist[0])
    k+=1
    
