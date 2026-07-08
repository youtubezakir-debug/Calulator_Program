# Python Calculator

Operator = input("Enter An Operator (+ - * / or + +, + -, + *, + /): ")

if Operator == "+":
    Num1 =float(input("Enter a Number: "))
    Num2 =float(input("Enter a Number: "))

    Result = (Num1 + Num2)
    print(round(Result, 2))

elif Operator == "-":
    Num1 =float(input("Enter a Number: "))
    Num2 =float(input("Enter a Number: "))

    Result = (Num1 - Num2) 
    print(round(Result, 2))

elif Operator == "*":
    Num1 =float(input("Enter a Number: "))
    Num2 =float(input("Enter a Number: "))
    
    Result = Num1 * Num2
    print(round(Result, 2))

elif Operator == "/":
    Num1 =float(input("Enter a Number: "))
    Num2 =float(input("Enter a Number: "))

    Result = Num1 / Num2
    print(round(Result, 2))

elif Operator == "+ +":
    Num1 =float(input("Enter a Number: "))
    Num2 =float(input("Enter a Number: "))
    Num3 =float(input("Enter a Number: "))

    Result = Num1 + Num2 + Num3
    print(round(Result, 2))

elif Operator == "+ -":
    Num1 =float(input("Enter a Number: "))
    Num2 =float(input("Enter a Number: "))
    Num3 =float(input("Enter a Number: "))

    Result = Num1 + Num2 - Num3
    print(round(Result, 2))

elif Operator == "+ *":
    Num1 =float(input("Enter a Number: "))
    Num2 =float(input("Enter a Number: "))
    Num3 =float(input("Enter a Number: "))

    Result = (Num1 + Num2) * Num3
    print(round(Result, 2))

elif Operator == "+ /":
    Num1 =float(input("Enter a Number: "))
    Num2 =float(input("Enter a Number: "))
    Num3 =float(input("Enter a Number: "))

    Result = (Num1 + Num2) / Num3
    print(round(Result, 2))


else:
    print(f"{Operator} is not a valid Operator!")


    
