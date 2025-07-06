"""IMPORT ProgrammingLanguage FROM programming_language

CREATE python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
CREATE ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
CREATE visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

PRINT python  # uses __str__ method

SET languages TO [python, ruby, visual_basic]

PRINT "The dynamically typed languages are:"

FOR EACH language IN languages
    IF language.is_dynamic() == True THEN
        PRINT language.name
    END IF
END FOR
"""

from programming_language import ProgrammingLanguage

# Create ProgrammingLanguage objects
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print one language to check __str__ output
print(python)

# Create a list of these languages
languages = [python, ruby, visual_basic]

# Print dynamically typed languages using is_dynamic method
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
