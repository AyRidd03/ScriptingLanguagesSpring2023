#!/usr/bin/env python3

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Ayden Riddle'
__version__ = '1.0'
__date__ = '2023.04.25'
__status__ = 'Development'
import re


class FileValidator:
    def __init__(self, files=[]):
        self.files = files

    def add_file(self, file):
        self.files.append(file)

    def open_files(self):
            for fname in self.files:
                try:
                    with open(fname) as f:
                        self.data_validate(f)
                except:
                    print(f"Error, {fname} could not be opened.")

    def data_validate(self, file):
        """
        Takes the given file and searches for pieces of data divided by strings and checks for valid data
        :param file:
        :return:
        """
        print(f"File {file.name} Opened")
        data = file.read()


    def phonevalid(self, phone):
        """
        Validates the Input String phone and makes sure it is a phone Number with dashes or dots
        :param phone:
        :return: True or False
        """
        regex = re.compile(r'([0-9]{3})([-_.])([0-9]{3})([-_.])([0-9]{4})')
        if re.fullmatch(regex, phone):
            print(f"{phone} is a valid phone #")
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
            return True
        else:
            print(f"{email} is an invalid email")
            return False
