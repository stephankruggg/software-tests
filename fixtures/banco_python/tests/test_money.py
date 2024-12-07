import unittest
from src.dinheiro import Dinheiro, Moeda, ValorMonetario

class TestMoney(unittest.TestCase):
    def test_returns_true_when_money_is_zero(self):
        # Inline - Fixture Setup
        zero_money = Dinheiro(Moeda.BRL, 0, 0)

        # Exercise SUT
        result = zero_money.zero()

        # Result Verification
        self.assertEqual(True, result)

        # Fixture Teardown

    def test_returns_false_when_money_is_not_zero(self):
        # Inline - Fixture Setup
        not_zero_money = Dinheiro(Moeda.BRL, 1, 0)

        # Exercise SUT
        result = not_zero_money.zero()

        # Result Verification
        self.assertEqual(False, result)

        # Fixture Teardown

    def test_returns_negative_monetary_value_when_calling_negative(self):
        # Inline - Fixture Setup
        monetary_value = ValorMonetario(Moeda.BRL, -100)
        money = Dinheiro(Moeda.BRL, 1, 0)

        # Exercise SUT
        result = money.negativo()

        # Result Verification
        self.assertEqual(monetary_value, result)

        # Fixture Teardown

    def test_returns_positive_monetary_value_when_calling_positive(self):
        # Inline - Fixture Setup
        monetary_value = ValorMonetario(Moeda.BRL, 100)
        money = Dinheiro(Moeda.BRL, 1, 0)

        # Exercise SUT
        result = money.positivo()

        # Result Verification
        self.assertEqual(monetary_value, result)

        # Fixture Teardown

    def test_returns_1050_when_calling_quantity_in_scale_for_10_50(self):
        # Inline - Fixture Setup
        money = Dinheiro(Moeda.BRL, 10, 50)

        # Exercise SUT
        result = money.obter_quantia_em_escala()

        # Result Verification
        self.assertEqual(1050, result)

        # Fixture Teardown
