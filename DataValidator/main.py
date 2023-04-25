#!/usr/bin/env python3

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Ayden Riddle'
__version__ = '1.0'
__date__ = '2023.04.25'
__status__ = 'Development'
import file_validator as fv
def main():
    print("Hi")
    file_check = fv.FileValidator()
    file_check.add_file("hello.csv")
    file_check.add_file("bop")
    file_check.open_files()
    file_check.emailvalid("audentheninja@gmail.com")
    file_check.phonevalid("402_639_4850")

if __name__ == '__main__':
    # help('main_menu')  # used to display the script's docstring
    main()