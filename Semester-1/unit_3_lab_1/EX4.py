# Function Calculator
# Author: Group 14

# Function List
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# Calculations
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    print("Enter choice(1/2/3/4): ")
    choice = input("")
    if choice in ('1', '2', '3', '4'):
        print("Enter First Number:")
        num1 = float(input(""))
        print("Enter Second Number:")
        num2 = float(input(""))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Please enter a valid input.")
