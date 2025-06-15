"""BEGIN

    SET names TO ["Bob", "Angel", "Jimi", "Alan", "Ada"]
    SET full_names TO ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

    INITIALIZE first_initials AS empty list
    FOR EACH name IN names DO
        APPEND first character of name TO first_initials
    END FOR
    DISPLAY first_initials

    SET first_initials TO [first character of name FOR EACH name IN names]
    DISPLAY first_initials

    SET full_initials TO [first character of first word + first character of second word
                          FOR EACH name IN full_names]
    DISPLAY full_initials

    SET a_names TO [name FOR EACH name IN names IF name starts with "A"]
    DISPLAY a_names

    SORT names alphabetically
    JOIN sorted names WITH spaces INTO one string
    DISPLAY joined string

    SET lowercase_full_names TO [lowercase version of name FOR EACH name IN full_names]
    DISPLAY lowercase_full_names

    SET almost_numbers TO ['0', '10', '21', '3', '-7', '88', '9']

    SET numbers TO [integer version of num FOR EACH num IN almost_numbers]
    DISPLAY numbers

    SET numbers_greater_than_nine TO [num FOR EACH num IN numbers IF num > 9]
    DISPLAY numbers_greater_than_nine

    INITIALIZE long_last_names AS empty list
    FOR EACH name IN full_names DO
        IF length of name > 11 THEN
            SPLIT name INTO parts
            APPEND second part (last name) TO long_last_names
        END IF
    END FOR
    JOIN long_last_names WITH ", " INTO a string
    DISPLAY the string

END
"""

"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# this splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# this example uses filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# and here's the join string method being used to create a single string from the names like:
# 'Ada Alan Angel Bob Jimi'
print(" ".join(sorted(names)))

# ✅ list comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']

# ✅ list comprehension to create a list of integers from the above list of strings
numbers = [int(num) for num in almost_numbers]
print(numbers)

# ✅ list comprehension to create a list of only the numbers that are greater than 9
numbers_greater_than_nine = [num for num in numbers if num > 9]
print(numbers_greater_than_nine)

# ✅ (advanced) string of last names for full names longer than 11 characters
long_last_names_string = ", ".join(
    [name.split()[1] for name in full_names if len(name) > 11]
)
print(long_last_names_string)  # Output: Harlem, Hendrix, Lovelace
