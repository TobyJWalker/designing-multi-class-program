import pytest
from lib.diary_entry import DiaryEntry

def test_title_not_string():
    with pytest.raises(TypeError) as e:
        DiaryEntry(1, 'This is a diary entry')
    assert str(e.value) == 'Title must be a string'

def test_title_empty():
    with pytest.raises(ValueError) as e:
        DiaryEntry('', 'This is a diary entry')
    assert str(e.value) == 'Title cannot be empty'

def test_title_space():
    with pytest.raises(ValueError) as e:
        DiaryEntry(' ', 'This is a diary entry')
    assert str(e.value) == 'Title cannot be empty'

def test_title_valid():
    d = DiaryEntry('My first diary entry', 'This is a diary entry')
    assert d.title == 'My first diary entry'

def test_contents_not_string():
    with pytest.raises(TypeError) as e:
        DiaryEntry('My first diary entry', 1)
    assert str(e.value) == 'Contents must be a string'

def test_contents_empty():
    with pytest.raises(ValueError) as e:
        DiaryEntry('My first diary entry', '')
    assert str(e.value) == 'Contents cannot be empty'

def test_contents_space():
    with pytest.raises(ValueError) as e:
        DiaryEntry('My first diary entry', ' ')
    assert str(e.value) == 'Contents cannot be empty'

def test_contents_valid():
    d = DiaryEntry('My first diary entry', 'This is a diary entry')
    assert d.contents == 'This is a diary entry'

def test_count_words():
    d = DiaryEntry('My first diary entry', 'This is a diary entry')
    assert d.count_words() == 5

def test_wpm_not_int():
    d = DiaryEntry('My first diary entry', 'This is a diary entry')
    with pytest.raises(TypeError) as e:
        d.reading_time('1')
    assert str(e.value) == 'Words per minute must be an integer'

def test_wpm_less_than_zero():
    d = DiaryEntry('My first diary entry', 'This is a diary entry')
    with pytest.raises(ValueError) as e:
        d.reading_time(-1)
    assert str(e.value) == 'Words per minute must be greater than zero'

def test_reading_time():
    d = DiaryEntry('My first diary entry', 'This is a diary entry')
    assert d.reading_time(5) == 1

def test_format_string():
    d = DiaryEntry('My first diary entry', 'This is a diary entry')
    assert d.format_string() == 'My first diary entry : This is a diary entry'