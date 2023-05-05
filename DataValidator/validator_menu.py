#!/usr/bin/env python3

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Ayden Riddle'
__version__ = '1.5'
__date__ = '2023.05.04'
__status__ = 'Finished'

import pygame
import file_validator as fv


class Menu:
    def __init__(self, debug=False):
        self.validator = fv.FileValidator(files=["valid.csv", "invalid.csv", "hello.csv"])
        self.debug = debug

    def main_menu(self):
        if self.debug:
            print(f"Debug Mode: Starting {self.main_menu.__name__()}")
        while True:
            print(fv.LINE)
            print("Welcome to the Main Menu! Here are your Options:")
            print("1: Add a File Name/Path")
            print("2: View a File(s)")
            print("3: Validate File Data")
            print("4: Get a list of Data Saved")
            print("0: Exit")
            print(fv.LINE)
            while True:
                try:
                    user = input("Please insert a number between 0-4: ")
                    user = int(user)
                    if user < 0 or user > 4:
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
                print("Fetching Valid Data")
                self.list_menu()
            else:
                print("How did you get here? "
                      "Error should cover anything that isn't 0-4. "
                      "Oh well, Back to the Drawing Board")

    def add_file(self):
        file = input("Please insert the File Name/ Path: ")
        self.validator.add_file(file)

    def open_file(self):
        while True:
            print(self.validator.get_file_names())
            user = input("Please Choose a File to Open or 0 to Exit: ")
            if user in self.validator.get_file_names():
                self.validator.read_file(user)
                break
            elif user == 0:
                print("Returning to Main Menu")
                break
            else:
                print("ERROR: Not a valid input")

    def validate_file(self):
        while True:
            print(self.validator.get_file_names())
            user = input("Please Choose a File to Open or type All for All of them or 0 to Exit: ")
            if user in self.validator.get_file_names():
                self.validator.file_validate(user)
                break
            elif user == "All":
                for i in self.validator.get_file_names():
                    self.validator.file_validate(i)
                break
            elif user == 0:
                print("Returning to Main Menu")
                break
            else:
                print("ERROR: Not a valid input")

    def list_menu(self):
            if self.debug:
                print(f"Debug Mode: Starting {self.list_menu.__name__()}")
            while True:
                print(fv.LINE)
                print("Welcome to the List Menu! Here are your Options:")
                print("1: Names")
                print("2: Phone Numbers")
                print("3: Emails")
                print("4: First and Last Names Separately")
                print("0: Exit")
                print(fv.LINE)
                while True:
                    try:
                        user = input("Please insert a number between 0-4: ")
                        user = int(user)
                        if user < 0 or user > 4:
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
                    print("Here's the List of valid Names:")
                    for i in self.validator.names:
                        last_name, first_name = i
                        print(f"{first_name} {last_name}")
                elif user == 2:
                    print("Here's the list of valid Numbers:")
                    for i in self.validator.get_phone_numbers():
                        print(i)
                elif user == 3:
                    print("Here's the list of valid Emails:")
                    for i in self.validator.get_emails():
                        print(i)
                elif user == 4:
                    print("Here's the last and first names in record:")
                    print(f"First Name" + " " * 10 + "| Last Name")
                    j = 0
                    for i in self.validator.firstnames:
                        if j < len(self.validator.lastnames):
                            print(f"{i:<20}| {self.validator.lastnames[j]}")
                            j += 1
                        else:
                            print(f"{i:<20}|")

                else:
                    print("How did you get here? "
                          "Error should cover anything that isn't 0-4. "
                          "Oh well, Back to the Drawing Board")
