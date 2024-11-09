import csv


class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar."""
        current_year = 2024  # Assuming the current year is 2024
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (50 years or older)."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Define less than operator for sorting by year."""
        return self.year < other.year


def read_guitars_from_csv(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            year = int(row[1])
            cost = float(row[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display all guitars in the list."""
    for guitar in guitars:
        print(guitar)


def main():
    """Main function to run the program."""
    filename = 'guitars.csv'

    # Read existing guitars from CSV
    guitars = read_guitars_from_csv(filename)

    # Display current guitars
    print("Current Guitars:")
    display_guitars(guitars)

    # Sort guitars by year
    guitars.sort()

    # Display sorted guitars
    print("\nSorted Guitars (by Year):")
    display_guitars(guitars)

    # User input for new guitars
    while True:
        name = input("\nEnter guitar name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)

    # Write updated list back to CSV
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

    print("\nUpdated list of guitars has been saved.")


if __name__ == "__main__":
    main()