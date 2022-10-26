inputstring = str(input("Enter your line: "))
print ("Line length: " + str(len(inputstring)))
count={}
for element in inputstring: 
    if element in count:
        count[element]+=1                       
    else:
        count[element]=1
for element in count:
    print ("Amount "+str(element) +" letter "+": " + str(count[element]))
print ("Counter of letter in line: "+ str(count))