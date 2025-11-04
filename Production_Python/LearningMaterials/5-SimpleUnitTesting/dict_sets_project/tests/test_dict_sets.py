"""testing file for dict_sets.py"""
from src.dict_sets import cleanup_address_book, search_address_book, count_vowels
from src.dict_sets import get_names_in_common, get_numbers_in_common, combine_address_books

def test_cleanup_address_book():
    """unit tests for cleanup_address_book function"""
    #arrange
    input_address_book = {
        "john doe": 1234567890,
        "JANE SMITH": "0987654321",
        "alice": "5551234",
        "BOB": "5556789"
    }
    expected_output = {
        "John Doe": "123 4567890",
        "Jane Smith": "098 7654321",
        "Alice": "5551234",
        "Bob": "5556789"
    }
    #act
    actual_output = cleanup_address_book(input_address_book)
    #assert
    assert actual_output == expected_output

def test_search_address_book():
    """unit tests for search_address_book function"""
    #arrange
    input_address_book = {
        "John Doe": "123 4567890",
        "Jane Smith": "098 7654321",
        "Alice": "5551234",
        "Bob": "5556789"
    }
    search_string = "Ja"
    expected_output = {
        "Jane Smith": "098 7654321"
    }
    #act
    actual_output = search_address_book(input_address_book, search_string)
    #assert
    assert actual_output == expected_output

def test_count_vowels():
    """unit tests for count_vowels function"""
    #arrange
    input_string = "Hello World! This is a Test String."
    expected_output = {"a": 1, "e": 2, "i": 3, "o": 2, "u": 0}
    #act
    actual_output = count_vowels(input_string)
    #assert
    assert actual_output == expected_output

def test_get_names_in_common():
    """unit tests for get_names_in_common function"""
    #arrange
    address_book1 = {
        "John Doe": "123 4567890",
        "Jane Smith": "098 7654321",
        "Alice": "5551234"
    }
    address_book2 = {
        "Jane Smith": "098 7654321",
        "Bob": "5556789",
        "Charlie": "4445555"
    }
    expected_output = {"Jane Smith"}
    #act
    actual_output = get_names_in_common(address_book1, address_book2)
    #assert
    assert actual_output == expected_output

def test_get_numbers_in_common():
    """unit tests for get_numbers_in_common function"""
    #arrange
    address_book1 = {
        "John Doe": "123 4567890",
        "Jane Smith": "098 7654321",
        "Alice": "5551234"
    }
    address_book2 = {
        "Bob": "5556789",
        "Charlie": "098 7654321",
        "David": "4445555"
    }
    expected_output = {"098 7654321"}
    #act
    actual_output = get_numbers_in_common(address_book1, address_book2)
    #assert
    assert actual_output == expected_output

def test_combine_address_books():
    """unit tests for combine_address_books function"""
    #arrange
    address_book1 = {
        "John Doe": "123 4567890",
        "Jane Smith": "098 7654321",
        "Alice": "5551234"
    }
    address_book2 = {
        "Jane Smith": "098 7654321",
        "Bob": "5556789",
        "Charlie": "4445555"
    }
    expected_output = (
        {
            "John Doe": "123 4567890",
            "Jane Smith": "098 7654321",
            "Alice": "5551234",
            "Bob": "5556789",
            "Charlie": "4445555"
        },
        {
            "Jane Smith": "098 7654321"
        }
    )
    #act
    actual_output = combine_address_books(address_book1, address_book2)
    #assert
    assert actual_output == expected_output