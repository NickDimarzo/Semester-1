# Lab: Syntax Rules, Conditions and Loops ex 10
# Author: Group 14

# Variables
number = 0

# Inputs
print("Welcome to Average of Integers ")
N = int(input("Please enter Integer: "))

# Calculations
for i in range(0, N + 1):
    number += i

number_average = (number / N)

# Output
print("Average of", N, "is:", number_average)