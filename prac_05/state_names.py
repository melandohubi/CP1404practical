from operator import itemgetter

# Dictionary to store state codes and names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Display the dictionary
print("State Codes and Names:")
for code, name in sorted(CODE_TO_NAME.items()):
    print(f"{code}: {name}")

# Input loop for state codes
state_code = input("\nEnter short state code (or press Enter to quit): ")
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state code")
    state_code = input("Enter short state code (or press Enter to quit): ")