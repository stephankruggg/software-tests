import unittest
from src.banco import Banco
from src.conta import Conta
from src.dinheiro import Moeda

class TestAgency(unittest.TestCase):
    def setUp(self) -> None:
        self._bank = Banco('test', Moeda.BRL)
        self._agency = self._bank.criar_agencia('test')

    def test_returns_account_when_creating_account(self):
        # Implicit, Inline - Fixture Setup
        expected_account = Conta('test', 1, self._agency)

        # Exercise SUT
        actual_account = self._agency.criar_conta('test')

        # Result Verification
        self.assertEqual(expected_account.obter_identificador(), actual_account.obter_identificador())

        # Fixture Teardown

    def test_returns_account_by_name(self):
        # Implicit, Inline - Fixture Setup
        expected_account = self._agency.criar_conta('test')
        identifier = expected_account.obter_identificador()

        # Exercise SUT
        actual_account = self._agency.obter_conta(identifier)

        # Result Verification
        self.assertEqual(expected_account, actual_account)

        # Fixture Teardown

    def test_returns_none_when_no_account_with_identifier_exist(self):
        # Implicit - Fixture Setup

        # Exercise SUT
        account = self._agency.obter_conta('0001-4')

        # Result Verification
        self.assertIsNone(account)

        # Fixture Teardown
