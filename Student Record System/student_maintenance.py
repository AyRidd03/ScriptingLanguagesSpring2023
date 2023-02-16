#!/usr/bin/env python3

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Ayden Riddle'
__version__ = '1.0'
__date__ = '2023.02.16'
__status__ = 'Development'

LINE = "=" * 20  # For Neatness :)


def add_student(student_list, new_student_id):
    print(LINE)
    student_f_name = input("Please insert the Student's First Name: ")  # To store first name into the student id later
    student_l_name = input("Please insert the Student's Last Name: ")  # To store last name into the student id later
    student_list[new_student_id] = (student_f_name, student_l_name)
    print(f"Student {student_f_name}, {student_l_name} has been added.")  # To Let the User Know
    print(LINE)


def list_students(student_list):
    print(LINE)
    if len(student_list) == 0:
        print("No Students are Registered")
        print(LINE)
        return
    print(LINE)
    print("Here's Your List of Students: ")
    for student_id, student_name in student_list.items():  # Unpacks the Dictionary
        for f_name, l_name in student_name:  # Unpacks the Tuple in the Dictionary
            print(f"{student_id}: {f_name}, {l_name}")
            print(f"f_name:{f_name}")
            print(f"l_name: {l_name}")
            print(f"student_name:{student_name}")
            print(f"student_id:{student_id}")
            print(f"student_list:{student_list}")


def delete_student(student_list):
    print(LINE)
    student_delete_id = input("Please insert the Student ID you wish to Delete: ")  # To let the user pick the ID
    user_confirmation = input("Are you Sure this is the Student you wish to delete? Y/N: ")  # To Doublecheck
    print("This Student has been deleted.")  # To Let the User Know
    print(LINE)


def update_student(student_list):
    student_edit_id = input("Please insert the Student ID you wish to Edit: ")  # To let the user pick the ID
    print("This Student has been updated")  # To Let the User Know
    print(LINE)
