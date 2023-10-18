
class ContactList:

    def __init__(self, name, contacts):
        self.name = name
        self.contacts = contacts    
   
    def create_contact(self):
        input_name = input("Enter a name")
        input_number = input("Enter a phone number")
        return {'name': input_name, 'number': input_number}

    def add_contact(self, d):
        self.contacts.append(d)
        self.contacts = sorted(self.contacts, key=lambda x: x['name'])

    @property
    def get_name(self):
        return self.name
    
    @get_name.setter
    def set_name(self, new_name):
        self.name = new_name

    @property
    def get_contacts(self):
        return self.contacts
    
    @get_contacts.setter
    def set_contacts(self, new_contacts):
        self.contacts = new_contacts

    def remove_contact(self, value):
        new_contacts = []
        for contact in self.contacts:
            if contact['name'] != value:
                new_contacts.append(contact)
        self.contacts = new_contacts

    def find_shared_contacts(self, other_contact_list):
        shared_contacts = []
        for contact in self.contacts:
            if contact in other_contact_list.get_contacts:
                shared_contacts.append(contact)
        return shared_contacts
    