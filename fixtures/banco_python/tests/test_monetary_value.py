import unittest
from src.dinheiro import ValorMonetario, Moeda, Dinheiro

class TestMonetaryValue(unittest.TestCase):
    def test_returns_true_when_monetary_value_is_zero(self):
        # Inline - Fixture Setup
        zero_monetary_value = ValorMonetario(Moeda.BRL, 0)

        # Exercise SUT
        result = zero_monetary_value.zero()

        # Result Verification
        self.assertEqual(True, result)

        # Fixture Teardown

    def test_returns_false_when_monetary_value_is_not_zero(self):
        # Inline - Fixture Setup
        not_zero_monetary_value = ValorMonetario(Moeda.BRL, 100)

        # Exercise SUT
        result = not_zero_monetary_value.zero()

        # Result Verification
        self.assertEqual(False, result)

        # Fixture Teardown

    def test_raises_incompatible_coins_exception_when_coins_are_incompatible(self):
        # Inline - Fixture Setup
        monetary_value_brl = ValorMonetario(Moeda.BRL, 100)
        monetary_value_usd = Dinheiro(Moeda.USD, 100, 0)

        # Exercise SUT
        with self.assertRaises(Exception):
            result = monetary_value_brl.validar_moeda(monetary_value_usd)

        # Result Verification

        # Fixture Teardown
