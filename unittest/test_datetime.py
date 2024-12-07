import unittest
import datetime

class DateTimeTest(unittest.TestCase):
    def test_create_2024_christmas_date(self):
        # Fixture Setup

        # Exercise SUT
        christmas_date = datetime.date(2024, 12, 25)

        # Result Verification
        self.assertEqual(2024, christmas_date.year)
        self.assertEqual(12, christmas_date.month)
        self.assertEqual(25, christmas_date.day)

        # Fixture Teardown

    def test_throws_error_when_creating_date_with_negative_year(self):
        # Fixture Setup

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_date = datetime.date(-1, 12, 25)

        # Result Verification

        # Fixture Teardown

    def test_throws_error_when_creating_date_in_month_zero(self):
        # Fixture Setup

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_date = datetime.date(2024, 12, 0)

        # Result Verification

        # Fixture Teardown

    def test_throws_error_when_creating_date_with_more_than_12_months(self):
        # Fixture Setup

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_date = datetime.date(2024, 13, 25)

        # Result Verification

        # Fixture Teardown

    def test_throws_error_when_creating_date_with_29_days_in_february_of_non_leap_year(self):
        # Fixture Setup

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_date = datetime.date(2023, 2, 29)

        # Result Verification

        # Fixture Teardown

    def test_create_date_day_29_in_februrary_of_leap_year(self):
        # Fixture Setup

        # Exercise SUT
        feb_leap_year_29 = datetime.date(2024, 2, 29)

        # Result Verification
        self.assertEqual(2024, feb_leap_year_29.year)
        self.assertEqual(2, feb_leap_year_29.month)
        self.assertEqual(29, feb_leap_year_29.day)

        # Fixture Teardown

    def test_weekday_returns_0_when_day_is_monday(self):
        # Fixture Setup
        monday_date = datetime.date(2024, 9, 2)

        # Exercise SUT
        monday_date_weekday = monday_date.weekday()

        # Result Verification
        self.assertEqual(0, monday_date_weekday)

        # Fixture Teardown

    def test_weekday_returns_1_when_day_is_tuesday(self):
        # Fixture Setup
        tuesday_date = datetime.date(2024, 9, 3)

        # Exercise SUT
        tuesday_date_weekday = tuesday_date.weekday()

        # Result Verification
        self.assertEqual(1, tuesday_date_weekday)

        # Fixture Teardown

    def test_weekday_returns_2_when_day_is_wednesday(self):
        # Fixture Setup
        wednesday_date = datetime.date(2024, 9, 4)

        # Exercise SUT
        wednesday_date_weekday = wednesday_date.weekday()

        # Result Verification
        self.assertEqual(2, wednesday_date_weekday)

        # Fixture Teardown

    def test_weekday_returns_3_when_day_is_thursday(self):
        # Fixture Setup
        thursday_date = datetime.date(2024, 9, 5)

        # Exercise SUT
        thursday_date_weekday = thursday_date.weekday()

        # Result Verification
        self.assertEqual(3, thursday_date_weekday)

        # Fixture Teardown

    def test_weekday_returns_4_when_day_is_friday(self):
        # Fixture Setup
        friday_date = datetime.date(2024, 9, 6)

        # Exercise SUT
        friday_date_weekday = friday_date.weekday()

        # Result Verification
        self.assertEqual(4, friday_date_weekday)

        # Fixture Teardown

    def test_weekday_returns_5_when_day_is_saturday(self):
        # Fixture Setup
        saturday_date = datetime.date(2024, 9, 7)

        # Exercise SUT
        saturday_date_weekday = saturday_date.weekday()

        # Result Verification
        self.assertEqual(5, saturday_date_weekday)

        # Fixture Teardown

    def test_weekday_returns_6_when_day_is_sunday(self):
        # Fixture Setup
        sunday_date = datetime.date(2024, 9, 8)

        # Exercise SUT
        sunday_date_weekday = sunday_date.weekday()

        # Result Verification
        self.assertEqual(6, sunday_date_weekday)

        # Fixture Teardown

    def test_create_8am_time(self):
        # Fixture setup

        # Exercise SUT
        time_8am = datetime.time(8, 0, 0)

        # Result Verification
        self.assertEqual(8, time_8am.hour)
        self.assertEqual(0, time_8am.minute)
        self.assertEqual(0, time_8am.second)

        # Fixture Teardown
    
    def test_throws_error_when_creating_time_hour_25(self):
        # Fixture Setup

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_time = datetime.time(25, 0, 0)

        # Result Verification

        # Fixture Teardown

    def test_throws_error_when_creating_time_hour_negative(self):
        # Fixture Setup

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_time = datetime.time(-5, 0, 0)

        # Result Verification

        # Fixture Teardown

    def test_create_christmas_date_8am_datetime(self):
        # Fixture setup

        # Exercise SUT
        christmas_8am_datetime = datetime.datetime(2024, 12, 25, 8, 0, 0)

        # Result Verification
        self.assertEqual(2024, christmas_8am_datetime.year)
        self.assertEqual(12, christmas_8am_datetime.month)
        self.assertEqual(25, christmas_8am_datetime.day)
        self.assertEqual(8, christmas_8am_datetime.hour)
        self.assertEqual(0, christmas_8am_datetime.minute)
        self.assertEqual(0, christmas_8am_datetime.second)

        # Fixture Teardown

    def test_difference_between_2_dates_returns_1_day_when_difference_between_them_is_1_day(self):
        # Fixture setup
        first_date = datetime.date(2024, 12, 25)
        second_date = datetime.date(2024, 12, 26)

        # Exercise SUT
        difference = second_date - first_date

        # Result Verification
        self.assertEqual(1, difference.days)

        # Fixture Teardown

    def test_difference_between_2_dates_returns_30_days_when_difference_between_them_is_30_days(self):
        # Fixture setup
        first_date = datetime.date(2024, 11, 25)
        second_date = datetime.date(2024, 12, 25)

        # Exercise SUT
        difference = second_date - first_date

        # Result Verification
        self.assertEqual(30, difference.days)

        # Fixture Teardown

    def test_difference_between_2_dates_returns_365_days_when_difference_between_them_is_365_days(self):
        # Fixture setup
        first_date = datetime.date(2022, 12, 25)
        second_date = datetime.date(2023, 12, 25)

        # Exercise SUT
        difference = second_date - first_date

        # Result Verification
        self.assertEqual(365, difference.days)

        # Fixture Teardown

    def test_throws_error_when_replacing_date_with_negative_year(self):
        # Fixture setup
        christmas_date = datetime.date(2024, 12, 25)

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_time = christmas_date.replace(year = -1)

        # Result Verification

        # Fixture Teardown

    def test_throws_error_when_replacing_date_with_negative_month(self):
        # Fixture setup
        christmas_date = datetime.date(2024, 12, 25)

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_time = christmas_date.replace(month = -1)

        # Result Verification

        # Fixture Teardown

    def test_throws_error_when_replacing_date_with_negative_day(self):
        # Fixture setup
        christmas_date = datetime.date(2024, 12, 25)

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_time = christmas_date.replace(day = -1)

        # Result Verification

        # Fixture Teardown

    def test_throws_error_when_replacing_date_with_year_zero(self):
        # Fixture setup
        christmas_date = datetime.date(2024, 12, 25)

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_time = christmas_date.replace(year = 0)

        # Result Verification

        # Fixture Teardown

    def test_throws_error_when_replacing_date_with_month_zero(self):
        # Fixture setup
        christmas_date = datetime.date(2024, 12, 25)

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_time = christmas_date.replace(month = 0)

        # Result Verification

        # Fixture Teardown

    def test_throws_error_when_replacing_date_with_day_zero(self):
        # Fixture setup
        christmas_date = datetime.date(2024, 12, 25)

        # Exercise SUT
        with self.assertRaises(ValueError):
            invalid_time = christmas_date.replace(day = 0)

        # Result Verification

        # Fixture Teardown

    def test_replaces_christmas_2024_with_christmas_2025(self):
        # Fixture setup
        christmas_date_2024 = datetime.date(2024, 12, 25)

        # Exercise SUT
        christmas_date_2025 = christmas_date_2024.replace(year = 2025)

        # Result Verification
        self.assertEqual(2025, christmas_date_2025.year)

        # Fixture Teardown

unittest.main()
