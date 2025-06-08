"""PROMPT "Enter your name: " AND STORE IN name
OPEN "name.txt" FOR writing AND STORE IN out_file
WRITE name TO out_file
CLOSE out_file
"""

"""OPEN "name.txt" FOR reading AND STORE IN in_file
READ contents of in_file AND STORE IN name
CLOSE in_file
PRINT "Hi " + name + "!"
"""

"""OPEN "numbers.txt" FOR reading USING with statement AS file
    READ all lines FROM file AND STORE IN lines
    CONVERT lines[0] TO integer AND STORE IN number1
    CONVERT lines[1] TO integer AND STORE IN number2
    total = number1 + number2
    PRINT total
END WITH
"""

"""SET total = 0
OPEN "numbers.txt" FOR reading USING with statement AS file
    FOR each line IN file:
        CONVERT line TO integer AND ADD TO total
END WITH
PRINT total
"""

# ----- Task 1 -----
# Ask user for name, write it to name.txt using open and close

name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()


# ----- Task 2 -----
# Read name from name.txt and print greeting, using open and close

in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Hi {name}!")


# ----- Task 3 -----
# Read the first two numbers from numbers.txt, add them and print the result
# Use with and readlines() here

with open("numbers.txt", "r") as file:
    lines = file.readlines()
    number1 = int(lines[0])
    number2 = int(lines[1])
    total = number1 + number2
    print(total)  # Should print 59


# ----- Task 4 -----
# Read all numbers in numbers.txt and print their total
# Use with and a for loop (for line in file)

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print(total)  # Should print 459 for 17 + 42 + 400
