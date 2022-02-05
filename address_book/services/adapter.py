from registry.contact_object_creator import Contacts
from registry.usa_contact_object import USAContactObject


class ListToDict:

    def __init__(self, list_of_addressbook_values):
        self.company_details = {"first_name": list_of_addressbook_values[0],
                                "last_name": list_of_addressbook_values[1],
                                "address": list_of_addressbook_values[2],
                                "city": list_of_addressbook_values[3],
                                "state": list_of_addressbook_values[4],
                                "zip": list_of_addressbook_values[5],
                                "phone_number": list_of_addressbook_values[6],
                                "email": list_of_addressbook_values[7]
                                }

    def return_contact_object(self):
        return Contacts(self.company_details)

    def usa_contact_object(self):
        return USAContactObject(self.company_details)

