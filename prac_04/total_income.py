"""BEGIN

    FUNCTION main
        SET incomes TO an empty list

        DISPLAY "How many months?"
        GET user input AND STORE AS number_of_months

        FOR month FROM 1 TO number_of_months DO
            DISPLAY "Enter income for month" + month
            GET user input AND STORE AS income (converted to float)
            APPEND income TO incomes
        END FOR

        CALL print_income_report(incomes)
    END FUNCTION


    FUNCTION print_income_report(incomes)
        DISPLAY "Income Report"
        DISPLAY "-------------"

        SET total TO 0

        FOR month FROM 1 TO LENGTH of incomes DO
            SET income TO incomes[month - 1]
            SET total TO total + income

            DISPLAY formatted "Month", month, "Income", income, "Total", total
        END FOR
    END FUNCTION

    CALL main

END
"""


"""
CP1404/CP5632 Practical
Refactored code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Step 3: f-string used here
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    """Print the income report showing each month's income and cumulative total."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")
