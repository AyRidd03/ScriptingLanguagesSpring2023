#!/usr/bin/env python3

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Ayden Riddle'
__version__ = '1.1'
__date__ = '2023.04.25'
__status__ = 'Development'

import pygame
import file_validator as fv


class Menu:
    def __init__(self):
        self.validator = fv.FileValidator()

    def main_menu(self):
        print(fv.LINE)
        self.setup_saves()
        while True:
            print(fv.LINE)
            print("Welcome to the Main Menu! Here are your Options:")
            print("1: Add a File Name/Path")
            print("2: View a File(s)")
            print("3: Validate File Data")
            print("4: Edit the Data of a File")
            print("5: Validate a piece of Data outside of a file")
            print("6: Get a list of Data Saved")
            print("0: Exit")
            print(fv.LINE)
            while True:
                try:
                    user = input("Please insert a number between 0-6: ")
                    user = int(user)
                    if user < 0 or user > 6:
                        raise Exception()
                    else:
                        break

                except ValueError:
                    print("Error: Not a Number")
                except Exception:
                    print("Error: Number not between 0-5")
                except:
                    print("An Unknown Error has Occurred.")
            if user == 0:
                break
            elif user == 1:
                print("Adding File Name/Path")
                self.add_file()
            elif user == 2:
                print("Opening File")
                self.open_file()
            elif user == 3:
                print("Validating File")
                self.validate_file()
            elif user == 4:
                print("Editing a File")
                # self.edit_file()
            elif user == 5:
                print("Validating a Piece of Data")
                # self.validate_data()
            else:
                print("How did you get here? "
                      "Error should cover anything that isn't 0-5. "
                      "Oh well, Back to the Drawing Board")

    def setup_saves(self):
        self.validator.add_file("invalid.csv")
        self.validator.add_file("valid.csv")

    def add_file(self):
        file = input("Please insert the File Name/ Path")
        self.validator.add_file(file)

    def open_file(self):
        print(self.validator.get_file_names())
        user = input("Please Choose a File to Open: ")
        if user in self.validator.get_file_names():
            self.validator.read_file(user)
        else:
            print("ERROR: Not a valid input, returning to Main Menu")

    def validate_file(self):
        print(self.validator.get_file_names())
        user = input("Please Choose a File to Open or Type All for all: ")
        if user in self.validator.get_file_names():
            self.validator.file_validate(user)
        elif user == "All":
            for i in self.validator.get_file_names():
                self.validator.file_validate(i)
        else:
            print("ERROR: Not a valid input, returning to Main Menu")
