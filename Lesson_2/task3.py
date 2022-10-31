enternumber= int(input("Enter your number: "))
numberlist=[]
iteration=0
while iteration<enternumber:
    numberlist.insert(iteration, str(iteration+1))
    iteration+=1
numberlist.reverse()  
iteration=0

while iteration<enternumber:
    print(" ".join(numberlist))
    numberlist.remove(numberlist[0])
    iteration+=1
    
