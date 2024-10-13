import random

# Constants
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    # Ask the user how many quick picks to generate
    num_picks = int(input("How many quick picks? "))

    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in sorted(quick_pick)))

def generate_quick_pick():
    """Generate a list of unique random numbers."""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:  # Ensure no duplicates
            numbers.append(number)
    return numbers

main()