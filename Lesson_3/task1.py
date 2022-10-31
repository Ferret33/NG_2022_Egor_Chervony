def doOperation(operation, firstNumber, secondNumber):
    match operation:
        case "+":
            operationPlus(firstNumber, secondNumber)
        case "-":
            operatiomMinus(firstNumber, secondNumber)
        case "*":
            operationMultiply(firstNumber, secondNumber)
        case "/":
            try:
                operationDivision(firstNumber, secondNumber)
            except ZeroDivisionError as e:
                return ("Result: Infinity, "+ str(e))
        case "square":
            operationSquare(firstNumber, secondNumber)
        case "square root":
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