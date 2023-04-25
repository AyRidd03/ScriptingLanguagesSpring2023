import password_validator as pv


def main():
    pass_val = pv.PasswordValidator(debug=True)
    insert = input("Please put in a password: ")
    pass_val.is_valid(insert)


if __name__ == '__main__':
    # help('main_menu')  # used to display the script's docstring
    main()