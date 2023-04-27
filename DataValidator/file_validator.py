#!/usr/bin/env python3

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Ayden Riddle'
__version__ = '1.0'
__date__ = '2023.04.25'
__status__ = 'Development'

import csv
import re

LINE = "=" * 40


class FileValidator:
    def __init__(self, files=[]):
        self.files = files
        self.phone_numbers = []
        self.emails = []

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
            print(f"File {file.name} Opened")
        except StopIteration:
            print(f"ERROR: {fname} had a Stop Iteration Error and could not be continued.")
        except FileNotFoundError:
            print(f"ERROR: {fname} could not be found.")
        except:
            print(f"ERROR {fname} had an error and could not be opened or continued.")
        print(LINE)
    def data_validate(self, fname):
        """
        Takes the given file and searches for pieces of data divided by strings and checks for valid data
        :param file:
        :return:
        """
        self.open_file(fname)
        data = list(csv.reader(self.file, delimiter=","))
        self.file.close()
        print(data)
        print(LINE)

        print(LINE)
        for i in data:
            for piece in i:
                if self.phonevalid(piece):
                    self.phone_numbers.append(piece)
                elif self.emailvalid(piece):
                    self.emails.append(piece)
                else:
                    print(f"{piece}, is not a valid piece of data")
                print(LINE)

    def phonevalid(self, phone):
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
