# A Program for Student Classes
# Author: Dawson Gall

# Class & Definitions
class Student:
    def __init__(self, name, id_number, address):
        self.name = name
        self.id_number = id_number
        self.address = address

    def student_name(self):
        print(f'Student Name: {self.name}')

    def student_id(self):
        print(f'Student Id: {self.id_number}')

    def student_address(self):
        print(f'Student Address: {self.address} ')


# Student Info
student_name = "Mark"
student_id = "301897"
student_address = "124 Cherry Street"

student_info = Student(student_name, student_id, student_address)
student_info.student_name()
student_info.student_address()
student_info.student_id()
