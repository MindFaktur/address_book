import logging
from registry.address_book import AddressBooks
from regex.regex import RegexValidations
from registry.contact_object_creator import Contacts
from registry.usa_contact_object import USAContactObject
from services.adapter import ListToDict


class Operations:
    logging.basicConfig(filename='log.log', filemode='a', format=' \n %(asctime)s - %(message)s',
                        level=logging.DEBUG)

    @staticmethod
    def get_input(field_name, regex):
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
                return Operations.get_input(field_name, regex)
        except Exception:
            print("Enter proper value")
            logging.exception("Error while taking input in get_input")

    @staticmethod
    def get_user_choice():
        """
        Print's the main menu
        :return: Choice that user want's to do
        """
        try:
            option = int(input("Press \n 1) Add new Address Book \n 2) Edit Existing book "
                               "\n 3) Add contact to existing address book \n 4) Print All \n 5) Search "
                               "\n 6) Delete Contact \n 7) Quit "
                               "\n choice =  "))
            return option

        except Exception:
            print("Please enter proper option")
            logging.exception("error")
            return Operations.get_user_choice()

    def menu(self):
        """
        Performs action based on the user choice from main menu
        :return:
        """

        new_option = self.get_user_choice()
        try:
            while new_option != 7:
                if new_option == 1:
                    book_name = input("Please enter the new address book name \n ")
                    if book_name not in AddressBooks.system_registry.keys():
                        new_object = self.contact_details()
                        contact_object = ListToDict(new_object).usa_contact_object()
                        contact_object.var_printer()
                        AddressBooks().add_to_system(book_name, contact_object)
                        new_option = self.get_user_choice()
                    else:
                        print(f"{book_name} already exists please choose edit option to edit it")

                elif new_option == 2:
                    self.edit_menu()
                    new_option = self.get_user_choice()

                elif new_option == 3:
                    book_name = input("Please enter the existing address book name to add contact \n ")
                    if book_name in AddressBooks.system_registry.keys():
                        new_object = self.contact_details()
                        contact_object = ListToDict(new_object).usa_contact_object()
                        AddressBooks().add_to_list(book_name, contact_object)
                        new_option = self.get_user_choice()
                    else:
                        print(f"{book_name} doesnt exist please create new book with the name")

                elif new_option == 4:
                    AddressBooks().print_system_registry()
                    new_option = self.get_user_choice()

                elif new_option == 5:
                    self.search_menu()
                    new_option = self.get_user_choice()

                elif new_option == 6:
                    self.delete_contact()
                    new_option = Operations.get_user_choice()

        except Exception:
            logging.exception(f"Error at menu operations, choice is {new_option}")

    def contact_details(self):
        """
        Gives a list of user input for all contact details
        :return: dictionary object
        """
        try:
            detail_object = [self.get_input(" First Name ", RegexValidations.name_regex),
                             self.get_input(" Last Name ", RegexValidations.name_regex),
                             self.get_input(" Address ", RegexValidations.address_regex),
                             self.get_input(" City ", RegexValidations.city_regex),
                             self.get_input(" State ", RegexValidations.state_regex),
                             self.get_input(" Zip code ", RegexValidations.zip_regex),
                             self.get_input(" Phone Number ", RegexValidations.phone_regex),
                             self.get_input(" Email -ID ", RegexValidations.email_regex)
                             ]
            return detail_object

        except Exception:
            logging.exception("Error at contact_details")

    def edit_menu(self):
        """
        Inner menu of which contact data the user want's to edit
        :return: nothing
        """
        try:
            book_name = input("Please enter the address book name ")
            if book_name in AddressBooks.system_registry.keys():
                contact_first_name = self.get_input(" First Name ", RegexValidations.name_regex)
                contact_last_name = self.get_input(" Last Name ", RegexValidations.name_regex)
                contact_obj = AddressBooks().edit_contact(book_name, contact_first_name, contact_last_name)
                i = 1
                print("--- Press ---")
                for var in contact_obj.var_printer():
                    print(f"{i}) {var}")
                    i = i + 1
                edit_choice = int(input("choice is: "))

                if contact_obj:
                    contact_obj.edit_values(edit_choice)
            else:
                print(f"{book_name} doesnt exist please create new book with the name")

        except TypeError:
            print("Please enter values of data type as mentioned above")
        except Exception:
            logging.exception(f"Error while taking input in edit_menu ")

    def search_menu(self):
        """
        Shows the menu of search items
        :return:
        """
        ad = AddressBooks()
        contact = ad.return_single_contact()
        i = 1
        print("\n --- Press ---")
        try:
            for var in contact.var_printer():
                print(f"{i}) {var}")
                i = i + 1
            search_choice = int(input("choice is: "))
            self.search_dict(contact, search_choice)
        except Exception:
            print("Enter correct option")
            logging.debug(msg=f"Error at search menu")
            return self.search_menu()

    def search_function(self, value_to_input, regex, choice):
        """
        searches paramter across all object's properties and print's names of object's having same value
        :param value_to_input:
        :param regex:
        :param choice:
        :return:
        """
        try:
            list_of_contacts = AddressBooks.system_registry.values()
            found_list = []
            new_val = self.get_input(value_to_input, regex)
            print(f"Same {value_to_input} : {new_val}")
            for contact_list in list_of_contacts:
                for contact in contact_list:
                    value = contact.list_of_get_functions(choice + 1)
                    if value == new_val:
                        found_list.append(f"{contact.get_first_name()} {contact.get_last_name()}")
            print(found_list)
        except Exception:
            logging.exception(msg="Error at search function")

    def search_dict(self, cont_obj, choice):

        choice = choice - 1
        list_of_fields = cont_obj.list_of_search_options(choice)
        try:
            self.search_function(list_of_fields[0], list_of_fields[1], choice)
        except Exception:
            print("Please enter from above options")
            logging.exception(msg="error at search dict")

    def delete_contact(self):
        book_name = input("Please enter the new address book name \n ")
        contact_first_name = self.get_input(" First Name ", RegexValidations.name_regex)
        contact_last_name = self.get_input(" Last Name ", RegexValidations.name_regex)
        AddressBooks().delete_contact(book_name, contact_first_name, contact_last_name)
