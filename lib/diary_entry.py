class DiaryEntry():
    def __init__(self, title, contents):
        if type(title) != str:
            raise TypeError('Title must be a string')
        elif title.strip() == '':
            raise ValueError('Title cannot be empty')
        elif type(contents) != str:
            raise TypeError('Contents must be a string')
        elif contents.strip() == '':
            raise ValueError('Contents cannot be empty')
        self.title = title
        self.contents = contents
    
    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        if type(wpm) != int:
            raise TypeError('Words per minute must be an integer')
        elif wpm <= 0:
            raise ValueError('Words per minute must be greater than zero')
        return self.count_words() / wpm

    def format_string(self):
        return f'{self.title} : {self.contents}'