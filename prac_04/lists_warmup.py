"""SET numbers TO [3, 1, 4, 1, 5, 9, 2]

# Accessing values
numbers[0]         → RETURNS 3
numbers[-1]        → RETURNS 2
numbers[3]         → RETURNS 1
numbers[:-1]       → RETURNS [3, 1, 4, 1, 5, 9]
numbers[3:4]       → RETURNS [1]

# Membership checks
IF 5 == ANY element IN numbers THEN
    RETURN True
ELSE
    RETURN False

IF 7 == ANY element IN numbers THEN
    RETURN True
ELSE
    RETURN False

IF "3" == ANY element IN numbers THEN
    RETURN True
ELSE
    RETURN False

# Concatenation
SET result TO numbers + [6, 5, 3]  → RETURNS [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Modifications
SET numbers[0] TO "ten"     # Replace first element with "ten"
SET numbers[-1] TO 1        # Replace last element with 1

# Slicing
PRINT all elements in numbers WHERE index >= 2

# Check if 9 exists in numbers
IF 9 == ANY element IN numbers THEN
    PRINT True
ELSE
    PRINT False
"""



numbers = [3, 1, 4, 1, 5, 9, 2]

# Predictions:
# numbers[0]        -> 3
# numbers[-1]       -> 2
# numbers[3]        -> 1
# numbers[:-1]      -> [3, 1, 4, 1, 5, 9]
# numbers[3:4]      -> [1]
# 5 in numbers      -> True
# 7 in numbers      -> False
# "3" in numbers    -> False  (because "3" is a string, not an integer)
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Now, do the following changes and prints:

# Change the first element of numbers to "ten"
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
