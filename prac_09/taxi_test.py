# 1. Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
my_taxi = Taxi("Prius 1", 100, 1.23)

# 2. Drive the taxi 40 km
my_taxi.drive(40)

# 3. Print the taxi's details and the current fare
print(my_taxi)  # Assuming __str__ or __repr__ is implemented in Taxi class
print("Current fare:", my_taxi.get_fare())  # Assuming get_fare() method exists

# 4. Restart the meter (start a new fare) and then drive the car 100 km
my_taxi.restart_meter()
my_taxi.drive(100)

# 5. Print the details and the current fare
print(my_taxi)  # Print taxi details again
print("Current fare:", my_taxi.get_fare())  # Print current fare again