"""Start

Define CODE_TO_NAME as a dictionary:
    "QLD" maps to "Queensland"
    "NSW" maps to "New South Wales"
    "NT" maps to "Northern Territory"
    "WA" maps to "Western Australia"
    "ACT" maps to "Australian Capital Territory"
    "VIC" maps to "Victoria"
    "TAS" maps to "Tasmania"
    "SA" maps to "South Australia"

FOR EACH state_code, state_name IN CODE_TO_NAME
    Display state_code + " is " + state_name, formatted neatly
END FOR

Prompt user: "Enter short state: "
Read state_code
Convert state_code to uppercase

WHILE state_code != ""
    TRY
        Display state_code + " is " + CODE_TO_NAME[state_code]
    EXCEPT KeyError
        Display "Invalid short state"
    END TRY

    Prompt user: "Enter short state: "
    Read state_code
    Convert state_code to uppercase
END WHILE

End
"""


"""
CP1404/CP5632 Practical
State names in a dictionary
"""

# Dictionary mapping state codes to state names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Print all states and their names neatly lined up
for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:3} is {state_name}")

print()

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        # Attempt to print state name directly (EAFP approach)
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
