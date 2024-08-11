import random
import random as tel

class Help:
    @staticmethod
    def random_telephone():
        country_code = '+7'
        operator_code = '926'
        last_digits = random.randint(1000000, 9999999)
        fake_number = country_code + str(operator_code) + str(last_digits)
        return fake_number