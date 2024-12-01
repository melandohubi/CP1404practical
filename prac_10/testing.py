import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    False  # Corrected expected output
    """
    return len(word) >= length


def format_sentence(phrase):
    """Format the phrase as a proper sentence.

    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('python')
    'Python.'  # Additional test case
    """
    return phrase.capitalize() + '.'


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"  # This should now pass

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car(fuel=10)
    assert car._fuel == 10, "Car does not set fuel correctly when passed in."
    car_default = Car()  # Test default fuel
    assert car_default._fuel == 0, "Car does not set default fuel correctly."


run_tests()

# Uncomment this line to run the doctests
doctest.testmod()