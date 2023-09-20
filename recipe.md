>> PURPOSE

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

>> CLASS STRUCTURES
```python
class Diary():
    def __init__():
        Purpose: Initialise some lists to store diary entries, todo list and contacts
        Input: None
        Output: None
        Effects: Creates empty lists
    
    def add_entry():
        Purpose: Add a diary entry to the diary
        Input: Diary entry
        Output: None
        Effects: Adds diary entry to entry list
    
    def add_todo():
        Purpose: Add a todo item to the todo list
        Input: Todo item
        Output: None
        Effects: Adds todo item to todo list
    
    def add_contact():
        Purpose: Add a contact to the contact list
        Input: Contact
        Output: None
        Effects: Adds contact to contact list
    
    def get_contacts():
        Purpose: Get a list of all contacts
        Input: None
        Output: List of contacts
        Effects: None
    
    def get_single_contact(name):
        Purpose: Get a single contact
        Input: name as string
        Output: Contact
        Effects: None
    
    def get_entries():
        Purpose: Get a list of all diary entries
        Input: None
        Output: List of diary entries
        Effects: None
    
    def get_incomplete_todos():
        Purpose: Get a list of all incomplete todo items
        Input: None
        Output: List of incomplete todo items
        Effects: None

    def get_complete_todos():
        Purpose: Get a list of all completed todo items
        Input: None
        Output: List of completed todo items
        Effects: None
    
    def get_best_entry_for_time():
        Purpose: Get the best diary entry to read based on time available and reading speed
        Input: wpm, minutes
        Output: Diary entry
        Effects: None
    

class DiaryEntry():
    def __init__(title, contents):
        Purpose: Initialise a diary entry
        Input: Title, contents as strings
        Output: None
        Effects: Creates a diary entry with a title and contents
    
    def count_words():
        Purpose: Count the number of words in a diary entry
        Input: None
        Output: Number of words as integer
        Effects: None
    
    def reading_time(wpm):
        Purpose: Calculate the reading time of a diary entry
        Input: wpm as integer
        Output: minutes to read as integer
        Effects: None

    def readable_format():
        Purpose: Format a diary entry to as a string
        Input: None
        Output: Formatted diary entry as string
        Effects: None
    
class Contact():
    def __init__(name, number):
        Purpose: Initialise a contact
        Input: Name, number as strings
        Output: None
        Effects: Creates a contact with a name and number, error if number not valid
    
    def readable_format():
        Purpose: Format a contact as a string
        Input: None
        Output: Formatted contact as string
        Effects: None

class Todo():
    def __init__(task):
        Purpose: Initialise a todo item
        Input: task as string
        Output: None
        Effects: Creates a todo item with a task and incomplete status
    
    def mark_complete():
        Purpose: Mark a todo item as complete
        Input: None
        Output: None
        Effects: Changes status of todo item to complete
    
    def readable_format():
        Purpose: Format a todo item as a string
        Input: None
        Output: Formatted todo item as string
        Effects: None
```

>> TESTS

Todo Tests:
    - task is a string
    - task is not empty
    - task is stored correctly
    - task is marked as incomplete by default
    - task can be marked as complete
    - task can be formatted as a string

Contact Tests:
    - name is a string
    - name is not empty
    - name is stored correctly
    - number is a string
    - number is not empty
    - number is correct length
    - number is stored correctly
    - contact can be formatted as a string

DiaryEntry Tests:
    - title is a string
    - title is not empty
    - title is stored correctly
    - contents is a string
    - contents is not empty
    - contents is stored correctly
    - number of words is calculated correctly
    - wpm is an integer
    - wpm is greater than zero
    - reading time is calculated correctly
    - reading time is rounded to the nearest minute
    - diary entry can be formatted as a string

Diary Tests:
    - diary has an empty list of entries by default
    - diary has an empty list of todos by default
    - diary has an empty list of contacts by default
    - entry inputted when adding entry is a DiaryEntry
    - entry is added to list of entries
    - todo inputted when adding todo is a Todo
    - todo is added to list of todos
    - contact inputted when adding contact is a Contact
    - contact is added to list of contacts
    - list of contacts in readable format can be returned
    - single contact in readable format can be returned
    - list of entries in readable format can be returned
    - list of incomplete todos in readable format can be returned
    - list of complete todos in readable format can be returned
    - best entry for time can be returned
    - None returned if no valid entries for time