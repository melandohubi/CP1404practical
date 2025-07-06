"""
Estimate: 15 minutes
Start time: 2025-07-06 18:30
Actual time taken: ___ minutes (fill this in after testing)
"""

"""CLASS ProgrammingLanguage

    FUNCTION __init__(name, typing, reflection, year)
        SET self.name = name
        SET self.typing = typing
        SET self.reflection = reflection
        SET self.year = year
    END FUNCTION

    FUNCTION is_dynamic()
        IF self.typing == "Dynamic" THEN
            RETURN True
        ELSE
            RETURN False
        END IF
    END FUNCTION

    FUNCTION __str__()
        RETURN formatted string:
            self.name + ", " + self.typing + " Typing, Reflection=" + self.reflection
            + ", First appeared in " + self.year
    END FUNCTION

END CLASS
"""

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
