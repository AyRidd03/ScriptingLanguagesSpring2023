#!/usr/bin/env python3

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Ayden Riddle'
__version__ = '1.1'
__date__ = '2023.04.25'
__status__ = 'Development'

import csv
import re

LINE = "=" * 50


class FileValidator:
    def __init__(self, files=[]):
        self.files = files
        self.phone_numbers = []
        self.emails = []
        self.firstname = []
        self.lastname = []
        self.valid_data = {"#": [], "L_Name": [], "F_Name": [], "Number": [], "Email": []}
        self.invalid_data = {"#": [], "L_Name": [], "F_Name": [], "Number": [], "Email": []}
    def add_file(self, file):
        self.files.append(file)
        print(f"{file} has been added to the list of files")

    def open_files(self):
        for fname in self.files:
            try:
                self.open_file(fname)
            except StopIteration:
                print(f"ERROR: {fname} had a Stop Iteration Error and could not be continued.")
            except FileNotFoundError:
                print(f"ERROR: {fname} could not be found.")
            except:
                print(f"ERROR {fname} had an error and could not be opened or continued.")
        print(LINE)

    def open_file(self, fname):
        try:
            self.file = open(fname, "r")
            print(f"File {self.file.name} Opened")
        except StopIteration:
            print(f"ERROR: {fname} had a Stop Iteration Error and could not be continued.")
        except FileNotFoundError:
            print(f"ERROR: {fname} could not be found.")
        except:
            print(f"ERROR {fname} had an error and could not be opened or continued.")

    def write_file(self, fname, data):
        try:
            print("opening file")
            with open(fname, 'r', newline="") as self.file:
                print("Making Reader")
                reader = csv.reader(self.file, delimiter=",")
                print("Using reader")
                fieldnames = reader.__next__()
            print("opening file")
            with open(fname, 'w', newline='') as self.file:
                print("Making Writer")
                writer = csv.DictWriter(self.file, fieldnames=fieldnames)
                print("Writing Header")
                writer.writeheader()
                print("Writing Data")
                writer.writerow(data)
        except:
            print(f"An Error has occured in Writing to {fname}")

    def read_file(self, fname):
        try:
            with open(fname, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in reader:
                    print(', '.join(row))
        except:
            print(f"An Error has occured in Reading {fname}")

    def file_validate(self, fname):
        """
        Takes the given file and searches for pieces of data divided by strings and checks for valid data
        :param file:
        :return:
        """
        self.open_file(fname)
        data = list(csv.reader(self.file, delimiter=","))
        self.file.close()
        headers = data[1]
        print(data)
        print(LINE)
        for i in data:
            self.valid_data.update({headers[1]: i[1]})
            self.invalid_data.update({headers[1]: i[1]})

            if self.name_valid((i[2],i[3])):
                self.valid_data.update({headers[2]: i[2]})
                self.valid_data.update({headers[3]: i[3]})
            else:
                self.invalid_data.update({headers[2]: i[2]})
                self.invalid_data.update({headers[3]: i[3]})

            if self.phone_valid(i[3]):
                self.valid_data.update({headers[3]: i[3]})
            else:
                self.invalid_data.update({headers[3]: i[3]})

            if self.email_valid(i[4]):
                self.valid_data.update({headers[4]: i[4]})
            else:
                self.invalid_data.update({headers[4]: i[4]})
    def reset_data(self):
        """
        Clears the Dictionaries to get ready for the next line of data
        :return:
        """
        self.valid_data = {"#": [], "L_Name": [], "F_Name": [], "Number": [], "Email": []}
        self.invalid_data = {"#": [], "L_Name": [], "F_Name": [], "Number": [], "Email": []}

    def name_valid(self, name):
        """
        Validates the Input Tuple of strings to make sure they are either a first or last name
        :param name: Tuple with Last,First Name
        :return: True or false
        """
        last_name, first_name = name
        regex = re.compile(r'([A-Z])*([a-z])')
        if re.fullmatch(regex, last_name):
            print(f"{last_name} is a valid last name")
            if name not in self.phone_numbers:
                print("Adding to list of last names")
                self.phone_numbers.append(name)
            else:
                print("This last name is already Added")
        else:
            print(f"{name} is an invalid last name")
            return False

        if re.fullmatch(regex, first_name):
            print(f"{first_name} is a valid last name")
            if first_name not in self.phone_numbers:
                print("Adding to list of last names")
                self.phone_numbers.append(name)
            else:
                print("This first name is already Added")
        else:
            print(f"{name} is an invalid last name")
            return False

        return True  # Down here so it doesn't get lost

    def phone_valid(self, phone):
        """
        Validates the Input String phone and makes sure it is a phone Number with dashes or dots
        :param phone:
        :return: True or False
        """
        regex = re.compile(r'([0-9]{3})([-_.])([0-9]{3})([-_.])([0-9]{4})')
        if re.fullmatch(regex, phone):
            print(f"{phone} is a valid phone #")
            if phone not in self.phone_numbers:
                print("Adding to list of Phone #'s")
                self.phone_numbers.append(phone)
            else:
                print("This Phone # is already Added")
                return False
            return True
        else:
            print(f"{phone} is an invalid phone #")
            return False

    def emailvalid(self, email):
        """
        Validates an Input String to make sure it is an email
        :param email:
        :return: True or False
        """
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if re.fullmatch(regex, email):
            print(f"{email} is a valid email")
            if email not in self.emails:
                print("Adding to list of Emails")
                self.emails.append(email)
            else:
                print("This Email is already Added")
                return False
            return True
        else:
            print(f"{email} is an invalid email")
            return False

    def get_phone_numbers(self):
        return self.phone_numbers

    def get_emails(self):
        return self.emails

    def get_file_names(self):
        return self.files
