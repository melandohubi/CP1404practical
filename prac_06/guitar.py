"""CLASS Guitar
    FUNCTION __init__(name = "", year = 0, cost = 0)
        SET self.name = name
        SET self.year = year
        SET self.cost = cost
    END FUNCTION

    FUNCTION __str__()
        RETURN string formatted as: self.name + " (" + self.year + ") : $" + self.cost with 2 decimal places
    END FUNCTION

    FUNCTION get_age()
        SET current_year = system's current year
        RETURN current_year - self.year
    END FUNCTION

    FUNCTION is_vintage()
        IF get_age() >= 50 THEN
            RETURN True
        ELSE
            RETURN False
        END IF
    END FUNCTION
END CLASS

# Main Program
CREATE guitar OBJECT with name = "Gibson L-5 CES", year = 1922, cost = 16035.40
PRINT guitar (calls __str__())
PRINT "Age: " + guitar.get_age() + " years"
PRINT "Vintage: " + guitar.is_vintage()
"""


from datetime import date

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

# Example usage:
guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar)
print(f"Age: {guitar.get_age()} years")
print(f"Vintage: {guitar.is_vintage()}")

