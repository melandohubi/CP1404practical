from guitar import Guitar


def main():
    """Main function to manage guitars."""
    print("My guitars!")

    guitars = []

    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        # Create a new Guitar instance and add it to the list
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i:>2}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()