import pytest
from lib.todo import Todo

def test_task_not_string():
    with pytest.raises(TypeError) as e:
        Todo(1)
    assert str(e.value) == 'Task must be a string'

def test_task_empty():
    with pytest.raises(ValueError) as e:
        Todo('')
    assert str(e.value) == 'Task cannot be empty'

def test_task_space():
    with pytest.raises(ValueError) as e:
        Todo(' ')
    assert str(e.value) == 'Task cannot be empty'

def test_task_valid():
    t = Todo('Buy milk')
    assert t.task == 'Buy milk'

def test_marked_incomplete():
    t = Todo('Buy milk')
    assert t.complete == False

def test_marked_complete():
    t = Todo('Buy milk')
    t.mark_complete()
    assert t.complete == True

def test_format_string():
    t = Todo('Buy milk')
    assert t.format_string() == 'Buy milk : incomplete'