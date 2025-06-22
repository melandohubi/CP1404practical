"""
BEGIN

FUNCTION extract_name_from_email(email)
    username_part ← SPLIT email AT "@"
    name_parts ← SPLIT username_part[0] AT "."
    formatted_name ← JOIN name_parts WITH SPACES
    RETURN title_case(formatted_name)
END FUNCTION

DECLARE email_to_name AS empty dictionary

PROMPT "Email: " AND STORE IN email

WHILE email != ""
    default_name ← CALL extract_name_from_email(email)

    PROMPT "Is your name " + default_name + "? (Y/n) " AND STORE IN confirmation
    SET confirmation TO LOWERCASE(TRIM(confirmation))

    IF confirmation == "" OR confirmation == "y" OR confirmation == "yes" THEN
        name ← default_name
    ELSE
        PROMPT "Name: " AND STORE IN name
    END IF

    SET email_to_name[email] = name

    PROMPT "Email: " AND STORE IN email
END WHILE

FOR EACH email, name IN email_to_name
    DISPLAY name + " (" + email + ")"
END FOR

END
"""


"""
Program to store users' emails and names in a dictionary.

Estimated time: 20 minutes  
Actual time: 18 minutes
"""

def extract_name_from_email(email):
    """Extract a name from the email address."""
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name

def main():
    """Main program to collect and display email-name pairs."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        default_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {default_name}? (Y/n) ").strip().lower()
        if confirmation in ('', 'y', 'yes'):
            name = default_name
        else:
            name = input("Name: ").strip()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
