enterednumber= input("Enter list: ")
splitednumber= enterednumber.split(", ")
splitednumber = list(map(int, splitednumber))
splitednumber.sort()
print("Min value: "+ str(splitednumber[0]))
print("Max value: "+ str(splitednumber[-1]))
print("Sum list without Max, Min: "+ str(sum(splitednumber)-splitednumber[0]-splitednumber[-1]))