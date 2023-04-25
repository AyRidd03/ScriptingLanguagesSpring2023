class PasswordValidator:
    LINE = "=" * 30
    __MIN_NUMBERS = 2
    __MIN_CAP_LETTERS = 2
    __MIN_LOW_LETTERS = 2
    __MIN_SPEC_LETTERS = 2
    __ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    __NUMBERS = "0123456789"

    def __init__(self, password=None, debug=False):
        self.password = password
        self.debug = debug

    def is_valid(self, password):
        if self.debug:
            print(f"Debug: Starting {self.is_valid.__name__}")
        self.password = password
        print(PasswordValidator.LINE)
        if self.password is None:
            print("Password has no Value")
            print(PasswordValidator.LINE)
            return
        else:
            print(f"Here is your password: {self.password}")
        print(PasswordValidator.LINE)

        if self.is_caps_valid():
            print("Caps Valid")
        else:
            print("Caps Invalid")
        print(PasswordValidator.LINE)

        if self.is_low_valid():
            print("Low Valid")
        else:
            print("Low Invalid")
        print(PasswordValidator.LINE)

        if self.is_num_valid():
            print("Num Valid")
        else:
            print("Num Invalid")
        print(PasswordValidator.LINE)

        if self.is_spec_valid():
            print("Spec Valid")
        else:
            print("Spec Invalid")
        print(PasswordValidator.LINE)

    def is_caps_valid(self):
        if self.debug:
            print(f"Debug: Starting {self.is_caps_valid.__name__}")
        count = 0
        for i in self.password:
            if i.isupper():
                count += 1
        print(f"Your password has {count} CAPITAL LETTER(S)")
        print(f"You need {PasswordValidator.__MIN_CAP_LETTERS} CAPITAL LETTER(S)")
        if count >= PasswordValidator.__MIN_CAP_LETTERS:

            return True
        else:
            return False

    def is_low_valid(self):
        if self.debug:
            print(f"Debug: Starting {self.is_low_valid.__name__}")
        count = 0
        for i in self.password:
            if i.islower():
                count += 1
        print(f"Your password has {count} lowercase letter(s)")
        print(f"You need {PasswordValidator.__MIN_LOW_LETTERS} lowercase letter(s)")
        if count >= PasswordValidator.__MIN_LOW_LETTERS:

            return True
        else:
            return False

    def is_num_valid(self):
        if self.debug:
            print(f"Debug: Starting {self.is_num_valid.__name__}")
        count = 0
        for i in self.password:
            if i in PasswordValidator.__NUMBERS:
                count += 1
        print(f"Your password has {count} Number(s)")
        print(f"You need {PasswordValidator.__MIN_NUMBERS} Number(s)")
        if count >= PasswordValidator.__MIN_NUMBERS:
            return True
        else:
            return False

    def is_spec_valid(self):
        if self.debug:
            print(f"Debug: Starting {self.__ne__} . {self.is_spec_valid.__name__}")
        count = 0
        for i in self.password:
            if i not in PasswordValidator.__ALPHABET and i not in PasswordValidator.__NUMBERS:
                count += 1
        print(f"Your password has {count} Special Character(s)")
        print(f"You need {PasswordValidator.__MIN_SPEC_LETTERS} Special Character(s)")
        if count >= PasswordValidator.__MIN_SPEC_LETTERS:
            return True
        else:
            return False
