import unittest

from src.dinheiro import Moeda

from tests.tests_helper import TestsHelper

class TestAccount(unittest.TestCase):
    def test_return_owner_when_calling_owner(self):
        # Delegated - Fixture Setup
        _, account = TestsHelper().create_bank_system_with_account_with_funds(Moeda.BRL, 100, 0)

        # Exercise SUT
        owner = account.titular

        # Result Verification
        self.assertEqual('test', owner)

        # Fixture Teardown
