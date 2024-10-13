# List of authorized usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']

# Prompt the user for their username
user_input = input("Enter your username: ")

# Check if the username is in the list and print the appropriate message
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")