#!/usr/bin/env python3

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Ayden Riddle'
__version__ = '1.0'
__date__ = '2023.02.16'
__status__ = 'Development'

import data_validation as dv  # user input data validation

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

    print("Here's Your List of Students: ")
    for student_id, student_name in student_list.items():  # Unpacks the Dictionary
        f_name, l_name = student_name  # Unpacks the Tuple in the Dictionary
        print(f"{student_id}: {f_name}, {l_name}")


def delete_student(student_list):
    list_students(student_list)
    while True:  # Make sure user inputs a proper integer
        student_delete_id = dv.get_num(  # To let the user pick the ID
            "Please insert the Student ID you wish to Delete or push 0 to cancel: ")
        if student_delete_id == 0:
            return
        elif student_delete_id not in student_list:
            print("Invalid input, please insert a valid ID")
        else:
            break  # Must be a valid input in this case since we already checked 0

    f_name, l_name = student_list[student_delete_id]
    user_confirmation = dv.get_yes_no(f"Are you Sure you wish to delete {f_name} {l_name}? Y/N: ")  # To Doublecheck
    if user_confirmation:
        student_list.pop(student_delete_id)
        print("This Student has been deleted.")  # To Let the User Know
    print(LINE)


def update_student(student_list):
    list_students(student_list)
    while True:
        student_edit_id = dv.get_num(  # To let the user pick the ID
                "Please insert the Student ID you wish to Edit or push 0 to cancel: ")
        if student_edit_id == 0:
            return
        elif student_edit_id not in student_list:
            print("Invalid input, please insert a valid ID")
        else:
            break  # Must be a valid input in this case since we already checked 0

    f_name, l_name = student_list[student_edit_id]
    old_f_name = f_name
    old_l_name = l_name
    f_name = input(f"Please insert {f_name}'s new first name or push enter to continue : ")
    l_name = input(f"Please insert {l_name}'s new last name or push enter to continue : ")
    if l_name == '' and f_name == '':
        return
    if l_name == '':
        l_name = old_l_name
    if f_name == '':
        f_name = old_f_name
    user_confirmation = dv.get_yes_no(
        f"Are you Sure you wish to edit {old_f_name} {old_l_name} into {f_name} {l_name}? Y/N: ")  # To Doublecheck
    if not user_confirmation:
        return
    student_list[student_edit_id] = (f_name, l_name)

    print("This Student has been updated")  # To Let the User Know
    print(LINE)
