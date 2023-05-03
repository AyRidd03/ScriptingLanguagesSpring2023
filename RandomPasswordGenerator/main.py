import password_validator as pv
import advanced_validator as av


def main():
    pass_val = av.AdvancedValidator(debug=True)
    insert = input("Please put in a password: ")
    pass_val.is_valid(insert)


if __name__ == '__main__':
    # help('main_menu')  # used to display the script's docstring
    main()
