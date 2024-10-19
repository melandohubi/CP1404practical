from operator import itemgetter

def read_data(filename):
    """Read the data from the given file and return a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        data = [line.strip().split(",") for line in in_file.readlines()[1:]]  # Skip header
    return data

def count_champions(data):
    """Count the occurrences of each champion."""
    champion_counts = {}
    for entry in data:
        champion = entry[2]  # Champion's name is in the third column
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts

def get_unique_countries(data):
    """Get a set of unique countries from the champion's country."""
    countries = set()
    for entry in data:
        countries.add(entry[1])  # Champion's country is in the second column
    return countries

def main():
    filename = "wimbledon_champions.csv"  # Replace with your filename
    data = read_data(filename)

    # Count champions
    champion_counts = count_champions(data)

    # Calculate the maximum width for champions and counts
    champion_width = max(len(champion) for champion in champion_counts.keys())
    count_width = max(len(str(count)) for count in champion_counts.values())

    # Sort and display the champions and their win counts
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_counts.items(), key=itemgetter(1), reverse=True):
        print(f"{champion:<{champion_width}} = {count:{count_width}}")

    # Get and output the unique countries
    unique_countries = get_unique_countries(data)
    sorted_countries = sorted(unique_countries)
    print("\nThese countries have won Wimbledon:")
    print(", ".join(sorted_countries))

if __name__ == "__main__":
    main()