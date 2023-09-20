from lib.diary_entry import DiaryEntry
from lib.contact import Contact
from lib.todo import Todo

class Diary():
    def __init__(self):
        self.entries = []
        self.contacts = []
        self.todos = []
    
    def add_entry(self, entry):
        if type(entry) != DiaryEntry:
            raise TypeError('Entry must be of type DiaryEntry')
        self.entries.append(entry)
    
    def add_contact(self, contact):
        if type(contact) != Contact:
            raise TypeError('Contact must be of type Contact')
        self.contacts.append(contact)
    
    def add_todo(self, todo):
        if type(todo) != Todo:
            raise TypeError('Todo must be of type Todo')
        self.todos.append(todo)
    
    def get_contacts(self):
        return [contact.format_string() for contact in self.contacts]
    
    def get_single_contact(self, name):
        if type(name) != str:
            raise TypeError('Name must be a string')
        elif name.strip() == '':
            raise ValueError('Name cannot be empty')
        for contact in self.contacts:
            if contact.name == name:
                return contact.format_string()
    
    def get_entries(self):
        return [entry.format_string() for entry in self.entries]

    def get_incomplete_todos(self):
        return [todo.format_string() for todo in self.todos if not todo.complete]
    
    def get_complete_todos(self):
        return [todo.format_string() for todo in self.todos if todo.complete]
    
    def get_best_entry_for_time(self, wpm, minutes):
        if type(wpm) != int:
            raise TypeError('wpm must be an integer')
        elif wpm <= 0:
            raise ValueError('wpm must be greater than zero')
        elif type(minutes) != int:
            raise TypeError('Minutes must be an integer')
        elif minutes <= 0:
            raise ValueError('Minutes must be greater than zero')
        best_entry = None

        valid_entries = [entry for entry in self.entries if entry.reading_time(wpm) <= minutes]

        for entry in valid_entries:
            if best_entry == None:
                best_entry = entry
            elif entry.reading_time(wpm) > best_entry.reading_time(wpm):
                best_entry = entry
        
        return best_entry.format_string() if best_entry != None else None
        