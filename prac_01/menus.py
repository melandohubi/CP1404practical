def main():
    """Greeting program that interacts with the user."""

    name = input("Enter name: ")

    while True:
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")

        choice = input(">>> ").strip().upper()

        if choice == 'H':
            print(f"Hello {name}")
        elif choice == 'G':
            print(f"Goodbye {name}")
        elif choice == 'Q':
            print("Finished")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()