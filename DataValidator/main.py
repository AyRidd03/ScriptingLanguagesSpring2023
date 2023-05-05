#!/usr/bin/env python3

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Ayden Riddle'
__version__ = '1.1'
__date__ = '2023.04.25'
__status__ = 'Development'

import file_validator as fv
import validator_menu as vm
def main():
    menu = vm.Menu()
    menu.main_menu()


if __name__ == '__main__':
    # help('main_menu')  # used to display the script's docstring
    main()
