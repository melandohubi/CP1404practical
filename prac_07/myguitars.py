"""CLASS Guitar
    FUNCTION __init__(name = "", year = 0, cost = 0)
        SET self.name = name
        SET self.year = year
        SET self.cost = cost
    END FUNCTION

    FUNCTION __str__()
        RETURN self.name + " (" + str(self.year) + ") : $" + format(self.cost, 2 decimal places)
    END FUNCTION

    FUNCTION get_age()
        SET current_year = system's current year
        RETURN current_year - self.year
    END FUNCTION

    FUNCTION is_vintage()
        IF self.get_age() >= 50 THEN
            RETURN True
        ELSE
            RETURN False
        END IF
    END FUNCTION

    FUNCTION __lt__(other)
        RETURN self.year < other.year
    END FUNCTION
END CLASS


FUNCTION load_guitars(filename)
    CREATE empty list guitars
    OPEN file with name = filename FOR reading
    FOR EACH line IN file
        SPLIT line BY "," INTO name, year, cost
        CONVERT year TO integer
        CONVERT cost TO float
        CREATE Guitar object with name, year, cost
        ADD Guitar object TO guitars
    END FOR
    RETURN guitars
END FUNCTION


FUNCTION display_guitars(guitars)
    PRINT "These are my guitars:"
    FOR index FROM 0 TO length of guitars - 1
        SET guitar = guitars[index]
        IF guitar.is_vintage() == True THEN
            SET vintage_label = "(vintage)"
        ELSE
            SET vintage_label = ""
        END IF
        PRINT "Guitar " + (index + 1) + ": " + str(guitar) + " " + vintage_label
    END FOR
END FUNCTION


FUNCTION add_guitars()
    CREATE empty list new_guitars
    PRINT "Enter your new guitars. Leave name blank to finish."
    WHILE True
        PROMPT user FOR name
        IF name == "" THEN
            BREAK
        END IF
        PROMPT user FOR year AS integer
        PROMPT user FOR cost AS float
        CREATE Guitar object with name, year, cost
        ADD Guitar object TO new_guitars
    END WHILE
    RETURN new_guitars
END FUNCTION


FUNCTION save_guitars(filename, guitars)
    OPEN file with name = filename FOR writing
    FOR EACH guitar IN guitars
        WRITE guitar.name + "," + str(guitar.year) + "," + str(guitar.cost) TO file
    END FOR
END FUNCTION


FUNCTION main()
    SET FILENAME = "guitars.csv"
    SET guitars = load_guitars(FILENAME)

    CALL display_guitars(guitars)

    SET new_guitars = add_guitars()
    ADD all guitars from new_guitars TO guitars

    SORT guitars using __lt__ method (by year)

    PRINT "Sorted guitars:"
    CALL display_guitars(guitars)

    CALL save_guitars(FILENAME, guitars)

    PRINT length of guitars + " guitars saved to " + FILENAME
END FUNCTION


CALL main()
"""


from datetime import date

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return date.today().year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year


def load_guitars(filename):
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_string}")


def add_guitars():
    new_guitars = []
    print("Enter your new guitars. Leave name blank to finish.")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitars.append(Guitar(name, year, cost))
    return new_guitars


def save_guitars(filename, guitars):
    with open(filename, "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def main():
    FILENAME = "guitars.csv"
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    new_guitars = add_guitars()
    guitars.extend(new_guitars)

    guitars.sort()
    print("\nSorted guitars:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\n{len(guitars)} guitars saved to {FILENAME}.")


if __name__ == '__main__':
    main()
