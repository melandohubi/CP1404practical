import random

MAX_INCREASE = 0.1
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 1000.0

INITIAL_PRICE = float(input("Enter initial stock price: "))

price = INITIAL_PRICE
print(f"Starting Price: ${price:,.2f}")

days = int(input("Enter number of days to simulate: "))
price_history = [price]

for day in range(days):
    if MIN_PRICE <= price <= MAX_PRICE:
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        price_history.append(price)
        print(f"Day {day + 1}: ${price:,.2f}")
    else:
        break

print("Price history:", [f"${p:,.2f}" for p in price_history])