# :::: calculator project ::::

num1= float(input("Enter first number:  "))
operator = input("Enter operator: + - * / : ")
num2 = float(input("Enter second number: "))

if (operator == "+"):
    print(f"sum of {num1} and {num2} is : ", num1 + num2)
elif (operator == "-"):
    print(f" ofsubtraction of {num1} and {num2} is : ", num1 - num2)
elif (operator == "*"):
   print(f"multiplication of {num1} and {num2} is : ", num1 * num2)
elif (operator == "/"):
    print(f"divison of {num1} and {num2} is : ", num1 / num2)
else:
    print(f"{operator} is not a valid operator")


