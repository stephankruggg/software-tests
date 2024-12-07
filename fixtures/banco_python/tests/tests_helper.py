from src.sistema_bancario import SistemaBancario
from src.dinheiro import Dinheiro

class TestsHelper:
    def create_bank_system_with_account_with_funds(self, coin, int_value, frac_value):
        bank_system = SistemaBancario()
        bank = bank_system.criar_banco('test', coin)
        agency = bank.criar_agencia('test')
        account = agency.criar_conta('test')

        money = Dinheiro(coin, int_value, frac_value)
        bank_system.depositar(account, money)

        return bank_system, account
