import csv
import random

# Travel Tracker Program
# Author: Melando Vrierto Hubi
# Description: An interactive program to track places to visit and those already visited.

# Constants
VISITED = 'y'
UNVISITED = 'n'

# Place data structure
class Place:
    def __init__(self, name, country, priority, visited):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __str__(self):
        visited_marker = '*' if self.visited else ''
        return f"{visited_marker}{self.priority}. {self.name} in {self.country} {self.priority}"

def load_places(filename):
    """Load places from a CSV file."""
    places = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, country, priority, visited = row
                places.append(Place(name, country, int(priority), visited.lower() == VISITED))
    except FileNotFoundError:
        print("File not found. Initializing with default places.")
        # Default places with associated countries
        default_places = [
            ["Lima", "Peru", 3, UNVISITED],
            ["Auckland", "New Zealand", 1, VISITED],
            ["Rome", "Italy", 12, UNVISITED],
            ["Xanadu", "Atlantis", 4, UNVISITED],
            ["Malaga", "Spain", 2, UNVISITED]
        ]
        for row in default_places:
            places.append(Place(row[0], row[1], int(row[2]), row[3] == VISITED))
    return places

def display_places(places):
    """Display all places with their details."""
    for place in sorted(places, key=lambda x: (-x.visited, -x.priority)):
        print(place)
    unvisited_count = sum(not place.visited for place in places)
    print(f"{len(places)} places tracked. You still want to visit {unvisited_count} places.")

def recommend_place(places):
    """Recommend a random unvisited place."""
    unvisited_places = [place for place in places if not place.visited]
    if unvisited_places:
        recommended = random.choice(unvisited_places)
        print(f"Not sure where to visit next?\nHow about... {recommended.name} in {recommended.country}?")
    else:
        print("No places left to visit!")

def mark_visited(places):
    """Mark a selected place as visited."""
    display_places(places)
    try:
        choice = int(input("Enter the number of a place to mark as visited\n>>> "))
        if choice < 1 or choice > len(places):
            print("Invalid place number")
            return
        if places[choice - 1].visited:
            print(f"You have already visited {places[choice - 1].name}")
            return
        places[choice - 1].visited = True
        print(f"{places[choice - 1].name} in {places[choice - 1].country} visited!")
    except ValueError:
        print("Invalid input; enter a valid number")

def add_place(places):
    """Add a new place to the tracker."""
    name = input("Name:\n")
    while not name.strip():
        print("Input can not be blank")
        name = input("Name:\n")

    country = input("Country:\n")
    while not country.strip():
        print("Input can not be blank")
        country = input("Country:\n")

    priority = input("Priority:\n")
    while not priority.isdigit() or int(priority) <= 0:
        print("Number must be > 0")
        priority = input("Priority:\n")

    places.append(Place(name, country, int(priority), False))
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")

def main():
    """Main function to run the Travel Tracker program."""
    filename = "places.csv"
    places = load_places(filename)

    print(f"Travel Tracker 1.0 - by Lindsay Ward")
    print(f"{len(places)} places loaded from {filename}")

    while True:
        print("\nMenu:")
        print("D - Display all places")
        print("R - Recommend a random place")
        print("A - Add a new place")
        print("M - Mark a place as visited")
        print("Q - Quit")

        choice = input(">>> ").strip().lower()

        if choice == 'd':
            display_places(places)
        elif choice == 'r':
            recommend_place(places)
        elif choice == 'a':
            add_place(places)
        elif choice == 'm':
            mark_visited(places)
        elif choice == 'q':
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for place in places:
                    writer.writerow([place.name, place.country, place.priority, VISITED if place.visited else UNVISITED])
            print(f"{len(places)} places saved to {filename}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")

if __name__ == "__main__":
    main()
