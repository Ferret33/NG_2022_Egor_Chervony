enternumber= int(input("Enter your number: "))
iteration=0

while iteration!=enternumber :
    while iteration<enternumber:
        print(enternumber-iteration,end=" ")
        iteration+=1
    print(end="\n")
    iteration=0
    enternumber-=1