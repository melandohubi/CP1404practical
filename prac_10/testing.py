"""PROGRAM main
    CALL run_tests
    CALL doctest.testmod IF this module is the main program
END PROGRAM

FUNCTION repeat_string(s, n)
    # Return string s repeated n times, separated by spaces
    RETURN s joined with a space, repeated n times
END FUNCTION

FUNCTION is_long_word(word, length DEFAULT 5)
    # Return True if length of word is greater than or equal to the given length
    IF LENGTH(word) >= length THEN
        RETURN True
    ELSE
        RETURN False
    END IF
END FUNCTION

FUNCTION phrase_as_sentence(phrase)
    REMOVE leading and trailing whitespace from phrase

    IF phrase == empty string THEN
        RETURN "."
    END IF

    SET first_letter TO uppercase of first character in phrase
    SET remainder TO all characters in phrase except the first
    SET sentence TO first_letter concatenated with remainder

    IF sentence DOES NOT end with "." THEN
        ADD "." to end of sentence
    END IF

    RETURN sentence
END FUNCTION

FUNCTION run_tests
    # Test repeat_string
    ASSERT repeat_string("Python", 1) == "Python"
    ASSERT repeat_string("hi", 2) == "hi hi"
    ASSERT repeat_string("wow", 0) == ""
    ASSERT repeat_string("", 3) == "  "  # Two spaces, empty strings repeated
    ASSERT repeat_string("x", 5) == "x x x x x"

    # Test is_long_word
    ASSERT is_long_word("short") == True         # Because length == 5
    ASSERT is_long_word("tiny", 6) == False
    ASSERT is_long_word("Python", 6) == True
    ASSERT is_long_word("abcdefg", 7) == True
    ASSERT is_long_word("") == False

    # Test Car initialization
    CREATE car_default AS new Car()
    ASSERT car_default._odometer == 0
    ASSERT car_default.fuel == 0

    CREATE car_fuel AS new Car(fuel = 10)
    ASSERT car_fuel.fuel == 10
    ASSERT car_fuel._odometer == 0

    # Test phrase_as_sentence
    ASSERT phrase_as_sentence("hello") == "Hello."
    ASSERT phrase_as_sentence("It is an ex parrot.") == "It is an ex parrot."
    ASSERT phrase_as_sentence("  yEs  ") == "Yes."
    ASSERT phrase_as_sentence("") == "."
    ASSERT phrase_as_sentence("hello world!") == "Hello world!."
END FUNCTION
"""

"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.

    >>> repeat_string("hi", 2)
    'hi hi'
    >>> repeat_string("hello", 3)
    'hello hello hello'
    >>> repeat_string("Python", 1)
    'Python'
    """
    # Use join to repeat with spaces as required
    return ' '.join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    >>> is_long_word("long", 4)
    True
    """
    # Use >= so that exactly equal length returns True
    return len(word) >= length

def phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence:
    - Capitalize the first character,
    - Ensure there is a single trailing full stop (period).
    - Remove any leading/trailing whitespace.

    >>> phrase_as_sentence('hello')
    'Hello.'
    >>> phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_as_sentence('  yEs  ')
    'Yes.'
    >>> phrase_as_sentence('')
    '.'
    >>> phrase_as_sentence('hello world!')
    'Hello world!.'
    """
    phrase = phrase.strip()
    if not phrase:
        return '.'
    # Capitalise the first letter, leave the rest as is
    sentence = phrase[0].upper() + phrase[1:]
    # Add a full stop if not already ending with a period.
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence

def run_tests():
    """Run the tests on functions and Car class using assertions."""
    # Test repeat_string
    assert repeat_string("Python", 1) == "Python", "repeat_string(1) failed"
    assert repeat_string("hi", 2) == "hi hi", "repeat_string(2) failed"
    assert repeat_string("wow", 0) == "", "repeat_string(0) failed"
    assert repeat_string("", 3) == "  ", "repeat_string with empty string failed"
    assert repeat_string("x", 5) == "x x x x x", "repeat_string(5) failed"

    # Test is_long_word
    assert is_long_word("short")  # Default length is 5, 'short' is 5
    assert not is_long_word("tiny", 6)
    assert is_long_word("Python", 6)
    assert is_long_word("abcdefg", 7)
    assert not is_long_word("")   # Empty string is not long

    # Test Car __init__
    car_default = Car()
    assert car_default._odometer == 0, "Car default odometer not zero"
    assert car_default.fuel == 0, "Car default fuel not zero"

    car_fuel = Car(fuel=10)
    assert car_fuel.fuel == 10, "Car fuel not set correctly when value passed in"
    assert car_fuel._odometer == 0, "Car odometer not zero when passing fuel"

    # Test phrase_as_sentence
    assert phrase_as_sentence('hello') == 'Hello.'
    assert phrase_as_sentence('It is an ex parrot.') == 'It is an ex parrot.'
    assert phrase_as_sentence('  yEs  ') == 'Yes.'
    assert phrase_as_sentence('') == '.'
    assert phrase_as_sentence('hello world!') == 'Hello world!.'

# Actually run the test functions
run_tests()

if __name__ == "__main__":
    # Run all doctests in this file.
    doctest.testmod()
