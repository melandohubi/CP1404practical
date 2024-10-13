"""
CP1404/CP5632 Practical
Cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))  # Renamed from 'months' to 'num_months'

    # Collect incomes for each month
    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Using f-string
        incomes.append(income)

    # Print the income report
    print_income_report(incomes, num_months)

def print_income_report(incomes, num_months):
    """Prints the income report based on the provided incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")  # Using f-string

main()