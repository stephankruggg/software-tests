import unittest
from src.banco import Banco
from src.agencia import Agencia
from src.dinheiro import Moeda

class TestBank(unittest.TestCase):
    def setUp(self) -> None:
        self._bank = Banco('test', Moeda.BRL)

    def test_returns_agency_when_creating_agency(self):
        # Implicit, Inline - Fixture Setup
        expected_agency = Agencia('test', 1, self._bank)

        # Exercise SUT
        actual_agency = self._bank.criar_agencia('test')

        # Result Verification
        self.assertEqual(expected_agency.obter_identificador(), actual_agency.obter_identificador())

        # Fixture Teardown

    def test_returns_agency_agency_by_name(self):
        # Implicit, Inline - Fixture Setup
        expected_agency = self._bank.criar_agencia('test')

        # Exercise SUT
        actual_agency = self._bank.obter_agencia('test')

        # Result Verification
        self.assertEqual(expected_agency, actual_agency)

        # Fixture Teardown

    def test_returns_none_when_agency_by_name_does_not_exist(self):
        # Implicit - Fixture Setup

        # Exercise SUT
        agency = self._bank.obter_agencia('test')

        # Result Verification
        self.assertIsNone(agency)

        # Fixture Teardown