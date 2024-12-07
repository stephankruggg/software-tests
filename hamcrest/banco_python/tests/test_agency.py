from hamcrest import assert_that, same_instance, none, is_, empty, contains_inanyorder, only_contains, less_than
import unittest

from src.banco import Banco
from src.dinheiro import Moeda

class TestAgency(unittest.TestCase):
    def setUp(self) -> None:
        self._bank = Banco('test', Moeda.BRL)
        self._agency = self._bank.criar_agencia('test')

    def test_returns_account_by_name(self):
        # Implicit, Inline - Fixture Setup
        expected_account = self._agency.criar_conta('test')
        identifier = expected_account.obter_identificador()

        # Exercise SUT
        actual_account = self._agency.obter_conta(identifier)

        # Result Verification
        assert_that(expected_account, is_(same_instance(actual_account)))

        # Fixture Teardown

    def test_returns_none_when_no_account_with_identifier_exist(self):
        # Implicit - Fixture Setup

        # Exercise SUT
        account = self._agency.obter_conta('0001-4')

        # Result Verification
        assert_that(account, is_(none()))

        # Fixture Teardown

    def test_returns_empty_accounts_when_no_account_in_agency(self):
        # Implicit - Fixture Setup

        # Exercise SUT
        accounts = self._agency.obter_contas()

        # Result Verification
        assert_that(accounts, is_(empty()))

        # Fixture Teardown

    def test_returns_2_accounts_when_2_accounts_in_agency(self):
        # Implicit, Inline - Fixture Setup
        account_one = self._agency.criar_conta('test 1')
        account_two = self._agency.criar_conta('test 2')

        # Exercise SUT
        accounts = self._agency.obter_contas()

        # Result Verification
        assert_that(accounts, contains_inanyorder(account_one, account_two))

        # Fixture Teardown

    def test_adding_account_increases_number_of_accounts_in_agency(self):
        # Implicit, Inline - Fixture Setup
        self._agency.criar_conta('test 1')
        number_of_accounts_before_addition = len(self._agency.obter_contas())
        self._agency.criar_conta('test 2')

        # Exercise SUT
        number_of_accounts_after_addition = len(self._agency.obter_contas())

        # Result Verification
        assert_that(number_of_accounts_before_addition, is_(less_than(number_of_accounts_after_addition)))

        # Fixture Teardown
