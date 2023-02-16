#!/usr/bin/env python3

"""
the validation module for all user input.
"""

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Debbie Johnson'
__version__ = '1.0'
__date__ = '2023.02.14'
__status__ = 'Development'


def get_string(prompt):
    """
    Display an input prompt to get a string value, which can not be an empty string
    and loop again if invalid

    :param prompt: the text that will be used for the user's input prompt
    :return: the user's input as a string
    """

    while True:
        user_input = input(f'{prompt}: ')

        if user_input > '':
            return user_input

        print('Invalid Input: Please enter a value!')


def get_num(prompt, data_type='int'):
    """
    Display an input prompt to get a number from the user, and convert it to an int or float
    and loop again if invalid
    :param prompt: the text that will be used for the user's input prompt
    :param data_type: a string indicating how the user input will be converted to (default=int or float)
    :return: the user's input as a number that will be either an int or float
    """

    while True:
        user_input = input(f'{prompt}: ')

        try:
            if data_type == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            return number

        except ValueError:
            print('Invalid Input: Please enter a number')


def get_positive_num(prompt, data_type='int'):
    """
    Display an input prompt to get a positive number from the user, and convert it to an int or float
    and loop again if invalid

    :param prompt: the text that will be used for the user's input prompt
    :param data_type: a string indicating how the user input will be converted to (default=int or float)
    :return: the user's input as a number that will be either an int or float
    """

    while True:
        user_input = input(f'{prompt}: ')

        try:
            if data_type == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            if number > 0:
                return number
            else:
                print(f'Invalid Input: Please enter a positive number')

        except ValueError:
            print('Invalid Input: Please enter a number')


def get_range(prompt, low, high, data_type='int'):
    """
    Display an input prompt to get a number from the user within an acceptable range, and convert it to an int or float
    and loop again if invalid

    :param prompt: the text that will be used for the user's input prompt
    :param low: the lowest possible numeric value
    :param high: the highest possible numeric value
    :param data_type: a string indicating how the user input will be converted to (default=int or float)
    :return: the user's input as a number that will be either an int or float
    """

    while True:
        user_input = input(f'{prompt} (Valid {low}-{high}): ')

        try:
            if data_type == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            if low <= number <= high:
                return number
            else:
                print(f'Invalid Input: Please enter a number greater or equal to {low} '
                      f'and less than or equal to {high}')

        except ValueError:
            print('Invalid Input: Please enter a number')


def get_yes_no(prompt='(y=Yes, n=No):'):
    """
    Display an input prompt to get a yes/no answer from the user (valid lower cased inputs are y, yes, n, no)
    and loop again if invalid

    :param prompt: user's prompt if one is passed otherwise the default is
    :return: true for yes or false for no
    """

    while True:
        user_input = input(f'{prompt} (y=Yes, n=No): ').lower()

        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print('Invalid Input: Please enter a y=yes, or n=no')


# if this is the module where the program started from, then display the module docstring
if __name__ == '__main__':
    help('validation')
