"""START

CONSTANT MAX_INCREASE ← 0.1
CONSTANT MAX_DECREASE ← 0.05
CONSTANT MIN_PRICE ← 0.01
CONSTANT MAX_PRICE ← 1000.0
CONSTANT INITIAL_PRICE ← 10.0
CONSTANT OUTPUT_FILE ← "output.txt"

SET price ← INITIAL_PRICE
SET day ← 1

OPEN OUTPUT_FILE FOR writing

WRITE "Starting price: $" + FORMAT(price, 2 decimal places) TO OUTPUT_FILE

WHILE price ≥ MIN_PRICE AND price ≤ MAX_PRICE DO
    SET random_choice ← RANDOM integer BETWEEN 1 AND 2

    IF random_choice = 1 THEN
        SET price_change ← RANDOM float BETWEEN 0 AND MAX_INCREASE
    ELSE
        SET price_change ← RANDOM float BETWEEN -MAX_DECREASE AND 0
    ENDIF

    SET price ← price × (1 + price_change)

    WRITE "On day " + day + ": $" + FORMAT(price, 2 decimal places) TO OUTPUT_FILE

    SET day ← day + 1
ENDWHILE

CLOSE OUTPUT_FILE

END
"""



"""
CP1404/CP5632 - Practical
Stock Price Simulator for Capitalist Conrad.
Simulates a volatile stock price over time with random daily changes.
"""

import random

# Constants
MAX_INCREASE = 0.1      # 10%
MAX_DECREASE = 0.05     # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "output.txt"

# Initial setup
price = INITIAL_PRICE
day = 1

# Open the file for writing
with open(OUTPUT_FILE, "w") as out_file:
    out_file.write(f"Starting price: ${price:,.2f}\n")

    # Main simulation loop
    while MIN_PRICE <= price <= MAX_PRICE:
        # Determine daily price change
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)

        # Apply the price change
        price *= (1 + price_change)
        out_file.write(f"On day {day}: ${price:,.2f}\n")
        day += 1
