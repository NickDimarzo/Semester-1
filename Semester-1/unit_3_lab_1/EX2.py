# Function for Area of a Rectangle
# Author: Group 14

# Function Storage
def rectangular_area(side_b, side_c):
    return side_b*side_c


# User Input
print("To Calculate the Area of a Rectangle input the length of the two sides")
print("The length of side b is:")
b = int(input(""))
print("The length of side c is:")
c = int(input(""))
print(f"The area of a circle with length {b} and {c} will be {rectangular_area(b, c)}")
