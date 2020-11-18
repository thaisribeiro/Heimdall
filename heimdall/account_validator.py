import re
from generic_validators import GenericValidators
from common_validate import CommonValidate
from base_validate_error import InvalidAgencyNumber, InvalidDigitAgencyNumber,InvalidAccountNumber, InvalidDigitAccountNumber, InvalidCodeBankP 
from calculate_number_account_agency import CalculateNumberAccount, CalculateNumberAgency
class AccountValidator(CommonValidate):
    def __init__(self, config):
        self.config = config

    def start(self):
        try:
            bank_code = self.config.get('bank_code')
            account_code = self.config.get('account_code')

            switcher = {
                '001': AccountValidator.valid_account_bb,
                '237': AccountValidator.valid_account_bradesco,
                '341': AccountValidator.valid_account_itau,
                '033': AccountValidator.valid_account_santander,
                '745': AccountValidator.valid_account_citibank,
                '041': AccountValidator.valid_account_banrisul
            }
            
            result = switcher.get(bank_code)()

            if not result:
                return self.valid_account_generic()

            return result
        except Exception:
            print('Erro')
    
    def valid_account_generic(self):
        return {}

    def valid_account_bb(self):
        """
          Valida a conta e o dígito verificador do Banco do Brasil
          Tamanho da Conta - 8 Dígitos + 1 DV
        """
        account = self.config('account')

        if len(account) < 9:
            raise InvalidAccountNumber(9)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        calculate_account = CalculateNumberAccount(account).caculate_number_account_bb()

        if not calculate_account:
            raise InvalidDigitAccountNumber()

        return True

    def valid_account_itau(self):
        """
          Valida a conta e o dígito verificador do banco Itaú
          Tamanho da Conta - 5 Dígitos + 1 DV
        """
        account = self.config('account')

        if len(account) < 6:
            raise InvalidAccountNumber(6)
        
        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()
        
        account_agency = account + self.config('agency')
        calculate_account = CalculateNumberAccount(account_agency).calculate_number_account_itau()
        
        if not calculate_account:
            raise InvalidAccountNumber()
        
        return True

    def valid_account_bradesco(self):
        """
          Valida a conta e o dígito verificador do banco Bradesco
          Tamanho da Conta - 7 Dígitos + 1 DV
        """
        account = self.config('account')

        if len(account) < 8:
            raise InvalidAccountNumber(8)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        calculate_account = CalculateNumberAccount(account).calculate_number_account_bradesco()

        if not calculate_account:
            raise InvalidDigitAccountNumber()

        return True

    def valid_account_santander(self):
        """
          Valida a conta e o dígito verificador do banco Santander
          Tamanho da Conta - 8 dígitos + 1 DV
        """
        account = self.config('account')

        if len(account) < 9:
            raise InvalidAccountNumber(9)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        calculate_account = CalculateNumberAccount(account).calculate_number_account_santander()

        if not calculate_account:
            raise InvalidDigitAccountNumber()

        return True

    def valid_account_citibank(self):
        """
          Valida a conta e o dígito verificador do banco Banrisul
          Tamanho da Conta - 7 Dígitos + 1 DV
        """
        account = self.config('account')

        if len(account) < 8:
            raise InvalidAccountNumber(8)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        calculate_account = CalculateNumberAccount(account).calculate_number_account_citibank()

        if not calculate_account:
            raise InvalidDigitAccountNumber()

        return True
    
    def valid_account_banrisul(self):
        """
          Valida a conta e o dígito verificador do banco Banrisul
          Tamanho da Conta - 9 Dígitos + 1 DV (sendo os dois primeiros o tipo de conta)
        """
        account = self.config('account')

        if len(account) < 10:
            raise InvalidAccountNumber(10)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        calculate_account = CalculateNumberAccount(account).calculate_number_account_banrisul()

        if not calculate_account:
            raise InvalidDigitAccountNumber()

        return True
