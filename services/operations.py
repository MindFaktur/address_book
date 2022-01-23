import logging
from registry.address_book import AddressBooks


class Operations:

    logging.basicConfig(filename='address_book_log.log', filemode='a', format=' \n %(asctime)s - %(message)s', level=logging.DEBUG)

    @staticmethod
    def get_input(field_name):
        """
        Get's user input and returns it
        :param field_name: The user data field
        :return: data field
        """
        try:
            return input(f" Please enter {field_name}")

        except Exception:
            logging.exception("Error while taking input in get_input")

    @staticmethod
    def get_user_choice():
        """
        Print's the main menu
        :return: Choice that user want's to do
        """
        try:
            option = int(input("Press \n 1) Add new Address Book \n 2) Edit Existing book "
                               "\n 3) Add contact to existing address book \n 4) Print All \n 5) Quit "
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
            while new_option != 5:
                if new_option == 1:
                    book_name = input("Please enter the new address book name \n ")
                    new_object = Operations.contact_details()
                    contact_object = AddressBooks(new_object)

                    contact_object.add_to_system(book_name, contact_object)

                    contact_object.print_system_registry()
                    new_option = Operations.get_user_choice()

                elif new_option == 2:
                    Operations.edit_menu()
                    new_option = Operations.get_user_choice()

                elif new_option == 3:
                    book_name = input("Please enter the existing address book name to add contact \n ")
                    new_object = Operations.contact_details()
                    contact_object = AddressBooks(new_object)
                    AddressBooks.add_to_list(book_name, contact_object)
                    new_option = Operations.get_user_choice()

                elif new_option == 4:
                    AddressBooks.print_system_registry()
                    new_option = Operations.get_user_choice()

        except Exception:
            logging.exception("Error at contact_details")

    @staticmethod
    def contact_details():
        """
        Gives a dictionary object of user input for all contact details
        :return: dictionary object
        """
        try:
            detail_object = {"first_name": Operations.get_input(" First Name "),
                             "last_name": Operations.get_input(" Last Name "),
                             "address": Operations.get_input(" Address "),
                             "city": Operations.get_input(" City "),
                             "state": Operations.get_input(" State "),
                             "zip": Operations.get_input(" Zip code "),
                             "phone_number": Operations.get_input(" Phone Number "),
                             "email": Operations.get_input(" Email -ID ")
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
            book_name = input("Please enter the new address book name ")
            contact_first_name = input("Please enter the first name of contact to edit")
            contact_last_name = input("Please enter the last name of contact to edit")
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
            new_value = input("Please enter the new value: ")
            contact_obj = AddressBooks.edit_contact(book_name, contact_first_name, contact_last_name)

            if contact_obj:
                Operations.editor(contact_obj, edit_field, new_value)

        except TypeError:
            print("Please enter values of data type as mentioned above")
        except Exception:
            logging.exception(f"Error while taking input in edit_menu ")

    @staticmethod
    def editor(contact_object, choice, new_val):
        """
        All editing of contact details
        :param contact_object: The person's contact data object
        :param choice: The data field user wants to edit
        :param new_val: The new value of the field
        :return: nothing
        """
        try:
            if choice == 1:
                contact_object.first_name = new_val
            elif choice == 2:
                contact_object.last_name = new_val
            elif choice == 3:
                contact_object.address = new_val
            elif choice == 4:
                contact_object.city = new_val
            elif choice == 5:
                contact_object.state = new_val
            elif choice == 6:
                contact_object.zip = new_val
            elif choice == 7:
                contact_object.phone_number = new_val
            elif choice == 8:
                contact_object.email = new_val
            else:
                print("Please choose from above")

        except Exception:
            logging.exception("editor error")


