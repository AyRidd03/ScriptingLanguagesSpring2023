#!/usr/bin/env python3

__author__ = 'Ayden Riddle'
__version__ = '1.0'
__date__ = '2023.05.03'
__status__ = 'Finished'

import password_generator as pg


def main():
    pass_gen = pg.PasswordGenerator()
    pass_gen.generate_password()


if __name__ == '__main__':
    # help('main_menu')  # used to display the script's docstring
    main()
