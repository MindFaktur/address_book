import logging


class AddressBooks:

    logging.basicConfig(filename='log.txt', filemode='a', format=' \n %(asctime)s - %(message)s', level=logging.DEBUG)
    system_registry = {}

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

    @staticmethod
    def add_to_list(book_name, contact_object_to_add):
        """
        Add's the given new contact object to the list
        :param book_name: Address book name to whose list the new contact object is to be added
        :param contact_object_to_add: new contact
        :return: boolean
        """
        try:
            contact_list = AddressBooks.system_registry.get(book_name)
            for contact_obj in contact_list:
                print(contact_obj)
                if contact_obj.first_name == contact_object_to_add.first_name\
                        and contact_obj.last_name == contact_object_to_add.last_name:
                    print("This contact details already exists with same name")
                    return
            contact_list.append(contact_object_to_add)
            return

        except Exception:
            logging.exception("Error occurred while adding contact object to list")

    def get_contact_list_using_book_name(self, book_name):
        """
        Returns the whole list of contacts for the given book name
        :param book_name: Address book key book name
        :return: list of contacts
        """
        try:
            if book_name in self.system_registry.keys():
                return self.system_registry.get(book_name)
            else:
                print("Doesn't Exist")
                return

        except Exception:
            print("Exception occurred")
            logging.exception(f"Error occurred while getting contact list using book name: {book_name}")

    @staticmethod
    def edit_contact(book_name, first_name, last_name):
        """
        Get's the object whoose data field is to be changed
        :param book_name: Address book name
        :param first_name: contact object first name
        :param last_name: contact object last name
        :return: contact object to edit
        """
        try:
            if book_name in AddressBooks.system_registry.keys():
                contact_list = AddressBooks.system_registry.get(book_name)
                for item in contact_list:
                    if item.first_name == first_name and item.last_name == last_name:
                        return item

                print("Given names Doesn't Exist")
                return False

            else:
                print("The given address book name doesn't exist")
                return False

        except Exception:
            logging.exception(f"Error occurred while getting contact list using book name, given names are"
                              f" book_name: {book_name}, first_name: {first_name}, last_name: {last_name}")

    def add_to_system(self, book_name, contact_object):
        """
        Add's new book name and the contact
        :param book_name: new boook name
        :param contact_object: new contact to add
        :return: nothing
        """
        try:
            list_of_contacts = []
            list_of_contacts.append(contact_object)
            if book_name not in self.system_registry.keys():
                self.system_registry[book_name] = list_of_contacts
                return
            else:
                print("The given address book name already exists")
                return

        except Exception:
            logging.exception("Error occurred while adding contact list to system registry")

    @staticmethod
    def print_system_registry():
        """
        Prints the system registry
        :return: nothing
        """
        try:
            for i in range(0, len(AddressBooks.system_registry.items())):
                for key in AddressBooks.system_registry.keys():
                    print(key)
                    for obj in AddressBooks.system_registry.get(key):
                        print(obj)

        except Exception:
            logging.exception("error while printing")

