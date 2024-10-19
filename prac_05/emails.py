def extract_name(email):
    """Extracts and formats the name from the email."""
    # Split the email at '@' and take the part before it
    name_part = email.split('@')[0]
    # Replace dots and underscores with spaces, then title case
    name = name_part.replace('.', ' ').replace('_', ' ').title()
    return name


def main():
    user_dict = {}

    while True:
        email = input("Email: ")
        if not email:
            break

        # Extract name from the email
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n): ").strip().lower()

        if confirmation not in ('', 'y'):
            name = input("Name: ").strip()

        user_dict[email] = name

    # Calculate maximum width for names and emails for formatting
    name_width = max(len(name) for name in user_dict.values())
    email_width = max(len(email) for email in user_dict.keys())

    # Sort and display the items in the dictionary
    for email, name in sorted(user_dict.items(), key=lambda item: item[1]):
        print(f"{name:<{name_width}} ({email:<{email_width}})")


if __name__ == "__main__":
    main()