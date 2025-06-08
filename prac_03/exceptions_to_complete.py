"""START

SET is_finished ← False

WHILE is_finished = False DO
    TRY
        DISPLAY "Enter a valid integer: "
        INPUT user_input
        SET result ← CONVERT user_input TO integer
        SET is_finished ← True
    CATCH ValueError
        DISPLAY "Please enter a valid integer."
    ENDTRY
ENDWHILE

DISPLAY "Valid result is: " + result

END
"""

"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # TODO: this line
    except ValueError:  # TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", result)
