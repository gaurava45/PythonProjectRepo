# 56 + 9 = 77
# 25 - 7 = 15
# 56/6 = 4

num1 = int(input("Enter first integer\n"))
num2 = int(input("Enter second integer\n"))
op = input("enter the operator\n")

if  op == '+':
    if num1 == 56 and num2 == 9:
        print(77)
    else:
        print(num1 + num2)
elif op == '-':
    if num1 == 25 and num2 == 7:
        print(15)
    else:
        print(num1 - num2)
else:
    if num1 == 56 and num2 == 6:
        print(4)
    else:
        print(num1 / num2)

