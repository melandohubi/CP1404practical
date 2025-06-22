"""BEGIN

FUNCTION read_wimbledon_data(filename)
    OPEN file with name filename FOR reading, with encoding "utf-8-sig"
    READ and ignore the first line (header)
    INITIALIZE data_list AS empty list
    FOR EACH row IN file
        APPEND row TO data_list
    RETURN data_list
END FUNCTION

FUNCTION count_champion_wins(data)
    INITIALIZE champion_to_wins AS empty dictionary with default value 0
    FOR EACH row IN data
        champion ← row[2]
        champion_to_wins[champion] ← champion_to_wins[champion] + 1
    RETURN champion_to_wins
END FUNCTION

FUNCTION get_unique_countries(data)
    INITIALIZE countries AS empty set
    FOR EACH row IN data
        country ← row[1]
        ADD country TO countries
    RETURN SORTED list of countries
END FUNCTION

FUNCTION display_results(champion_wins, countries)
    DISPLAY "Wimbledon Champions:"
    FOR EACH champion, wins IN champion_wins
        DISPLAY champion + " " + wins
    DISPLAY "These " + LENGTH(countries) + " countries have won Wimbledon:"
    DISPLAY countries JOINED BY ", "
END FUNCTION

FUNCTION main
    filename ← "wimbledon.csv"
    data ← CALL read_wimbledon_data(filename)
    champion_wins ← CALL count_champion_wins(data)
    countries ← CALL get_unique_countries(data)
    CALL display_results(champion_wins, countries)
END FUNCTION

CALL main

END
"""

"""
Program to process Wimbledon gentlemen's singles champions data.

Estimated time: 25 minutes  
Actual time: 22 minutes
"""

import csv
from collections import defaultdict

def read_wimbledon_data(filename):
    """Read the Wimbledon data file and return list of rows."""
    with open(filename, mode="r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        return [row for row in reader]

def count_champion_wins(data):
    """Count how many times each champion has won."""
    champion_to_wins = defaultdict(int)
    for row in data:
        champion = row[2]
        champion_to_wins[champion] += 1
    return champion_to_wins

def get_unique_countries(data):
    """Get a sorted list of unique countries from the data."""
    countries = {row[1] for row in data}
    return sorted(countries)

def display_results(champion_wins, countries):
    """Display the champions and countries."""
    print("Wimbledon Champions:")
    for champion, wins in champion_wins.items():
        print(f"{champion} {wins}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champion_wins = count_champion_wins(data)
    countries = get_unique_countries(data)
    display_results(champion_wins, countries)

if __name__ == "__main__":
    main()
