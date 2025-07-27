"""BEGIN

    // Create a Taxi object named "Prius 1" with 100 units of fuel
    my_taxi ← NEW Taxi("Prius 1", 100)

    // Drive 40 km with the taxi
    actual_distance_driven ← my_taxi.Drive(40)

    // Print the taxi's details and current fare
    PRINT my_taxi.ToString()
    PRINT "Current fare: $" + my_taxi.GetFare()

    // Restart the fare meter (start new fare)
    my_taxi.StartFare()

    // Drive the taxi 100 km
    actual_distance_driven ← my_taxi.Drive(100)

    // Print the taxi's details and current fare
    PRINT my_taxi.ToString()
    PRINT "Current fare: $" + my_taxi.GetFare()

END
"""

# taxi_test.py

from taxi import Taxi

def main():
    # 1. Create a new Taxi with name "Prius 1", 100 units of fuel
    my_taxi = Taxi("Prius 1", 100)

    # 2. Drive the taxi 40 km
    my_taxi.drive(40)

    # 3. Print the taxi's details and the current fare
    print(f"{my_taxi}")
    print(f"Current fare: ${my_taxi.get_fare()}")

    # 4. Restart the meter (start a new fare)
    my_taxi.start_fare()

    # 5. Drive the taxi 100 km
    my_taxi.drive(100)

    # 6. Print the details and the current fare
    print(f"{my_taxi}")
    print(f"Current fare: ${my_taxi.get_fare()}")

if __name__ == '__main__':
    main()
