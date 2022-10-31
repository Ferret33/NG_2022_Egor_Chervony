def doOperation(operation, firstNumber, secondNumber):
    if operation == "+":
        operationPlus(firstNumber, secondNumber)
    elif operation == "-":
        operatiomMinus(firstNumber, secondNumber)
    elif operation == "*":
        operationMultiply(firstNumber, secondNumber)
    elif operation == "/":
        operationDivision(firstNumber, secondNumber)
    elif operation == "square":
        operationSquare(firstNumber, secondNumber)
    elif operation == "square root":
        operationSquareRoot(firstNumber, secondNumber)
   
def operationPlus(firstNumber, secondNumber):
    print(firstNumber + secondNumber)

def operatiomMinus(firstNumber, secondNumber):
    print(firstNumber-secondNumber)

def operationMultiply(firstNumber, secondNumber):
    print(firstNumber*secondNumber)

def operationDivision(firstNumber, secondNumber):
    print(firstNumber/secondNumber)

def operationSquare(firstNumber, secondNumber):
    print(firstNumber**secondNumber)
    
def operationSquareRoot(firstNumber, secondNumber):
    print(firstNumber**(1/secondNumber))

def main():
    firstNumber = float(input("Enter first number: "))
    secondNumber = float(input("Enter second number: "))
    operation = input(("Select operation +, -, *, /, square, square root: "))
    doOperation(operation, firstNumber, secondNumber)
main()