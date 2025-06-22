"""Start

Define COLOUR_TO_HEX as a dictionary:
    "AliceBlue" maps to "#f0f8ff"
    "AntiqueWhite" maps to "#faebd7"
    "Aqua" maps to "#00ffff"
    "Aquamarine" maps to "#7fffd4"
    "Azure" maps to "#f0ffff"
    "Beige" maps to "#f5f5dc"
    "Bisque" maps to "#ffe4c4"
    "Black" maps to "#000000"
    "BlanchedAlmond" maps to "#ffebcd"
    "Blue" maps to "#0000ff"

Display "Available colours:"
FOR EACH colour IN COLOUR_TO_HEX
    Display colour
END FOR

Prompt user: "Enter colour name: "
Read colour_name
Convert colour_name to title case

WHILE colour_name != ""
    TRY
        Display "The hex code for " + colour_name + " is " + COLOUR_TO_HEX[colour_name]
    EXCEPT KeyError
        Display "Invalid colour name"
    END TRY

    Prompt user: "Enter colour name: "
    Read colour_name
    Convert colour_name to title case
END WHILE

Display "Goodbye!"

End
"""

"""
Hexadecimal Colour Code Lookup Program
"""

# Constant dictionary mapping colour names to hex codes
COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

# Print all available colours
print("Available colours:")
for colour in COLOUR_TO_HEX:
    print(colour)

print()

# Start user input loop
colour_name = input("Enter colour name: ").title()  # Case-insensitive input
while colour_name != "":
    try:
        print(f"The hex code for {colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()

print("Goodbye!")
