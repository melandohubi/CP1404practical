"""1. When will a ValueError occur?
A ValueError will occur in the following situations:
If the user inputs a value for either the numerator or denominator that cannot be converted to an integer. For example:
Entering a non-numeric string (e.g., "abc").
Entering a floating-point number (e.g., "3.14") since int() cannot convert it directly without raising an error.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the user inputs 0 as the denominator. In mathematical terms, division by zero is undefined, and Python raises this error to indicate that the operation cannot be performed.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, we can modify the code to check if the denominator is zero before performing the division. Here’s how you can do it:"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        raise ZeroDivisionError

    fraction = numerator / denominator
    print(f"Result: {fraction}")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")