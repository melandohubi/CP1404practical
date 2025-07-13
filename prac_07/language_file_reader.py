"""# Pseudocode for Language File Reader

# Import necessary modules: csv and namedtuple
# Import ProgrammingLanguage class from programming_language module

# Define main function:
#     Call load_languages with the CSV file name and store result in 'languages'
#     Display heading "All Programming Languages"
#     For each language in 'languages':
#         Print the language using its __str__ method
#     Display heading "Dynamically typed languages:"
#     For each language in 'languages':
#         If language.typing is "dynamic" (case-insensitive):
#             Print the language's name

# Define load_languages(filename):
#     Create empty list called 'languages'
#     Open filename in read mode as in_file using 'with' context
#     Create a csv.reader for the file
#     Skip the header line using next()
#     For each row in reader:
#         Convert reflection field to boolean (True if "yes")
#         Convert year field to integer
#         Create a ProgrammingLanguage object from row values
#         Append the object to 'languages'
#     Return the list 'languages'

# Define using_csv():
#     Open CSV file using 'with' context
#     Skip header
#     For each row in csv.reader:
#         Print row as list

# Define using_namedtuple():
#     Define a namedtuple called Language with four fields
#     Open CSV file using 'with' context
#     Skip header
#     For each row in csv.reader:
#         Create Language namedtuple from row using _make()
#         Print the namedtuple using repr()

# Define using_csv_namedtuple():
#     Define a namedtuple called Language
#     Open CSV file using 'with' context
#     Skip header
#     For each row in csv.reader:
#         Create Language namedtuple from row
#         Print name and year of release
#         Print full namedtuple using repr()

# At the end of the file:
# If this script is run directly, call main()
"""

"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
Demonstrates multiple approaches: manual parsing, csv module, and namedtuple
"""

import csv
from collections import namedtuple

from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = load_languages('languages.csv')
    print("All Programming Languages:\n")
    for language in languages:
        print(language)
    print("\nDynamically typed languages:")
    for language in languages:
        if language.typing.lower() == "dynamic":
            print(language.name)


def load_languages(filename):
    """Load programming languages from a CSV file into ProgrammingLanguage objects."""
    languages = []
    with open(filename, 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        for parts in reader:
            reflection = parts[2].strip().lower() == "yes"
            year = int(parts[3])
            language = ProgrammingLanguage(parts[0], parts[1], reflection, year)
            languages.append(language)
    return languages


def using_csv():
    """Demonstration: Language file reader using the csv module."""
    with open('languages.csv', 'r', newline='') as in_file:
        next(in_file)  # Skip header
        reader = csv.reader(in_file)
        for row in reader:
            print(row)


# using_csv()


def using_namedtuple():
    """Demonstration: Language file reader using a named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year')
    with open('languages.csv', 'r', newline='') as in_file:
        next(in_file)  # Skip header
        reader = csv.reader(in_file)
        for row in reader:
            language = Language._make(row)
            print(repr(language))


# using_namedtuple()


def using_csv_namedtuple():
    """Demonstration: Language file reader using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year')
    with open("languages.csv", "r", newline='') as in_file:
        next(in_file)
        for language in map(Language._make, csv.reader(in_file)):
            print(f"{language.name} was released in {language.year}")
            print(repr(language))


# using_csv_namedtuple()

if __name__ == '__main__':
    main()
