import unittest
from src.dinheiro import Moeda, Dinheiro
from src.operacao import EstadosDeOperacao

from tests_helper import TestsHelper

class TestBankSystem(unittest.TestCase):
    def test_deposit_100_reais_when_calling_deposit_with_valid_coin_and_value(self):
        # Delegated, Inline - Fixture Setup
        deposit_amount = Dinheiro(Moeda.BRL, 100, 0)
        total_amount = Dinheiro(Moeda.BRL, 200, 0)
        bank_system, account = TestsHelper().create_bank_system_with_account_with_funds(Moeda.BRL, 100, 0)

        # Exercise SUT
        result = bank_system.depositar(account, deposit_amount)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SUCESSO, result.obter_estado())
        self.assertEqual(total_amount.positivo(), account.calcular_saldo())

        # Fixture Teardown

    def test_returns_invalid_coin_when_calling_deposit_with_coin_from_another_countr(self):
        # Delegated, Inline - Fixture Setup
        deposit_amount = Dinheiro(Moeda.USD, 100, 0)
        bank_system, account = TestsHelper().create_bank_system_with_account_with_funds(Moeda.BRL, 100, 0)

        # Exercise SUT
        result = bank_system.depositar(account, deposit_amount)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.MOEDA_INVALIDA, result.obter_estado())

        # Fixture Teardown

    def test_returns_insufficient_funds_when_calling_deposit_with_zero(self):
        # Delegated, Inline - Fixture Setup
        deposit_amount = Dinheiro(Moeda.BRL, 0, 0)
        bank_system, account = TestsHelper().create_bank_system_with_account_with_funds(Moeda.BRL, 100, 0)

        # Exercise SUT
        result = bank_system.depositar(account, deposit_amount)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SALDO_INSUFICIENTE, result.obter_estado())

        # Fixture Teardown

    def test_withdraw_100_when_calling_withdraw_with_valid_coin_and_sufficient_funds(self):
        # Delegated, Inline - Fixture Setup
        withdrawal_amount = Dinheiro(Moeda.BRL, 100, 0)
        zero = Dinheiro(Moeda.BRL, 0, 0)
        bank_system, account = TestsHelper().create_bank_system_with_account_with_funds(Moeda.BRL, 100, 0)

        # Exercise SUT
        result = bank_system.sacar(account, withdrawal_amount)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SUCESSO, result.obter_estado())
        self.assertEqual(zero.positivo(), account.calcular_saldo())

        # Fixture Teardown

    def test_returns_insufficient_funds_when_calling_withdraw_with_insufficient_funds(self):
        # Delegated, Inline - Fixture Setup
        withdrawal_amount = Dinheiro(Moeda.BRL, 1000, 0)
        bank_system, account = TestsHelper().create_bank_system_with_account_with_funds(Moeda.BRL, 100, 0)

        # Exercise SUT
        result = bank_system.sacar(account, withdrawal_amount)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.SALDO_INSUFICIENTE, result.obter_estado())

        # Fixture Teardown

    def test_returns_invalid_coin_when_calling_withdraw_with_coin_from_another_country(self):
        # Delegated, Inline - Fixture Setup
        withdrawal_amount = Dinheiro(Moeda.USD, 100, 0)
        bank_system, account = TestsHelper().create_bank_system_with_account_with_funds(Moeda.BRL, 100, 0)

        # Exercise SUT
        result = bank_system.sacar(account, withdrawal_amount)

        # Result Verification
        self.assertEqual(EstadosDeOperacao.MOEDA_INVALIDA, result.obter_estado())

        # Fixture Teardown
