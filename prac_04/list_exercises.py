# Program to prompt the user for 5 numbers and output information about them

def main():
    numbers = []  # List to store the numbers

    # Prompt the user for 5 numbers
    for i in range(5):
        number = float(input(f"Number: "))  # Input prompt using f-string
        numbers.append(number)  # Append the number to the list

    # Calculate required statistics
    first_number = numbers[0]
    last_number = numbers[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average_number = sum(numbers) / len(numbers)

    # Output the results
    print(f"The first number is {first_number}")
    print(f"The last number is {last_number}")
    print(f"The smallest number is {smallest_number}")
    print(f"The largest number is {largest_number}")
    print(f"The average of the numbers is {average_number:.1f}")

main()