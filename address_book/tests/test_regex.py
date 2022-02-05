import unittest
import pytest
from regex.regex import RegexValidations


class TestRegexValidations(unittest.TestCase):

    def test_regex_given_name(self):
        """
        Test's all first names or last names from the below list
        :return: nothing
        """
        name_list = [('Vish', True), ('Vi', False), ('Vis', False), ('VIS', False),
                     ('vish', False), ('Vish87', False), ('87Vish', False), ('Vish@', False)]
        for i, j in name_list:
            with self.subTest(msg=f" Test {i} is {j}"):
                self.assertEqual(RegexValidations.regex_validator(i, RegexValidations.name_regex), j)

    def test_regex_given_address(self):
        """
        Test's all addresses from the below list
        :return: nothing
        """
        address_list = [('house name, street name', True), ('house no 1, street', True), ('!vishwa', True),
                        ('VIS', True),
                        ('vish', True), ('Vish87', True), ('87Vish', True), ('Vish@', True)]
        for i, j in address_list:
            with self.subTest(msg=f" Test {i} is {j}"):
                self.assertEqual(RegexValidations.regex_validator(i, RegexValidations.address_regex), j)

    def test_regex_given_city(self):
        """
        Test's all city names from the below list
        :return: nothing
        """
        city_list = [('Dharwad', True), ('dhar 96', False), ('hubli @!', False), ('HUBLI', False),
                     (' Karwar', False), ('New York', True), ('New York City', True)]
        for i, j in city_list:
            with self.subTest(msg=f" Test {i} is {j}"):
                self.assertEqual(RegexValidations.regex_validator(i, RegexValidations.city_regex), j)

    def test_regex_given_state(self):
        """
        Test's all state names from the below list
        :return: nothing
        """
        state_list = [('Karnataka', True), ('karnataka @!', False), ('HUBLI', False),
                     (' Karwar', False), ('Madhya Pradesh', True), ('New York City', True)]
        for i, j in state_list:
            with self.subTest(msg=f" Test {i} is {j}"):
                self.assertEqual(RegexValidations.regex_validator(i, RegexValidations.state_regex), j)

    def test_regex_given_zip(self):
        """
        Test's all zip codes from the below list
        :return: nothing
        """
        zip_list = [('580001', True), ('58', False), ('Vis', False), ('58001', False),
                     ('!58001', False), ('', False), ('87Vish', False), ('58 0001', False)]
        for i, j in zip_list:
            with self.subTest(msg=f" Test {i} is {j}"):
                self.assertEqual(RegexValidations.regex_validator(i, RegexValidations.zip_regex), j)

    def test_regex_given_phone_number(self):
        """
        Test's all phone numbers from the below list
        :return: nothing
        """
        number_list = [('91 9874563218', True), ('58', False), ('Vis', False), ('919874563218', False),
                     ('9874563218', False), ('9874563218 91', False), (' ', False), ('! @87955', False)]
        for i, j in number_list:
            with self.subTest(msg=f" Test {i} is {j}"):
                self.assertEqual(RegexValidations.regex_validator(i, RegexValidations.phone_regex), j)

    def test_regex_given_email(self):
        """
        Test's all email ids from the below list
        :return: nothing
        """
        email_list = [('email@gmail.com', True), ('@email@gmail.com', False), ('Email @gmail.com', False),
                      ('email.gmail.com', False),
                     (' email@gmail.com', False), ('email@gmail com', False), (' ', False), ('! @87955', False)]
        for i, j in email_list:
            with self.subTest(msg=f" Test {i} is {j}"):
                self.assertEqual(RegexValidations.regex_validator(i, RegexValidations.email_regex), j)
