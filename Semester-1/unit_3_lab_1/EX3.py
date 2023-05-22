# Function for Average of Integers
# Author: Group 14

# Function Storage
def average_sum(integer):
    number = 0
    for i in range(0, integer + 1):
        number += i

    return number/integer


# User Input
print("Enter integer you would like to find the average of:")
integer_input = int(input(""))
print(f"The average of {integer_input} is, {average_sum(integer_input)}")
