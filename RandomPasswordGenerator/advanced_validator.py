#!/usr/bin/env python3
"""
The Module for the Advanced Password Validator
"""

__author__ = 'Ayden Riddle'
__version__ = '1.0'
__date__ = '2023.05.03'
__status__ = 'Finished'

import password_validator as pv


class AdvancedValidator(pv.PasswordValidator):
    """
    The Child of PasswordValidator and the Parent of PasswordGenerator.
    Intended to have additional Parameters and Special Requirements.
    """
    MIN_LENGTH = 7
    MAX_LENGTH = 15
    __SPECIAL_CHARS = "-_;,."

    def __init__(self, password=None, debug=False, generator=False):
        pv.PasswordValidator.__init__(self, password=password, debug=debug, generator=generator)

    def is_valid(self, password=None):
        pv.PasswordValidator.is_valid(self, password)
        if self.is_length_valid():
            print("Length Valid")
        else:
            print("Length Invalid")
            self.valid = False
        print(pv.PasswordValidator.LINE)
        if self.valid:
            print(f"{self.password} is a Valid Password for the Advanced Password Validator")
        else:
            print(f"{self.password} is an Invalid Password for the Advanced Password Validator")

    def is_length_valid(self):
        """
                Checks if self.password is the required length for MIN_LENGTH and MAX_LENGTH.
                MAKE SURE self.password isn't None
                :return: True or False
        """
        if self.debug:
            print(f"Debug: Starting {self.is_length_valid.__name__}")
        count = 0
        for i in self.password:
            count += 1
        if not self.generator:
            print(f"Your password has {count} length")
            print(f"You need {AdvancedValidator.MIN_LENGTH} minimum characters, "
                  f"but not over {AdvancedValidator.MAX_LENGTH}")
        if AdvancedValidator.MIN_LENGTH <= count <= AdvancedValidator.MAX_LENGTH:
            return True
        else:
            return False

    def is_spec_valid(self):
        if self.debug:
            print(f"Debug: Starting {self.is_spec_valid.__name__}.")
        count = 0
        for i in self.password:
            count += 1 if i in AdvancedValidator.__SPECIAL_CHARS else 0
            if i not in AdvancedValidator.__SPECIAL_CHARS \
                    and i not in pv.PasswordValidator.ALPHABET \
                    and i not in pv.PasswordValidator.NUMBERS:
                if not self.generator:
                    print(f"Your password has a Special Character(s) not within {AdvancedValidator.__SPECIAL_CHARS}")
                return False
        if not self.generator:
            print(f"Your password has {count} Special Character(s) within {AdvancedValidator.__SPECIAL_CHARS}")
            print(f"You need {pv.PasswordValidator.MIN_SPEC_LETTERS} Special Character(s)")
        if count >= pv.PasswordValidator.MIN_SPEC_LETTERS:
            return True
        else:
            return False
