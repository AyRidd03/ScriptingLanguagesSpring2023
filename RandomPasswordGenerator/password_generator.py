#!/usr/bin/env python3
"""
The Module for the Password Generator
"""
__author__ = 'Ayden Riddle'
__version__ = '1.0'
__date__ = '2023.05.03'
__status__ = 'Finished'

import advanced_validator as av
import random as r
import string as s


class PasswordGenerator(av.AdvancedValidator):
    """
    The Class intended to be used to generate passwords based on PasswordValidator and AdvancedValidator's
    specifications.
    """
    def __init__(self, generator=True, debug=False):
        av.AdvancedValidator.__init__(self, generator=generator, debug=debug)

    def generate_password(self):
        """
                The Password Generator that will give a valid value for self.password based on the requirements of
                Advanced Validator and Password Validator.
                :return:
        """
        while True:
            self.password = ''.join(r.choices(s.ascii_letters + s.digits + s.punctuation,
                                              k=int(r.random() * av.AdvancedValidator.MIN_LENGTH +
                                                    av.AdvancedValidator.MAX_LENGTH - av.AdvancedValidator.MIN_LENGTH)))
            if self.is_valid(self.password):
                print(f"Here is your Password: {self.password}")
                return

    def is_valid(self, password=None):
        return av.AdvancedValidator.is_length_valid(self) and av.AdvancedValidator.is_low_valid(self) \
            and av.AdvancedValidator.is_num_valid(self) and av.AdvancedValidator.is_caps_valid(self) \
            and av.AdvancedValidator.is_spec_valid(self)
