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