print("Welcome to Commmand line interface Calulator")

op = input("Select the Operator + - * /")
a = int(input("Enter the First Number"))
b = int(input("Enter the Second Number"))

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
else:
    print("Invalid Operator")