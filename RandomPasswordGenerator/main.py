#!/usr/bin/env python3

__author__ = 'Ayden Riddle'
__version__ = '1.0'
__date__ = '2023.05.03'
__status__ = 'Finished'

import password_generator as pg
import password_validator as pv
import advanced_validator as av

def main():
    pass_gen = pg.PasswordGenerator()
    pass_gen.generate_password()
    pass_val = pv.PasswordValidator(pass_gen.password, debug=True)
    pass_val.is_valid()
    adv_val = av.AdvancedValidator(pass_gen.password, debug=True)
    adv_val.is_valid()


if __name__ == '__main__':
    # help('main_menu')  # used to display the script's docstring
    main()
