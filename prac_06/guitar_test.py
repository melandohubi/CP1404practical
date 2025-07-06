"""FUNCTION run_tests()
    SET current_year = system current year

    CREATE guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    CREATE guitar2 = Guitar("Another Guitar", 2013, 1000.00)

    SET expected_age1 = current_year - 1922
    SET expected_age2 = current_year - 2013

    PRINT guitar1.name + " get_age() - Expected " + expected_age1 + ". Got " + guitar1.get_age()
    PRINT guitar2.name + " get_age() - Expected " + expected_age2 + ". Got " + guitar2.get_age()

    PRINT guitar1.name + " is_vintage() - Expected " + (expected_age1 >= 50) + ". Got " + guitar1.is_vintage()
    PRINT guitar2.name + " is_vintage() - Expected " + (expected_age2 >= 50) + ". Got " + guitar2.is_vintage()
END FUNCTION
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

# Testing code

def run_tests():
    current_year = date.today().year

    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1000.00)

    expected_age1 = current_year - 1922
    expected_age2 = current_year - 2013

    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {guitar2.get_age()}")

    print(f"{guitar1.name} is_vintage() - Expected {expected_age1 >= 50}. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected {expected_age2 >= 50}. Got {guitar2.is_vintage()}")

run_tests()
