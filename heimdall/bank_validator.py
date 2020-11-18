import re
from heimdall.base_validate_error import InvalidCodeBank

class BankValidator():
    def __init__(self, bank_code):
        self.bank_code = bank_code

    def start(self):
        switcher = {
            '001': 'Banco do Brasil',
            '237': 'Bradesco',
            '341': 'Itaú',
            '033': 'Santander',
            '745': 'Citibank',
            '399': 'HSBC',
            '041': 'Banrisul'
        }

        bank_valid = switcher.get(self.bank_code)

        if not bank_valid:
            return self.valid_bank_generic()

        return bank_valid

    def valid_bank_generic(self):
        regex = re.compile('^([0-9A-Za-x]{3,5})$', re.I)
        match = bool(regex.match(self.bank_code))

        if match == False:
            raise InvalidCodeBank()

        return self.bank_code