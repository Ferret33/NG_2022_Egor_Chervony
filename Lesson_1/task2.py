firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))
operation = input("Select operation +, -, *, /, square, square root: ")

if operation == "+":
    print(firstNumber + secondNumber) 
elif operation == "-":
    print(firstNumber-secondNumber)
elif operation == "*":
    print(firstNumber*secondNumber)
elif operation == "/":
    print(firstNumber/secondNumber)
elif operation == "square":
    print(firstNumber**2 , secondNumber**2)
elif operation == "square root":
    print(firstNumber**0.5, secondNumber**0.5)