# A Cost Program for Shiny Paint
# Author: Group 14

# Function for Room Area
def compute_room_area(rooms):
    total_area = 0
    total_paint_required = 0
    total_paint_price = 0
    number_room_range = range(1, rooms + 1)

    # For loop taking user's room selection
    for room in number_room_range:
        while True:
            print(f'Room: {room}')
            print('Select the shape of the room:')
            print('1- Rectangular')
            print('2- Square')
            print('3- Custom (more or less than 4 walls, all square or rectangles)')
            shape = input()
            wall_area = 0

            if shape == "1":
                print('Enter the length of the room in feet:')
                length = int(input())
                print('Enter the width of the room in feet:')
                width = int(input())
                print('Enter the height of the room in feet:')
                height = int(input())
                wall_area = compute_rectangle_walls_area(length, width, height)
                break
            elif shape == "2":
                print('Enter the length of one side of the room:')
                length = int(input())
                wall_area = compute_square_walls_area(length)
                break
            elif shape == "3":
                print('How many walls are there in the room:')
                wall_amount = int(input())
                wall_area = compute_custom_walls_area(wall_amount)
                break
            else:
                print('Invalid selection, please try again')
                continue

        print("How many windows and doors does the room contain?")
        windows_doors = int(input())
        windows_doors_area = compute_windows_doors_area(windows_doors)
        room_area = wall_area - windows_doors_area
        paint_amount = compute_gallons(room_area)
        paint_price = compute_paint_price(room_area)
        print(f"For Room: {room}, the area to be painted is {room_area:.1f} square ft and will require "
              f"{paint_amount:.2f} gallons to paint. This will cost the customer ${paint_price:.2f} ")
        total_area += room_area
        total_paint_required += paint_amount
        total_paint_price += paint_price

    print(f"Area to be painted is {total_area:.2f} square ft and will require {total_paint_required:.2f} gallons to "
          f"paint. This will cost the customer ${total_paint_price:.2f}")


# Function for Rectangular Walls
def compute_rectangle_walls_area(length, width, height):
    length_side = 2 * calculate_rectangle_area(length, height)
    width_side = 2 * calculate_rectangle_area(width, height)
    rectangle_room = length_side + width_side
    return rectangle_room


# Function for Rectangular Area
def calculate_rectangle_area(length, width):
    rectangle_area = length * width
    return rectangle_area


# Function for Square Walls
def compute_square_walls_area(length_side):
    one_side = compute_square_area(length_side)
    square_room = one_side * 4
    return square_room


# Function for Square Area
def compute_square_area(length_side):
    square_area = length_side ** 2
    return square_area


# Function for Windows and Door Area
def compute_windows_doors_area(number_windows_doors):
    windows_doors_range = range(1, number_windows_doors + 1)
    area_windows_doors = 0

    for single_window_door in windows_doors_range:
        print(f'Enter window/door length for window/door {single_window_door} in feet')
        length = int(input())
        print(f'Enter window/door width for window/door {single_window_door} in feet')
        width = int(input())
        window_door_area = calculate_rectangle_area(length, width)
        area_windows_doors += window_door_area
    return area_windows_doors


# Function for Custom Room Area
def compute_custom_walls_area(walls):
    walls_range = range(1, walls + 1)
    custom_area = 0

    for wall in walls_range:
        print(f'Enter the height of wall {wall} in feet')
        height = int(input())
        print(f'Enter the length of wall {wall} in feet')
        length = int(input())
        wall_area = calculate_rectangle_area(length, height)
        custom_area += wall_area
    return custom_area


# Function for Paint Amount (Gallons)
def compute_gallons(area):
    gallons = (area / 350)
    return gallons


# Function for Paint Price
def compute_paint_price(area):
    paint_price = compute_gallons(area) * float(42.00)
    return paint_price


# Boot Print Screens
print('Welcome to Shiny Paint Company for indoor painting!')
print('How many Rooms do you want to paint:')
number_rooms = int(input())
print('Thank you!')
compute_room_area(number_rooms)
