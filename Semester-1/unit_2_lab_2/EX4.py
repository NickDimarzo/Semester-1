# EX_Simple_calculator
x = int(input("Please enter first integer:"))
y = int(input("Please enter second integer:"))

print("The operations available are: add, subtract, multiply and divide")
z = input("Please select the operation:")

op_1 = "add"
op_2 = "subtract"
op_3 = "multiply"
op_4 = "divide"

if z == op_1:
    print(x + y)
elif z == op_2:
    print(x - y)
elif z == op_3:
    print(x * y)
elif z == op_4:
    print(x / y)
