import pygame
import file_validator as fv


class Menu:
    def __init__(self):
        self.validator = fv.FileValidator()

    def main_menu(self):
        while True:
            print(fv.LINE)
            print("Welcome to the Main Menu! Here are your Options:")
            print("1: Add a File")
            print("2: Open Files")
            print("3: Validate File Data")
            print("4: Edit the Data of a File")
            print("5: Validate a piece of Data outside of a file")
            print("0: Exit")
            print(fv.LINE)
            while True:
                try:
                    user = input("Please insert a number between 0-5: ")
                    user = int(user)
                    if user < 0 or user > 5:
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
                print("Adding File")
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

    def add_file(self):
        file = input("Please insert the File Name/ Path")
        self.validator.add_file(file)

    def open_file(self):
        print(self.validator.get_file_names())
        user = input("Please Choose a File to Open or Type All for all: ")
        if user in self.validator.get_file_names():
            self.validator.open_file(user)
        elif user == "All":
            self.validator.open_files()
        else:
            print("ERROR: Not a valid input, returning to Main Menu")

    def validate_file(self):
        print(self.validator.get_file_names())
        user = input("Please Choose a File to Open or Type All for all: ")
        if user in self.validator.get_file_names():
            self.validator.data_validate(user)
        elif user == "All":
            for i in self.validator.get_file_names():
                self.validator.data_validate(i)
        else:
            print("ERROR: Not a valid input, returning to Main Menu")
