#!/usr/bin/env python3
"""
The module for the Root Parent Class of the password generator
"""

__author__ = 'Ayden Riddle'
__version__ = '1.0'
__date__ = '2023.05.03'
__status__ = 'Finished'


class PasswordValidator:
    """
    The Main Parent class of the Password Generator
    Intended to be a basic validator for the passwords requirements
    """
    LINE = "=" * 30  # For Text flavor in debug and if using this class as not a generator
    __MIN_NUMBERS = 2  # The Minimum amount of numbers required in a password
    __MIN_CAP_LETTERS = 1  # The Minimum amount of capital letters required in a password
    __MIN_LOW_LETTERS = 2  # The Minimum amount of lowercase letters required in a password
    MIN_SPEC_LETTERS = 2    # The Minimum amount of special characters required in a password
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  # For checking if a character is in the Alphabet
    NUMBERS = "0123456789"  # For checking if a character is a number

    def __init__(self, password=None, debug=False, generator=False):
        """
        The main initialization of the Password validator
        :param password: A preset string in case you wanted to preset a password to test the individual methods
        :param debug: A boolean that enables the values and method names to the user
        :param generator: A boolean that when enabled removes user interface for rapid looping functions
        """
        self.password = password
        self.debug = debug  # For general debug information
        self.generator = generator  # to prevent text in password_generator.py
        self.valid = False  # Guilty until is_valid is running

    def is_valid(self, password=None):
        """
        The main method that goes through every code and makes sure the password is a valid password
        :param password:
        :return:
        """
        self.valid = True  # Innocent until proven invalid
        if self.debug:
            print(f"Debug: Starting {self.__ne__}.{self.is_valid.__name__}")

        print(PasswordValidator.LINE)
        if password is None:  # In case the password has no value
            print("Password has no Value, using stored password")
            print(PasswordValidator.LINE)
        elif password is None and self.password is None:  # In case Both have no value
            print("ERROR: Password and stored password have no Value.")
            print(PasswordValidator.LINE)
            return
        else:
            self.password = password
        print(f"Here is your password: {self.password}")
        print(PasswordValidator.LINE)

        if self.is_caps_valid():
            print("Caps Valid")
        else:
            print("Caps Invalid")
            self.valid = False
        print(PasswordValidator.LINE)

        if self.is_low_valid():
            print("Low Valid")
        else:
            print("Low Invalid")
            self.valid = False
        print(PasswordValidator.LINE)

        if self.is_num_valid():
            print("Num Valid")
        else:
            print("Num Invalid")
            self.valid = False
        print(PasswordValidator.LINE)

        if self.is_spec_valid():
            print("Spec Valid")
        else:
            print("Spec Invalid")
            self.valid = False
        print(PasswordValidator.LINE)

        if self.valid and "PasswordValidator" in str(self.__ne__):
            print(f"{self.password} is a Valid Password for the Basic Password Validator")
        elif not self.valid and "PasswordValidator" in str(self.__ne__):
            print(f"{self.password} is an Invalid Password for the Basic Password Validator")

    def is_caps_valid(self):
        """
        Checks if there are the required amount of capital letters for __MIN_CAP_LETTERS.
        MAKE SURE self.password isn't None
        :return: True or False
        """
        if self.debug:
            print(f"Debug: Starting {self.is_caps_valid.__name__}")
        count = 0
        for i in self.password:
            if i.isupper():
                count += 1
        if not self.generator:
            print(f"Your password has {count} CAPITAL LETTER(S)")
            print(f"You need {PasswordValidator.__MIN_CAP_LETTERS} CAPITAL LETTER(S)")
        if count >= PasswordValidator.__MIN_CAP_LETTERS:

            return True
        else:
            return False

    def is_low_valid(self):
        """
                Checks if there are the required amount of lowercase letters for __MIN_LOW_LETTERS.
                MAKE SURE self.password isn't None
                :return: True or False
                """
        if self.debug:
            print(f"Debug: Starting {self.is_low_valid.__name__}")
        count = 0
        for i in self.password:  # for each character in the password string
            if i.islower():
                count += 1
        if not self.generator:
            print(f"Your password has {count} lowercase letter(s)")
            print(f"You need {PasswordValidator.__MIN_LOW_LETTERS} lowercase letter(s)")

        if count >= PasswordValidator.__MIN_LOW_LETTERS:

            return True
        else:
            return False

    def is_num_valid(self):
        """
                Checks if there are the required amount of numbers for __MIN_NUMBERS.
                MAKE SURE self.password isn't None
                :return: True or False
        """
        if self.debug:
            print(f"Debug: Starting {self.is_num_valid.__name__}")
        count = 0
        for i in self.password:
            if i in PasswordValidator.NUMBERS:
                count += 1
        if not self.generator:
            print(f"Your password has {count} Number(s)")
            print(f"You need {PasswordValidator.__MIN_NUMBERS} Number(s)")
        if count >= PasswordValidator.__MIN_NUMBERS:
            return True
        else:
            return False

    def is_spec_valid(self):
        """
                Checks if there are the required amount of special characters for __MIN_SPEC_LETTERS.
                MAKE SURE self.password isn't None
                :return: True or False
        """
        if self.debug:
            print(f"Debug: Starting {self.is_spec_valid.__name__}.")
        count = 0
        for i in self.password:
            if i not in PasswordValidator.ALPHABET and i not in PasswordValidator.NUMBERS:
                count += 1
        if not self.generator:
            print(f"Your password has {count} Special Character(s)")
            print(f"You need {PasswordValidator.MIN_SPEC_LETTERS} Special Character(s)")
        if count >= PasswordValidator.MIN_SPEC_LETTERS:
            return True
        else:
            return False
