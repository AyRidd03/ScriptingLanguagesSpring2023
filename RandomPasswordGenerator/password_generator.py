import advanced_validator as av
import random as r
import string as s


class PasswordGenerator(av.AdvancedValidator):
    def __init__(self, generator=True, debug=False):
        av.AdvancedValidator.__init__(self, generator=generator, debug=debug)

    def generate_password(self):
        while True:
            self.password = ''.join(r.choices(s.ascii_letters + s.digits + s.punctuation,
                                              k=int(r.random() * av.AdvancedValidator.MIN_LENGTH +
                                                    av.AdvancedValidator.MAX_LENGTH - av.AdvancedValidator.MIN_LENGTH)))
            if self.is_valid(self.password):
                print(f"Here is your Password: {self.password}")
                return
    def is_valid(self, password):
        return av.AdvancedValidator.is_length_valid(self) and av.AdvancedValidator.is_low_valid(self) \
            and av.AdvancedValidator.is_num_valid(self) and av.AdvancedValidator.is_caps_valid(self) \
            and av.AdvancedValidator.is_spec_valid(self)
