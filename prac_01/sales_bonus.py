def calculate_bonus(sales):
    if sales < 0:
        return None
    elif sales < 1000:
        return sales * 0.10
    elif sales <= 2000:
        return 150 + (sales - 1000) * 0.15
    else:
        return 300 + (sales - 2000) * 0.20


def main():
    sales = float(input("Enter sales: $"))

    while sales >= 0:
        bonus = calculate_bonus(sales)
        if bonus is not None:
            print(f"Bonus: ${bonus:.2f}")
        sales = float(input("Enter sales: $"))


if __name__ == "__main__":
    main()