"""BEGIN

SET name TO "Gibson L-5 CES"
SET year TO 1922
SET cost TO 16035.9

# --- String Formatting Examples ---

PRINT "My guitar: " + name + ", first made in " + CONVERT year TO STRING

PRINT "My guitar: {}, first made in {}".format(name, year)
PRINT "My guitar: {0}, first made in {1}".format(name, year)
PRINT "My {0} was first made in {1} (that's right, {1}!)".format(name, year)

PRINT f"My {name} was first made in {year} (that's right, {year}!)"

PRINT "My {} would cost ${:,.2f}".format(name, cost)
PRINT f"My {name} would cost ${cost:,.2f}"

# --- Loop through numbers with alignment ---
SET numbers TO [1, 19, 123, 456, -25]
FOR i FROM 1 TO LENGTH OF numbers
    SET number TO numbers[i - 1]
    PRINT f"Number {i} is {number:5}"
END FOR

# --- Required Task 1: f-string formatted guitar message ---
PRINT f"{year} {name} for about ${cost:,.0f}!"

# --- Required Task 2: Powers of 2 formatted output ---
FOR exponent FROM 0 TO 10 INCLUSIVE
    SET power TO 2 RAISED TO exponent
    PRINT f"2 ^{exponent:2} is {power:4}"
END FOR

END
"""

# String formatting examples

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# Old style (not recommended)
print("My guitar: " + name + ", first made in " + str(year))

# Using .format()
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Using f-strings (recommended)
print(f"My {name} was first made in {year} (that's right, {year}!)")

# Currency formatting with 2 decimal places and commas
print("My {} would cost ${:,.2f}".format(name, cost))  # Using .format()
print(f"My {name} would cost ${cost:,.2f}")  # Using f-string

# Aligning numbers with width
numbers = [1, 19, 123, 456, -25]
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# -------------------------------
# Required Task 1: F-string output
# -------------------------------
print(f"{year} {name} for about ${cost:,.0f}!")

# -------------------------------
# Required Task 2: Powers of 2 loop
# -------------------------------
for exponent in range(11):
    power = 2 ** exponent
    print(f"2 ^{exponent:2} is {power:4}")
