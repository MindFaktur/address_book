import logging

from regex.regex import RegexValidations
from registry.contact_object_creator import Contacts


class USAContactObject(Contacts):
    logging.basicConfig(filename='log.log', filemode='a', format=' \n %(asctime)s - %(message)s',
                        level=logging.DEBUG)

    def __init__(self, contact_object):
        super().__init__(contact_object)
        self.country = Contacts.get_input_object(" Country ", RegexValidations.state_regex)

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
                ", Country: " + self.country + \
                " } "

    def get_country(self):
        return self.country

    def set_country(self):
        self.country = Contacts.get_input_object(" new Country ", RegexValidations.state_regex)

    def edit_values(self, choice):
        """
        Changes the existing object value to a new one
        :param contact_obj: contact object whoose fields are to be changed
        :param choice:what field is to be changed
        :return:nothing
        """
        try:
            editors = {1: self.set_first_name, 2: self.set_last_name, 3: self.set_address,
                       4: self.set_city, 5: self.set_state, 6: self.set_zip,
                       7: self.set_phone, 8: self.set_email, 9: self.set_country
                       }
            editors.get(choice)()
        except Exception:
            logging.exception(msg="Error at edit values")
