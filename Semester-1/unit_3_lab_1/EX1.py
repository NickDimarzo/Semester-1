# Function for Calculating the Area of a Circle
# Author: Group 14

# Function Storage
def circumference_calculation(radius):
    return 2 * pi * radius


def area_calculation(radius):
    return pi * radius ** 2


# Variable Storage and User Input

pi = 3.14
print("To calculate the circumference and area of a circle please enter the desired radius length:")
radius_input = int(input(""))
print(f'The circumference of a circle with a radius {radius_input} will be {circumference_calculation(radius_input)}')
print(f'The area of a circle with a radius {radius_input} will be {area_calculation(radius_input)}')
