import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def generate_word(word_format, uppercase=False):
    """Generate a random word based on the specified format."""
    word = ""
    for kind in word_format:
        if kind == "c":
            letter = random.choice(CONSONANTS)
        elif kind == "v":
            letter = random.choice(VOWELS)
        else:
            continue
        if uppercase:
            letter = letter.upper()
        word += letter
    return word


word_format = input("Enter word format (c for consonant, v for vowel): ")

valid_characters = set('cv')
if not all(char in valid_characters for char in word_format):
    print("Invalid format! Use 'c' for consonant and 'v' for vowel.")
else:
    uppercase_choice = input("Do you want uppercase letters? (y/n): ").lower() == 'y'

    generated_word = generate_word(word_format, uppercase_choice)
    print(f"Generated word: {generated_word}")