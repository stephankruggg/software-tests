import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestDuckDuckGoCalculator(unittest.TestCase):
    def setUp(self):
        service = webdriver.ChromeService(executable_path='/usr/local/bin/chromedriver')

        self._browser = webdriver.Chrome(service=service)

        self._browser.get("http://duckduckgo.com")

        search_field = self._browser.find_element(By.CSS_SELECTOR, '#searchbox_input')
        search_field.send_keys('calculator')

        search_button = self._browser.find_element(By.CSS_SELECTOR, '.searchbox_searchButton__F5Bwq')
        search_button.click()

    def testSumSevenAndEight(self):
        seven = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(4)')
        seven.click()

        addition = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(15)')
        addition.click()

        eight = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(5)')
        eight.click()

        equal = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(18)')
        equal.click()

        time.sleep(5)
        result = self._browser.find_element(By.CSS_SELECTOR, '#display')
        self.assertEqual('15', result.text)

    def testSumSevenAndEightAndDivideByTen(self):
        seven = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(4)')
        seven.click()

        addition = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(15)')
        addition.click()

        eight = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(5)')
        eight.click()

        equal = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(18)')
        equal.click()

        divide = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(3)')
        divide.click()

        one = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(12)')
        one.click()

        zero = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(16)')
        zero.click()

        equal.click()

        time.sleep(5)

        result = self._browser.find_element(By.CSS_SELECTOR, '#display')
        self.assertEqual('1.5', result.text)

    def testSumSevenAndEightAndDecrementOneAndOneResultsInZero(self):
        seven = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(4)')
        seven.click()

        addition = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(15)')
        addition.click()

        eight = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(5)')
        eight.click()

        equal = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(18)')
        equal.click()

        clear = self._browser.find_element(By.CSS_SELECTOR, '#clear_button')
        clear.click()

        one = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(12)')
        one.click()

        decrement = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(11)')
        decrement.click()

        one.click()

        equal.click()

        time.sleep(5)

        result = self._browser.find_element(By.CSS_SELECTOR, '#display')
        self.assertEqual('0', result.text)

    def testSumSevenAndEightAndDecrementOneAndOneAndMultiplyTwoAndThreeShowsAllOperationsInHistory(self):
        seven = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(4)')
        seven.click()

        addition = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(15)')
        addition.click()

        eight = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(5)')
        eight.click()

        equal = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(18)')
        equal.click()

        clear = self._browser.find_element(By.CSS_SELECTOR, '#clear_button')
        clear.click()

        one = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(12)')
        one.click()

        decrement = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(11)')
        decrement.click()

        one.click()

        equal.click()

        clear.click()

        two = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(13)')
        two.click()

        multiply = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(7)')
        multiply.click()

        three = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(14)')
        three.click()

        equal.click()

        time.sleep(5)

        first_operation = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > ul > li:nth-child(3) > span.tile__past-formula.one-line')
        self.assertEqual('7 + 8', first_operation.text)
        first_result = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > ul > li:nth-child(3) > span.tile__past-result.one-line')
        self.assertEqual('15', first_result.text)

        middle_operation = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > ul > li:nth-child(2) > span.tile__past-formula.one-line')
        self.assertEqual('1 - 1', middle_operation.text)
        middle_result = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > ul > li:nth-child(2) > span.tile__past-result.one-line')
        self.assertEqual('0', middle_result.text)

        last_operation = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > ul > li:nth-child(1) > span.tile__past-formula.one-line')
        self.assertEqual('2 × 3', last_operation.text)
        last_result = self._browser.find_element(By.CSS_SELECTOR, '#zci-calculator > div > div > div > div > div > div.tile__tabs > ul > li:nth-child(1) > span.tile__past-result.one-line')
        self.assertEqual('6', last_result.text)
