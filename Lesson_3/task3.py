from collections import Counter

def count(enterString):
    print(Counter(enterString)) 

def main():
    enterString= input("Type your string: ")
    count(enterString)
main()
