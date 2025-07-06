"""FUNCTION main()
    PRINT "My guitars!"
    SET guitars = empty list

    LOOP FOREVER
        PROMPT "Name: " AND STORE IN name
        IF name == "" THEN
            BREAK LOOP
        PROMPT "Year: " AND STORE IN year AS INTEGER
        PROMPT "Cost: $" AND STORE IN cost AS FLOAT

        CREATE new_guitar = Guitar(name, year, cost)
        ADD new_guitar TO guitars
        PRINT new_guitar + " added."
    END LOOP

    PRINT "These are my guitars:"
    FOR EACH guitar IN guitars WITH index i STARTING FROM 1
        SET vintage_string = " (vintage)" IF guitar.is_vintage() == True ELSE ""
        PRINT "Guitar " + i + ": " + guitar.name right-aligned 20 + " (" + guitar.year + "), worth $" + guitar.cost formatted to 2 decimals + vintage_string
    END FOR
END FUNCTION
"""

def main():
    print("My guitars!")
    guitars = []

    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")

    # Uncomment these lines for testing without manual input:
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == '__main__':
    main()
