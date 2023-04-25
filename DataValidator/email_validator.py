import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def emailValid(email):
    if re.fullmatch(regex, email):
        print("The given mail is valid")
    else:
        print("The given mail is invalid")