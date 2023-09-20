import pytest
from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.contact import Contact
from lib.todo import Todo

def test_contact_list():
    d = Diary()
    c = Contact('John', '07123456789')
    d.add_contact(c)
    assert d.get_contacts() == ['John : 07123456789']

def test_contact_list_multiple():
    d = Diary()
    c1 = Contact('John', '07123456789')
    c2 = Contact('Jane', '07987654321')
    d.add_contact(c1)
    d.add_contact(c2)
    assert d.get_contacts() == ['John : 07123456789', 'Jane : 07987654321']

def test_get_single_contact():
    d = Diary()
    c1 = Contact('John', '07123456789')
    c2 = Contact('Jane', '07987654321')
    d.add_contact(c1)
    d.add_contact(c2)
    assert d.get_single_contact('John') == 'John : 07123456789'

def test_entry_list():
    d = Diary()
    de = DiaryEntry('My first diary entry', 'This is a diary entry')
    d.add_entry(de)
    assert d.get_entries() == ['My first diary entry : This is a diary entry']

def test_entry_list_multiple():
    d = Diary()
    de1 = DiaryEntry('My first diary entry', 'This is a diary entry')
    de2 = DiaryEntry('My second diary entry', 'This is another diary entry')
    d.add_entry(de1)
    d.add_entry(de2)
    assert d.get_entries() == ['My first diary entry : This is a diary entry', 'My second diary entry : This is another diary entry']

def test_incomplete_todo_list():
    d = Diary()
    t = Todo('Buy milk')
    d.add_todo(t)
    assert d.get_incomplete_todos() == ['Buy milk : incomplete']

def test_incomplete_todo_list_multiple():
    d = Diary()
    t1 = Todo('Buy milk')
    t1.mark_complete()
    t2 = Todo('Buy eggs')
    d.add_todo(t1)
    d.add_todo(t2)
    assert d.get_incomplete_todos() == ['Buy eggs : incomplete']

def test_complete_todo_list():
    d = Diary()
    t = Todo('Buy milk')
    t.mark_complete()
    d.add_todo(t)
    assert d.get_complete_todos() == ['Buy milk : complete']

def test_complete_todo_list_multiple():
    d = Diary()
    t1 = Todo('Buy milk')
    t1.mark_complete()
    t2 = Todo('Buy eggs')
    t2.mark_complete()
    d.add_todo(t1)
    d.add_todo(t2)
    assert d.get_complete_todos() == ['Buy milk : complete', 'Buy eggs : complete']

def test_get_best_entry_for_time():
    d = Diary()
    de1 = DiaryEntry('My first diary entry', 'This is a diary entry')
    de2 = DiaryEntry('My second diary entry', 'This is yet another diary entry')
    d.add_entry(de1)
    d.add_entry(de2)
    assert d.get_best_entry_for_time(6, 1) == 'My second diary entry : This is yet another diary entry'

def test_get_best_entry_non_valid():
    d = Diary()
    de1 = DiaryEntry('My first diary entry', 'This is a diary entry')
    de2 = DiaryEntry('My second diary entry', 'This is yet another diary entry')
    d.add_entry(de1)
    d.add_entry(de2)
    assert d.get_best_entry_for_time(3, 1) == None