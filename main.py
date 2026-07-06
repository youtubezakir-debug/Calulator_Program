# Python Calculator

Operator = input("Enter An Operator (+ - * /): ")

Num1 =float(input("Enter a Number: "))
Num2 =float(input("Enter a Number: "))

if Operator == "+":
    Result = Num1 + Num2
    print(round(Result, 2))

elif Operator == "-":
    Result = Num1 - Num2
    print(round(Result, 2))

elif Operator == "*":
    Result = Num1 * Num2
    print(round(Result, 2))

elif Operator == "/":
    Result = Num1 / Num2
    print(round(Result, 2))

else:
    print(f"{Operator} is not a valid Operator!")


    
