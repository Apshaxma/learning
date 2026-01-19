
print("Welcome to menu driven calculator")
operation = int(input("""Please select the operation you want to perfom 
                      1.Addition of 2 numbers
                      2.Subtraction of 2 numbers
                      3.Multiplication of 2 numbers
                      4.Division of 2 numbers
                        """))

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

if operation == 1:
    print(a+b)
elif operation == 2:
    print(a-b)
elif operation == 3:
    print(a*b)
elif operation == 4:
    print(a/b)
else:
    print("Invalid Operation")  