def main():
    """Calculate the total price of items in a shop."""

    while True:
        try:
            num_items = int(input("Number of items: "))
            if num_items < 0:
                print("Invalid number of items! Please enter a non-negative integer.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    total_price = 0.0

    for i in range(num_items):
        while True:
            try:
                price = float(input(f"Price of item {i + 1}: "))
                if price < 0:
                    print("Invalid price! Please enter a non-negative value.")
                else:
                    total_price += price
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    if total_price > 100:
        total_price *= 0.9

    print(f"Total price for {num_items} items is ${total_price:.2f}")

if __name__ == "__main__":
    main()