numb= int(input("Enter your number: "))
numberlist=[]
i=0
while i<numb:
    numberlist.insert(i, i+1)
    i+=1
numberlist.reverse()  
k=0
print(numberlist)
while k<numb:
    numberlist.remove(numberlist[0])
    k+=1
    
