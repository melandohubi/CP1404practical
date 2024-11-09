import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def load_languages_from_csv(filename):
    """Load programming languages from a CSV file and return as a list of ProgrammingLanguage objects."""
    languages = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # Skip header
        reader = csv.reader(in_file)
        for row in reader:
            reflection = row[2] == "Yes"  # Convert reflection string to boolean
            language = ProgrammingLanguage(row[0], row[1], reflection, int(row[3]))
            languages.append(language)
    return languages

def display_languages(languages):
    """Display all programming languages."""
    for language in languages:
        print(language)

def main():
    """Main function to run the program."""
    filename = 'languages.csv'
    languages = load_languages_from_csv(filename)
    display_languages(languages)

if __name__ == "__main__":
    main()