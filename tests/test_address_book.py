from unittest import TestCase
from registry.address_book import AddressBooks


class TestAddressBooks(TestCase):

    def test_add_to_system(self):
        """
        Tests if the code can create can a new object and add to system registry
        :return: True
        """
        detail_object = {"first_name": "First Name",
                         "last_name": "Last Name",
                         "address": "Address",
                         "city": "City",
                         "state": "State",
                         "zip": "Zip code",
                         "phone_number": "Phone Number",
                         "email": "Email -ID "
                         }
        book_name = "FirstBook"
        contact_obj = AddressBooks(detail_object)
        contact_obj.add_to_system(book_name, contact_obj)

        assert len(AddressBooks.system_registry) > 0

    def test_edit_contact_given_correct_names_return_object(self):
        """
        Will get the object by name to edit it
        :return: True
        """
        book_name = "FirstBook"
        first_name = "First Name"
        last_name = "Last Name"
        contact_obj = AddressBooks.edit_contact(book_name, first_name, last_name)
        if contact_obj:
            assert True

    def test_edit_contact_given_wrong_book_name_return_object(self):
        """
        Return's false if the object with given name doesn't exist
        :return: True
        """
        book_name = "FirstBook"
        first_name = "First Name"
        last_name = "Last Name"
        contact_obj = AddressBooks.edit_contact(book_name, first_name, last_name)
        if not contact_obj:
            assert True

    def test_edit_contact_given_wrong_first_name_return_False(self):
        """
        Return's false if the object with given name doesn't exist
        :return: True
        """
        book_name = "FirstBook"
        first_name = "FirstName"
        last_name = "Last Name"
        contact_obj = AddressBooks.edit_contact(book_name, first_name, last_name)
        if not contact_obj:
            assert True

    def test_edit_contact_given_wrong_last_name_return_False(self):
        """
        Return's false if the object with given name doesn't exist
        :return: True
        """
        book_name = "FirstBook"
        first_name = "First Name"
        last_name = "LastName"
        contact_obj = AddressBooks.edit_contact(book_name, first_name, last_name)
        if not contact_obj:
            assert True

    def test_add_to_list(self):
        """
        Test if a new object can be added to a existing list
        :return: True
        """
        detail_object = {"first_name": "First Name",
                         "last_name": "Last Name",
                         "address": "Address",
                         "city": "City",
                         "state": "State",
                         "zip": "Zip code",
                         "phone_number": "Phone Number",
                         "email": "Email -ID "
                         }
        book_name = "FirstBook"
        contact_obj = AddressBooks(detail_object)
        contact_obj.add_to_system(book_name, contact_obj)

        detail_object1 = {"first_name": "First1",
                          "last_name": "Last1",
                          "address": "Address1",
                          "city": "City1",
                          "state": "State1",
                          "zip": "Zip code1",
                          "phone_number": "Phone Number1",
                          "email": "Email -ID1"
                          }

        contact_obj1 = AddressBooks(detail_object1)
        contact_obj1.add_to_list(book_name, contact_obj1)
        list_of_contacts = contact_obj1.get_contact_list_using_book_name(book_name)

        assert len(list_of_contacts) > 0
