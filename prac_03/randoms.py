"""IMPORT the random module

# --- Line 1 ---
SET result1 = random.randint(5, 20)
PRINT result1
# result1 >= 5 AND result1 <= 20

# --- Line 2 ---
SET result2 = random.randrange(3, 10, 2)
PRINT result2
# result2 >= 3 AND result2 < 10 AND (result2 - 3) % 2 == 0

# --- Line 3 ---
SET result3 = random.uniform(2.5, 5.5)
PRINT result3
# result3 >= 2.5 AND result3 <= 5.5

# --- Generate a random number between 1 and 100 inclusive ---
SET random_number = random.randint(1, 100)
PRINT random_number
# random_number >= 1 AND random_number <= 100
"""

import random

# Line 1
print(random.randint(5, 20))
# This prints a random integer between 5 and 20 (inclusive).
# Smallest possible: 5
# Largest possible: 20

# Line 2
print(random.randrange(3, 10, 2))
# This prints a random number from the range starting at 3 up to (but not including) 10, stepping by 2.
# Possible values: 3, 5, 7, 9
# Smallest possible: 3
# Largest possible: 9
# Could it produce a 4? No, because step=2 from 3 gives only odd numbers.

# Line 3
print(random.uniform(2.5, 5.5))
# This prints a random floating-point number between 2.5 and 5.5 (inclusive of both ends in theory).
# Smallest possible: Close to 2.5
# Largest possible: Close to 5.5

# Task: Random number between 1 and 100 inclusive
print(random.randint(1, 100))
