"""FUNCTION get_valid_score()
    LOOP FOREVER
        DISPLAY "Enter a score (0–100): "
        READ input_value

        TRY TO CONVERT input_value TO FLOAT → score
        IF score >= 0 AND score <= 100 THEN
            RETURN score
        ELSE
            DISPLAY "Invalid score! Please enter a number between 0 and 100."
        END IF

    IF conversion fails THEN
        DISPLAY "Invalid input! Please enter a numeric value."
    END LOOP
END FUNCTION


FUNCTION determine_result(score)
    IF score >= 90 THEN
        RETURN "Excellent"
    ELSE IF score >= 75 THEN
        RETURN "Good"
    ELSE IF score >= 50 THEN
        RETURN "Passable"
    ELSE
        RETURN "Bad"
    END IF
END FUNCTION


FUNCTION show_stars(score)
    stars_count ← CONVERT score TO INTEGER
    FOR i FROM 1 TO stars_count DO
        DISPLAY "*" WITHOUT NEW LINE
    END FOR
    DISPLAY NEW LINE
END FUNCTION


FUNCTION main()
    score ← CALL get_valid_score()

    LOOP FOREVER
        DISPLAY NEW LINE
        DISPLAY "Menu:"
        DISPLAY "(G)et a valid score"
        DISPLAY "(P)rint result"
        DISPLAY "(S)how stars"
        DISPLAY "(Q)uit"

        DISPLAY ">>> "
        READ choice
        CONVERT choice TO UPPERCASE

        IF choice == "G" THEN
            score ← CALL get_valid_score()
        ELSE IF choice == "P" THEN
            result ← CALL determine_result(score)
            DISPLAY "Result: " + result
        ELSE IF choice == "S" THEN
            CALL show_stars(score)
        ELSE IF choice == "Q" THEN
            DISPLAY "Thank you for using the program. Farewell!"
            EXIT LOOP
        ELSE
            DISPLAY "Invalid option! Please choose again."
        END IF
    END LOOP
END FUNCTION


IF program is run directly THEN
    CALL main()
END IF
"""




def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    while True:
        try:
            score = float(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score! Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def determine_result(score):
    """Determine the result based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print stars corresponding to the score."""
    print('*' * int(score))


def main():
    """Main function to run the menu-driven program."""
    score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input(">>> ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Thank you for using the program. Farewell!")
            break
        else:
            print("Invalid option! Please choose again.")

if __name__ == "__main__":
    main()
