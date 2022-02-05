import re


class RegexValidations:

    name_regex = "^[A-Z]{1}[a-z]{3,12}$"
    address_regex = r"[A-Za-z0-9\s.]*"
    city_regex = r"^[A-Z]{1}[a-z]|[A-Z]{1}[a-z]* [A-Z]{1}[a-z]*"
    state_regex = r"^[A-Z]{1}[a-z]|[A-Z]{1}[a-z]* [A-Z]{1}[a-z]*"
    zip_regex = "^[0-9]{6}$"
    phone_regex = "^[0-9]{2} [6-9]{1}[0-9]{9}$"
    email_regex = "^[a-zA-Z0-9][a-zA-Z0-9+_.-]+@[a-zA-Z0-9][a-zA-Z0-9]+[+_.-][a-zA-Z0-9]+$"

    @staticmethod
    def regex_validator(value_to_validate, regex_pattern):
        """
        Takes string and the regex pattern to validate with
        :param value_to_validate: given user input
        :param regex_pattern: given regex pattern
        :return: True or False
        """

        val = re.search(regex_pattern, value_to_validate)
        if val:
            return True
        else:
            return False
