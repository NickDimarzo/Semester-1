# Project Classes Group 14
# Adam Sutherby
# Dawson Gall
# Nick Dimarzo

# This is a Patient and Doctor Management System designed for Alberta Hospital(AH). This Program is used to organize
# This Program is used record and update the current doctors and patients files within the hospital.

class Doctor:
    def __init__(self, doctor_id=None, name=None, specialization=None, working_time=None,
                 qualification=None, room_number=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    # Doctor getters
    def get_doctor_id(self):
        return self.doctor_id

    def get_name(self):
        return self.name

    def get_specialization(self):
        return self.specialization

    def get_working_time(self):
        return self.working_time

    def get_qualification(self):
        return self.qualification

    def get_room_number(self):
        return self.room_number

    # Doctor Setters
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id
        return new_id

    def set_name(self, new_name):
        self.name = new_name
        return new_name

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization
        return new_specialization

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time
        return new_working_time

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification
        return new_qualification

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number
        return new_room_number

    def __str__(self):
        return f'{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_' \
               f'{self.qualification}_{self.room_number}'


# DoctorManager is used to find, edit and add new doctors to the file system.
class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.doctors = self.read_doctors_file()

    def format_dr_info(self, doctor):
        formatted_doctor = Doctor(doctor)
        return f"{formatted_doctor}"

    # creates a new Doctor object
    def enter_dr_info(self):
        new_dr_id = input("Enter the doctor's ID: ")
        new_dr_name = input("Enter the doctor's name: ")
        new_dr_spec = input("Enter the doctor's speciality: ")
        new_dr_time = input("Enter the doctor's timing(e.g., 7am - 10pm): ")
        new_dr_qualification = input("Enter the doctor's qualification: ")
        new_dr_room = input("Enter the doctor's room number: ")

        new_doctor = Doctor(new_dr_id, new_dr_name, new_dr_spec, new_dr_time, new_dr_qualification, new_dr_room)
        return new_doctor

    # read_doctors_file pulls lines from the doctors.txt file and converts each line into Doctor object.
    @staticmethod
    def read_doctors_file():
        doctors_list = []
        file = open('doctors.txt', 'r')
        for line in file:
            data = line.strip().split('_')
            doctor_id = data[0]
            name = data[1]
            specialization = data[2]
            working_time = data[3]
            qualification = data[4]
            room_number = data[5]
            read_doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
            doctors_list.append(read_doctor)
        file.close()
        return doctors_list

    # searches for a Doctor object with matching id using the id attribute and getter of the Doctor class
    def search_doctor_by_id(self):
        display_doctor = None
        found_doctor = None
        search_id = input("Please enter Doctor ID: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == search_id:
                found_doctor = True
                display_doctor = self.display_doctor_info(doctor)
                break
            else:
                found_doctor = False
                continue
        if found_doctor:
            return print(display_doctor)
        else:
            print("Can't find the doctor with the same ID on the system")

    # searches for a Doctor object with matching name using the name attribute and getter of the Doctor class
    def search_doctor_by_name(self):
        display_doctor = None
        found_doctor = None
        search_name = input("Please enter Doctor name: ")
        search_doctor = search_name.strip()
        for doctor in self.doctors:
            strip_doctor = doctor.get_name()
            if strip_doctor.strip() == search_doctor:
                found_doctor = True
                display_doctor = self.display_doctor_info(doctor)
                break
            else:
                found_doctor = False
                continue
        if found_doctor:
            return print(display_doctor)
        else:
            print("Can't find the doctor with the same name on the system")

    # searches for Doctor using id attribute of Doctor class and setters to edit info of the Doctor with this id
    def edit_doctor_info(self):
        search_id = input("Please enter the id of the doctor that you want to edit their information: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == search_id:
                new_name = input("Enter new name:")
                new_speciality = input("Enter new speciality:")
                new_timing = input("Enter new timing: ")
                new_qualification = input("Enter new qualification: ")
                new_room = input("Enter new room number: ")
                doctor.set_name(new_name)
                doctor.set_specialization(new_speciality)
                doctor.set_working_time(new_timing)
                doctor.set_qualification(new_qualification)
                doctor.set_room_number(new_room)
                self.write_list_of_doctors_to_file()
                return print(f"Doctor whose ID is {search_id} has been edited")
            else:
                continue

    def display_doctor_info(self, doctor):
        return f'{doctor.get_doctor_id():<5} {doctor.get_name():<20} {doctor.get_specialization():<15}' \
               f'{doctor.get_working_time():<15} {doctor.get_qualification():<15} ' \
               f'{doctor.get_room_number()}\n'

    def display_doctors_list(self):
        for doctor in self.doctors:
            print(self.display_doctor_info(doctor))

    # records any changes to the doctors.txt file
    def write_list_of_doctors_to_file(self):
        file = open("doctors.txt", "w")
        for doctor in self.doctors:
            file.write(f"{doctor}\n")
        file.close()

    # records new Doctor to the doctors.txt file
    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        file = open("doctors.txt", "a")
        file.write(f"\n{new_doctor}")
        file.close()
        print(f"Doctor whose ID is {new_doctor.get_doctor_id()} has been added")


class Patient:
    def __init__(self, p_id=None, p_name=None, disease=None, gender=None, age=None):
        self.p_id = p_id
        self.p_name = p_name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_p_id(self):
        return self.p_id

    def get_p_name(self):
        return self.p_name

    def get_disease(self):
        return self.disease

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def set_p_id(self, new_p_id):
        self.p_id = new_p_id
        return new_p_id

    def set_p_name(self, new_p_name):
        self.p_name = new_p_name
        return new_p_name

    def set_disease(self, new_disease):
        self.disease = new_disease
        return new_disease

    def set_gender(self, new_gender):
        self.gender = new_gender
        return new_gender

    def set_age(self, new_age):
        self.age = new_age
        return new_age

    def __str__(self):
        return f'{self.p_id}_{self.p_name}_{self.disease}_{self.gender}_{self.age}'


# PatientManager is used to find, edit and add new doctors to the file system.
class PatientManager:
    def __init__(self):
        self.patients = []
        self.patients = self.read_patient_file()

    def format_patient_info(self, patient):
        formatted_patients = Patient(patient)
        return formatted_patients

    # creates new Patient object
    def enter_patient_info(self):
        new_p_id = input("Enter Patient ID:")
        new_p_name = input("Enter Patient Name:")
        new_disease = input("Enter Patient Disease:")
        new_gender = input("Enter Patient Gender:")
        new_age = input("Enter Patient Age:")
        new_patient = Patient(new_p_id, new_p_name, new_disease, new_gender, new_age)
        return new_patient

    # read_patient_file pulls lines from the patients.txt file and converts each line into Patient object.
    @staticmethod
    def read_patient_file():
        patient_list = []
        file = open('patients.txt', 'r')
        for line in file:
            data = line.strip().split('_')
            p_id = data[0]
            p_name = data[1]
            disease = data[2]
            gender = data[3]
            age = data[4]
            read_patient = Patient(p_id, p_name, disease, gender, age)
            patient_list.append(read_patient)
        file.close()
        return patient_list

    # searches for a Patient object with matching id using the id attribute and getter of the Patient class
    def search_patient_by_id(self):
        display_patient = None
        found_patient = None
        search_id = input("Please enter Patient ID: ")
        for patient in self.patients:
            if patient.get_p_id() == search_id:
                found_patient = True
                display_patient = self.display_patient_info(patient)
                break
            else:
                found_patient = False
                continue
        if found_patient:
            return print(display_patient)
        else:
            print("Can't find the Patient with the same id on the system")

    def display_patient_info(self, patient):
        return f'{patient.get_p_id():<5} {patient.get_p_name():<20} {patient.get_disease():<15} ' \
               f'{patient.get_gender():<15} {patient.get_age():<15}\n'

    # searches for Patient using id attribute of Patient class and setters to edit info of the Patient with this id
    def edit_patient_info(self):
        search_p_id = input("Please enter the id of the Patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.get_p_id() == search_p_id:
                new_p_name = input("Enter new Name:")
                new_disease = input("Enter new disease:")
                new_gender = input("Enter new gender:")
                new_age = input("Enter new age:")
                patient.set_p_name(new_p_name)
                patient.set_disease(new_disease)
                patient.set_gender(new_gender)
                patient.set_age(new_age)
                self.write_list_of_patients_to_file()
                return print(f'Patient whose ID is {search_p_id} had been edited')
            else:
                continue

    def display_patient_list(self):
        for patient in self.patients:
            print(self.display_patient_info(patient))

    # records any changes to the patients.txt file
    def write_list_of_patients_to_file(self):
        file = open("patients.txt", "w")
        for patient in self.patients:
            file.write(f"{patient}\n")
        file.close()

    # records new patients to the patients.txt file
    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        file = open("patients.txt", "a")
        file.write(f"\n{new_patient}")
        file.close()
        print(f"Patient whose ID is {new_patient.get_p_id()} has been added")


# Used to create objects of DoctorManager and PatientManager classes
class Management:

    @staticmethod
    def display_menu():

        while True:
            print("Welcome to Alberta Hospital (AH) Management system")
            print("Select from the following options, or select 3 to stop:")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit Program")
            main_menu_user_input = input("")

            if main_menu_user_input == "1":
                while True:
                    print("Doctors Menu:")
                    print("1 - Display Doctors list")
                    print("2 - Search for doctor by ID")
                    print("3 - Search for doctor by name")
                    print("4 - Add doctor")
                    print("5 - Edit doctor info")
                    print("6 - Back to the Main Menu")
                    doctors_menu_user_input = input("")

                    if doctors_menu_user_input == "1":
                        doctor_manager = DoctorManager()
                        doctor_manager.display_doctors_list()
                        continue

                    elif doctors_menu_user_input == "2":
                        doctor_manager = DoctorManager()
                        doctor_manager.search_doctor_by_id()
                        continue

                    elif doctors_menu_user_input == "3":
                        doctor_manager = DoctorManager()
                        doctor_manager.search_doctor_by_name()
                        continue

                    elif doctors_menu_user_input == "4":
                        doctor_manager = DoctorManager()
                        doctor_manager.add_dr_to_file()
                        continue

                    elif doctors_menu_user_input == "5":
                        doctor_manager = DoctorManager()
                        doctor_manager.edit_doctor_info()
                        continue

                    elif doctors_menu_user_input == "6":
                        break

                    else:
                        print("Invalid input. Please enter valid input")
                        continue

            elif main_menu_user_input == "2":
                while True:
                    print("Patient Menu:")
                    print("1 - Display patient list")
                    print("2 - Search for patient by ID")
                    print("3 - Add patient")
                    print("4 - Edit patient info")
                    print("5 - Back to the Main Menu")
                    patient_menu_user_input = input("")

                    if patient_menu_user_input == "1":
                        patient_manager = PatientManager()
                        patient_manager.display_patient_list()
                        continue

                    elif patient_menu_user_input == "2":
                        patient_manager = PatientManager()
                        patient_manager.search_patient_by_id()
                        continue

                    elif patient_menu_user_input == "3":
                        patient_manager = PatientManager()
                        patient_manager.add_patient_to_file()
                        continue

                    elif patient_menu_user_input == "4":
                        patient_manager = PatientManager()
                        patient_manager.edit_patient_info()
                        continue

                    elif patient_menu_user_input == "5":
                        break

                    else:
                        print("Invalid input. Please enter valid input")
                        continue

            elif main_menu_user_input == "3":
                print("Thanks for using the program. Bye!")
                break

            else:
                print("Please enter valid input")
                continue


Management().display_menu()
