enternumb = int(input("Enter the number to count factorial: "))
enternumbres =enternumb
if enternumb == 1:
    print(str(enternumb) +"! = 1" )

elif enternumb>0:
    nextnumber=enternumb-1
    while nextnumber != 0:
        enternumb=enternumb*nextnumber
        nextnumber-=1    
        result=enternumb
    print(str(enternumbres) + "! = " + str(result))        
    
else:
    print ("Enter a positive number")