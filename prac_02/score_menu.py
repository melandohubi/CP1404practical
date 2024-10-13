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