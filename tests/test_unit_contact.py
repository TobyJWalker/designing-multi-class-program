import pytest
from lib.contact import Contact

def test_name_not_string():
    with pytest.raises(TypeError) as e:
        Contact(1, '07123456789')
    assert str(e.value) == 'Name must be a string'

def test_name_empty():
    with pytest.raises(ValueError) as e:
        Contact('', '07123456789')
    assert str(e.value) == 'Name cannot be empty'

def test_name_space():
    with pytest.raises(ValueError) as e:
        Contact(' ', '07123456789')
    assert str(e.value) == 'Name cannot be empty'

def test_name_valid():
    c = Contact('John', '07123456789')
    assert c.name == 'John'

def test_contact_not_string():
    with pytest.raises(TypeError) as e:
        Contact('John', 0)
    assert str(e.value) == 'Contact must be a string'

def test_contact_empty():
    with pytest.raises(ValueError) as e:
        Contact('John', '')
    assert str(e.value) == 'Contact cannot be empty'

def test_contact_space():
    with pytest.raises(ValueError) as e:
        Contact('John', ' ')
    assert str(e.value) == 'Contact cannot be empty'

def test_contact_too_short():
    with pytest.raises(ValueError) as e:
        Contact('John', '0712345678')
    assert str(e.value) == 'Contact must be 11 digits'

def test_contact_too_long():
    with pytest.raises(ValueError) as e:
        Contact('John', '071234567890')
    assert str(e.value) == 'Contact must be 11 digits'

def test_contact_valid():
    c = Contact('John', '07123456789')
    assert c.contact == '07123456789'

def test_format_string():
    c = Contact('John', '07123456789')
    assert c.format_string() == 'John : 07123456789'