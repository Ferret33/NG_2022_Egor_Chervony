def doOperation(operation, firstNumber, secondNumber):
    if operation == "+":
        operationPlus(firstNumber, secondNumber)
    elif operation == "-":
        operatiomMinus(firstNumber, secondNumber)
    elif operation == "*":
        operationMultiply(firstNumber, secondNumber)
    elif operation == "/":
        try:
            operationDivision(firstNumber, secondNumber)
        except ZeroDivisionError as e:
            return ("Result: Infinity, "+ str(e))
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
    try:
        firstNumber = float(input("Enter first number: "))
        secondNumber = float(input("Enter second number: "))
    except ValueError as e:
        print("Type right value, "+ str(e))
        quit()
        
    operation = input(("Select operation +, -, *, /, square, square root: "))
    doOperation(operation, firstNumber, secondNumber)
main()