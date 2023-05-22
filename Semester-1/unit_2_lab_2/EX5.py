# EX5_Multiples
x = int(input("Please enter first number:"))
y = int(input("Please enter second number:"))

z1 = float(x % y)
z2 = float(y % x)

if z1 == 0 or z2 == 0:
    print("These numbers are multiples of each other.")
else:
    print("These numbers are not multiples of each other.")
