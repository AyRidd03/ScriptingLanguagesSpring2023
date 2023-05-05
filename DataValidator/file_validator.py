#!/usr/bin/env python3

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Ayden Riddle'
__version__ = '1.5'
__date__ = '2023.05.04'
__status__ = 'Finished'

import csv
import re

LINE = "=" * 50


class FileValidator:
    def __init__(self, files=[], debug=False):
        self.files = files  # The list of file names
        self.file = None  # the main name of the open file
        self.debug = debug
        # These are the lists of valid data pieces to prevent repetition
        self.phone_numbers = []
        self.emails = []
        self.firstnames = []
        self.lastnames = []
        self.names = []

        # These libraries are to help with storing data in the invalid and valid files
        self.valid_data = {"#": [], "L_Name": [], "F_Name": [], "Number": [], "Email": []}
        self.invalid_data = {"#": [], "L_Name": [], "F_Name": [], "Number": [], "Email": []}

    def add_file(self, file):
        if self.file_name_valid(file):
            self.files.append(file)
            print(f"{file} has been added to the list of files")
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

    def save_to_file(self, fname, data):
        try:
            if self.debug:
                print(f"Debug Mode: Starting {self.save_to_file.__name__()}")
                print(LINE)
                print(f"We are writing to {fname}")
                print("Here's the inputed data:")
                print(data)
                print("opening file")

            with open(fname, 'r', newline="") as self.file:

                if self.debug:
                    print("Making Reader")

                reader = list(csv.reader(self.file, delimiter=',', quotechar='|'))
                fieldnames = reader[0]
                saved_data = []

                if self.debug:
                    print("Using Reader")

                for row in reader:
                    if row == reader[0]:
                        continue
                    old_data = {}
                    count = 0
                    for i in fieldnames:
                        old_data.update({i: row[count]})
                        count += 1
                    if self.debug:
                        print(f"Old data line: {old_data}")
                    if data == old_data:
                        continue
                    saved_data.append(old_data)
                if self.debug:
                    print(LINE)
                    print("Saved Data:")
                    print(saved_data)

                    print("opening file")
            with open(fname, 'w', newline='') as self.file:
                if self.debug:
                    print("Making Writer")
                writer = csv.DictWriter(self.file, fieldnames=fieldnames)
                if self.debug:
                    print("Writing Header")
                writer.writeheader()
                if self.debug:
                    print("Writing Old Data")
                writer.writerows(saved_data)
                print(f"Writing Data to {fname}")
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
        headers = data[0]
        print(data)
        print(LINE)
        for i in data:
            if i == data[0]:
                continue
            self.valid_data.update({headers[0]: i[0]})
            self.invalid_data.update({headers[0]: i[0]})

            if self.name_valid((i[1], i[2])):
                self.valid_data.update({headers[1]: i[1]})
                self.valid_data.update({headers[2]: i[2]})
                self.invalid_data.update({headers[1]: "None"})
                self.invalid_data.update({headers[2]: "None"})
            else:
                self.valid_data.update({headers[1]: "None"})
                self.valid_data.update({headers[2]: "None"})
                self.invalid_data.update({headers[1]: i[1]})
                self.invalid_data.update({headers[2]: i[2]})

            if self.phone_valid(i[3]):
                self.valid_data.update({headers[3]: i[3]})
                self.invalid_data.update({headers[3]: "None"})
            else:
                self.valid_data.update({headers[3]: "None"})
                self.invalid_data.update({headers[3]: i[3]})

            if self.email_valid(i[4]):
                self.valid_data.update({headers[4]: i[4]})
                self.invalid_data.update({headers[4]: "None"})
            else:
                self.valid_data.update({headers[4]: "None"})
                self.invalid_data.update({headers[4]: i[4]})

            self.save_to_file("invalid.csv", self.invalid_data)
            self.save_to_file("valid.csv", self.valid_data)
            self.reset_data()
            print(LINE)
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
        regex = re.compile(r'([A-Z])([a-z]{2,})')
        if name in self.names:
            print(f"{first_name} {last_name} is already added")
            return True

        if re.fullmatch(regex, last_name):
            print(f"{last_name} is a valid last name")
            if last_name not in self.lastnames:
                print("Adding to list of last names")
                self.lastnames.append(last_name)
            else:
                print("This last name is already Added")
        else:
            print(f"{last_name} is an invalid last name")
            return False

        if re.fullmatch(regex, first_name):
            print(f"{first_name} is a valid first name")
            if first_name not in self.firstnames:
                print("Adding to list of last names")
                self.firstnames.append(first_name)
            else:
                print("This first name is already Added")
        else:
            print(f"{first_name} is an invalid first name")
            return False
        self.names.append((last_name, first_name))
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
            return True
        else:
            print(f"{phone} is an invalid phone #")
            return False

    def email_valid(self, email):
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
            return True
        else:
            print(f"{email} is an invalid email")
            return False

    def file_name_valid(self, fname):
        """
               Validates an Input String to make sure it is a valid file name
               :param fname:
               :return: True or False
               """
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if re.fullmatch(regex, fname):
            print(f"{fname} is a valid file name")
            if fname not in self.files:
                print("Adding to list of Files")
                self.emails.append(fname)
            else:
                print("This File is already Added")
            return True
        else:
            print(f"{fname} is an invalid file name")
            return False
    def get_phone_numbers(self):
        return self.phone_numbers

    def get_emails(self):
        return self.emails

    def get_file_names(self):
        return self.files
