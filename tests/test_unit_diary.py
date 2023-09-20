import pytest
from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.contact import Contact
from lib.todo import Todo

def test_entry_list_empty():
    d = Diary()
    assert d.entries == []

def test_contact_list_empty():
    d = Diary()
    assert d.contacts == []

def test_todo_list_empty():
    d = Diary()
    assert d.todos == []

def test_add_entry_not_DiaryEntry():
    d = Diary()
    with pytest.raises(TypeError) as e:
        d.add_entry(1)
    assert str(e.value) == 'Entry must be of type DiaryEntry'

def test_add_DiaryEntry():
    d = Diary()
    de = DiaryEntry('My first diary entry', 'This is a diary entry')
    d.add_entry(de)
    assert d.entries == [de]

def test_add_contact_not_Contact():
    d = Diary()
    with pytest.raises(TypeError) as e:
        d.add_contact(1)
    assert str(e.value) == 'Contact must be of type Contact'

def test_add_Contact():
    d = Diary()
    c = Contact('John', '07123456789')
    d.add_contact(c)
    assert d.contacts == [c]

def test_add_todo_not_Todo():
    d = Diary()
    with pytest.raises(TypeError) as e:
        d.add_todo(1)
    assert str(e.value) == 'Todo must be of type Todo'

def test_add_Todo():
    d = Diary()
    t = Todo('Buy milk')
    d.add_todo(t)
    assert d.todos == [t]