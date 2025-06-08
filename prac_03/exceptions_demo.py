"""START

DISPLAY "Enter the numerator: "
INPUT numerator_string

DISPLAY "Enter the denominator: "
INPUT denominator_string

TRY
    SET numerator ← CONVERT numerator_string TO integer
    SET denominator ← CONVERT denominator_string TO integer

    IF denominator = 0 THEN
        DISPLAY "Cannot divide by zero!"
    ELSE
        SET fraction ← numerator ÷ denominator
        DISPLAY fraction
    ENDIF

CATCH ValueError
    DISPLAY "Numerator and denominator must be valid integers!"

ENDTRY

DISPLAY "Finished."

END
"""


"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - A ValueError occurs when the input is not a valid integer (e.g., letters or special characters).
2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError occurs when the denominator entered is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, by checking if the denominator is 0 before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid integers!")

print("Finished.")
