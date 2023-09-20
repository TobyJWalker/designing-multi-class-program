class Contact():
    def __init__(self, name, contact):
        if type(name) != str:
            raise TypeError('Name must be a string')
        elif name.strip() == '':
            raise ValueError('Name cannot be empty')
        elif type(contact) != str:
            raise TypeError('Contact must be a string')
        elif contact.strip() == '':
            raise ValueError('Contact cannot be empty')
        elif len(contact) != 11:
            raise ValueError('Contact must be 11 digits')
        self.name = name
        self.contact = contact
    
    def format_string(self):
        return f'{self.name} : {self.contact}'