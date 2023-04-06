class PasswordValidator:
    __MIN_NUMBERS = 2
    __MIN_CAP_LETTERS = 2
    __MIN_LOW_LETTERS = 2

    def __init__(self, password=None, debug=False):
        self.password = password
        self.debug = debug

    def is_valid(self, password):
        self.password = password
        if self.password is None:
            print("Password has no Value")
        else:
            print(f"Here is your password: {self.password}")
        if self.is_caps_valid():
            print("Caps Valid")
        else:
            print("Not Caps Valid")

    def is_caps_valid(self):
        count = 0
        for i in self.password:
            if i.isupper():
                count += 1
        if count >= PasswordValidator.__MIN_CAP_LETTERS:
            return True
        else:
            return False
