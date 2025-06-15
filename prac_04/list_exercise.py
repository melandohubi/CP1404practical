"""BEGIN

    INITIALIZE numbers AS empty list

    FOR counter FROM 1 TO 5 DO
        PROMPT user for number
        CONVERT input TO integer
        APPEND number TO numbers
    END FOR

    DISPLAY "The first number is" numbers[0]
    DISPLAY "The last number is" numbers[length of numbers - 1]
    DISPLAY "The smallest number is" MIN(numbers)
    DISPLAY "The largest number is" MAX(numbers)
    DISPLAY "The average of the numbers is" SUM(numbers) / LENGTH(numbers)

    SET usernames TO [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
        'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
        'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
    ]

    PROMPT user to enter username
    STORE input AS user_input

    IF user_input IS IN usernames THEN
        DISPLAY "Access granted"
    ELSE
        DISPLAY "Access denied"
    END IF

END
"""

"""
CP1404/CP5632 Practical
List exercises - number summary and basic username access check
"""

# --- Part 1: Number analysis ---

numbers = []

for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# --- Part 2: Security checker ---

usernames = [
    'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
    'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
]

user_input = input("\nEnter your username: ")

if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")
