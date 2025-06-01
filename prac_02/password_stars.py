"""FUNCTION get_password()
    DISPLAY "Enter your password: "
    READ password
    RETURN password
END FUNCTION


FUNCTION print_asterisks(password)
    length ← LENGTH OF password
    FOR i FROM 1 TO length DO
        DISPLAY "*" WITHOUT NEW LINE
    END FOR
    DISPLAY NEW LINE
END FUNCTION


FUNCTION main()
    DISPLAY "Enter your username: "
    READ username

    password ← CALL get_password()

    IF password == "secret" THEN
        DISPLAY "Welcome, " + username + "!"
    ELSE
        DISPLAY "Invalid password."
    END IF

    CALL print_asterisks(password)
END FUNCTION


IF program is being run directly THEN
    CALL main()
END IF
"""



def get_password():
    """Function to get the password from the user."""
    return input("Enter your password: ")


def print_asterisks(password):
    """Function to print asterisks based on the password length."""
    print('*' * len(password))


def main():
    """Main function to execute the password check."""
    username = input("Enter your username: ")

    password = get_password()

    if password == "secret":
        print(f"Welcome, {username}!")
    else:
        print("Invalid password.")

    print_asterisks(password)


if __name__ == "__main__":
    main()
