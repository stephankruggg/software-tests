import unittest
from hamcrest import assert_that, greater_than, equal_to_ignoring_case, equal_to, is_, all_of, less_than, contains_string

from src.dinheiro import Dinheiro, Moeda, ValorMonetario

class TestMoney(unittest.TestCase):
    def test_returns_negative_monetary_value_when_calling_negative(self):
        # Inline - Fixture Setup
        monetary_value = ValorMonetario(Moeda.BRL, -100)
        money = Dinheiro(Moeda.BRL, 1, 0)

        # Exercise SUT
        result = money.negativo()

        # Result Verification
        assert_that(result, is_(equal_to(monetary_value)))

        # Fixture Teardown

    def test_returns_positive_monetary_value_when_calling_positive(self):
        # Inline - Fixture Setup
        monetary_value = ValorMonetario(Moeda.BRL, 100)
        money = Dinheiro(Moeda.BRL, 1, 0)

        # Exercise SUT
        result = money.positivo()

        # Result Verification
        assert_that(result, is_(equal_to(monetary_value)))

        # Fixture Teardown

    def test_returns_1050_when_calling_quantity_in_scale_for_10_50(self):
        # Inline - Fixture Setup
        money = Dinheiro(Moeda.BRL, 10, 50)

        # Exercise SUT
        result = money.obter_quantia_em_escala()

        # Result Verification
        assert_that(result, all_of(equal_to(1050), less_than(1100), greater_than(1000)))

        # Fixture Teardown

    def test_returns_formatted_string_with_positive_signal_for_monetary_value_100(self):
        # Inline - Fixture Setup
        monetary_value = ValorMonetario(Moeda.BRL, 100)

        # Exercise SUT
        formatted_with_signal = monetary_value.formatar_com_sinal()

        # Result Verification
        assert_that(formatted_with_signal, is_(equal_to_ignoring_case('+1,00 brl')))

        # Fixture Teardown


    def test_returns_formatted_string_with_negative_signal_for_monetary_value_negative_100(self):
        # Inline - Fixture Setup
        monetary_value = ValorMonetario(Moeda.BRL, -100)

        # Exercise SUT
        formatted_with_signal = monetary_value.formatar_com_sinal()

        # Result Verification
        assert_that(formatted_with_signal, all_of(contains_string('-'), contains_string('1,00'), contains_string('BRL')))

        # Fixture Teardown
