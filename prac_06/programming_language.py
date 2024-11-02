class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed."""
        return self.typing.lower() == "dynamic"


# Example usage
def main():
    # Creating instances of ProgrammingLanguage
    languages = [
        ProgrammingLanguage("Java", "Static", "Yes", 1995),
        ProgrammingLanguage("C++", "Static", "No", 1983),
        ProgrammingLanguage("Python", "Dynamic", "Yes", 1991),
        ProgrammingLanguage("Visual Basic", "Static", "No", 1991),
        ProgrammingLanguage("Ruby", "Dynamic", "Yes", 1995),
    ]

    # Displaying information about each language
    for language in languages:
        dynamic_status = "dynamically typed" if language.is_dynamic() else "statically typed"
        print(f"{language.name} is {dynamic_status} and was created in {language.year}.")


if __name__ == "__main__":
    main()