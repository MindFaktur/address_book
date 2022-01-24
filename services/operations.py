import logging
from registry.address_book import AddressBooks
from regex.regex import RegexValidations
from registry.contact_object_creator import Contacts


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
                               "\n 3) Add contact to existing address book \n 4) Print All \n 5) Search \n 6) Quit "
                               "\n choice =  "))
            return option

        except Exception:
            print("Please enter proper option")
            logging.exception("error")
            return Operations.get_user_choice()

    @staticmethod
    def menu():
        """
        Performs action based on the user choice from main menu
        :return:
        """

        new_option = Operations.get_user_choice()
        try:
            while new_option != 6:
                if new_option == 1:
                    book_name = input("Please enter the new address book name \n ")
                    if book_name not in AddressBooks.system_registry.keys():
                        new_object = Operations.contact_details()
                        contact_object = Contacts(new_object)
                        AddressBooks().add_to_system(book_name, contact_object)
                        new_option = Operations.get_user_choice()
                    else:
                        print(f"{book_name} already exists please choose edit option to edit it")

                elif new_option == 2:
                    Operations.edit_menu()
                    new_option = Operations.get_user_choice()

                elif new_option == 3:
                    book_name = input("Please enter the existing address book name to add contact \n ")
                    if book_name in AddressBooks.system_registry.keys():
                        new_object = Operations.contact_details()
                        contact_object = Contacts(new_object)
                        AddressBooks.add_to_list(book_name, contact_object)
                        new_option = Operations.get_user_choice()
                    else:
                        print(f"{book_name} doesnt exist please create new book with the name")

                elif new_option == 4:
                    AddressBooks.print_system_registry()
                    new_option = Operations.get_user_choice()

                elif new_option == 5:
                    choice = Operations.search_menu()
                    Operations().search_dict(choice)
                    new_option = Operations.get_user_choice()

        except Exception:
            logging.exception(f"Error at menu operations, choice is {new_option}")

    @staticmethod
    def contact_details():
        """
        Gives a dictionary object of user input for all contact details
        :return: dictionary object
        """
        try:
            detail_object = {"first_name": Operations.get_input(" First Name ", RegexValidations.name_regex),
                             "last_name": Operations.get_input(" Last Name ", RegexValidations.name_regex),
                             "address": Operations.get_input(" Address ", RegexValidations.address_regex),
                             "city": Operations.get_input(" City ", RegexValidations.city_regex),
                             "state": Operations.get_input(" State ", RegexValidations.state_regex),
                             "zip": Operations.get_input(" Zip code ", RegexValidations.zip_regex),
                             "phone_number": Operations.get_input(" Phone Number ", RegexValidations.phone_regex),
                             "email": Operations.get_input(" Email -ID ", RegexValidations.email_regex)
                             }
            return detail_object

        except Exception:
            logging.exception("Error at contact_details")

    @staticmethod
    def edit_menu():
        """
        Inner menu of which contact data the user want's to edit
        :return: nothing
        """
        try:
            book_name = input("Please enter the address book name ")
            if book_name in AddressBooks.system_registry.keys():
                contact_first_name = Operations.get_input(" First Name ", RegexValidations.name_regex)
                contact_last_name = Operations.get_input(" Last Name ", RegexValidations.name_regex)
                edit_field = int(input(" Press "
                                       "\n 1) Edit First Name" +
                                       "\n 2) Edit Last Name" +
                                       "\n 3) Edit Address" +
                                       "\n 4) Edit City" +
                                       "\n 5) Edit State" +
                                       "\n 6) Edit Zip code" +
                                       "\n 7) Edit Phone_number" +
                                       "\n 8) Edit Email" +
                                       "\n "
                                       ))
                contact_obj = AddressBooks.edit_contact(book_name, contact_first_name, contact_last_name)

                if contact_obj:
                    Operations.edit_values(contact_obj, edit_field)
            else:
                print(f"{book_name} doesnt exist please create new book with the name")

        except TypeError:
            print("Please enter values of data type as mentioned above")
        except Exception:
            logging.exception(f"Error while taking input in edit_menu ")

    @staticmethod
    def edit_values(contact_obj, choice):
        """
        Changes the existing object value to a new one
        :param contact_obj: contact object whoose fields are to be changed
        :param choice:what field is to be changed
        :return:nothing
        """
        try:
            editors = {1: contact_obj.set_first_name, 2: contact_obj.set_last_name, 3: contact_obj.set_address,
                       4: contact_obj.set_city, 5: contact_obj.set_state, 6: contact_obj.set_zip, 7: contact_obj.set_phone,
                       8: contact_obj.set_email}
            editors.get(choice)()
        except Exception:
            logging.exception(msg="Error at edit values")

    @staticmethod
    def search_menu():
        """
        Shows the menu of search items
        :return:
        """
        try:
            search_option = int(input("Press \n 1) Search by first name  \n 2) Search by last name "
                                      "\n 3) Search by city name \n 4) Search by state name \n 5) Search by zip code"
                                      " \n 6) Search by phone number \n 7) Search by email \n choice =  "))
            return search_option
        except Exception:
            print("Enter correct option")
            logging.debug(msg=f"Error at search menu")
            return Operations.search_menu()

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
                    editors = {1: contact.get_first_name, 2: contact.get_last_name,
                               3: contact.get_city, 4: contact.get_state, 5: contact.get_zip,
                               6: contact.get_phone, 7: contact.get_email}
                    editors.get(choice + 1)()
                    if editors.get(choice + 1)() == new_val:
                        found_list.append(f"{contact.get_first_name()} {contact.get_last_name()}")
            print(found_list)
        except Exception:
            logging.exception(msg="Error at search function")

    def search_dict(self, choice):
        """
        list of paramters
        :param choice:
        :return:
        """
        choice = choice - 1
        list_of_fields = [[" first name ", RegexValidations.name_regex], [" last name ", RegexValidations.name_regex],
                          [" city ", RegexValidations.city_regex], [" state ", RegexValidations.state_regex],
                          [" zip code ", RegexValidations.zip_regex], [" phone number ", RegexValidations.phone_regex],
                          [" email ", RegexValidations.email_regex]
                          ]
        try:
            self.search_function(list_of_fields[choice][0], list_of_fields[choice][1], choice)
        except Exception:
            print("Please enter from above options")
            logging.exception(msg="error at search dict")



