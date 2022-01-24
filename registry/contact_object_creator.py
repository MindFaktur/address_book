import logging

from regex.regex import RegexValidations


class Contacts:
    logging.basicConfig(filename='log.log', filemode='a', format=' \n %(asctime)s - %(message)s',
                        level=logging.DEBUG)

    def __init__(self, contact_object):
        self.first_name = contact_object["first_name"]
        self.last_name = contact_object["last_name"]
        self.address = contact_object["address"]
        self.city = contact_object["city"]
        self.state = contact_object["state"]
        self.zip = contact_object["zip"]
        self.phone_number = contact_object["phone_number"]
        self.email = contact_object["email"]

    def __str__(self):
        return " " + self.first_name + " " + self.last_name + \
                " { " + \
                " First Name: " + self.first_name + \
                ", Last Name: " + self.last_name + \
                ", Address: " + self.address + \
                ", City: " + self.city + \
                ", State: " + self.state + \
                ", Zip: " + self.zip + \
                ", Phone Number: " + self.phone_number + \
                ", Email: " + self.email + \
                " } "

    def get_first_name(self):
        return self.first_name

    def set_first_name(self):
        self.first_name = Contacts.get_input_object(" first name ", RegexValidations.name_regex)

    def get_last_name(self):
        return self.last_name

    def set_last_name(self):
        self.last_name = Contacts.get_input_object(" last name ", RegexValidations.name_regex)

    def get_address(self):
        return self.address

    def set_address(self):
        self.address = Contacts.get_input_object(" new address ", RegexValidations.address_regex)

    def get_city(self):
        return self.city

    def set_city(self):
        self.city = Contacts.get_input_object(" new city ", RegexValidations.city_regex)

    def get_state(self):
        return self.state

    def set_state(self):
        self.state = Contacts.get_input_object(" new state ", RegexValidations.state_regex)

    def get_zip(self):
        return self.zip

    def set_zip(self):
        self.zip = Contacts.get_input_object(" new zip code ", RegexValidations.zip_regex)

    def get_phone(self):
        return self.phone_number

    def set_phone(self):
        self.phone_number = Contacts.get_input_object(" new phone number ", RegexValidations.phone_regex)

    def get_email(self):
        return self.email

    def set_email(self):
        self.email = Contacts.get_input_object(" new email -Id ", RegexValidations.email_regex)

    @staticmethod
    def get_input_object(field_name, regex):
        """
        Get's the user input and validates the input according to the given regex
        :param field_name: The value to be entered
        :param regex: regex pattern
        :return: field value
        """
        try:
            field_value = input(f" Please enter {field_name}")
            if RegexValidations.regex_validator(field_value, regex):
                return field_value
            else:
                logging.debug(msg=f" Invalid value entered at {field_name} = {field_value}")
                print("Entered name is InValid, please enter again")
                return Contacts.get_input_object(field_name, regex)
        except Exception:
            print("Enter proper value")
            logging.exception("Error while taking input in get_input")
