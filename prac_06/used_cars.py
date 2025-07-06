"""
CP1404/CP5632 Practical - Client code to use the Car class.
"""

"""IMPORT Car class from prac_06.car module

FUNCTION main
    CREATE my_car AS new Car with fuel = 180

    CALL my_car.drive(30)
    SET distance_driven TO result of my_car.drive(30)

    PRINT "Car has fuel remaining: " + my_car.fuel
    PRINT "Distance driven this trip: " + distance_driven
    PRINT my_car  # This calls the Car's __str__ method

END FUNCTION

IF this file is the main program THEN
    CALL main()
END IF
"""

from prac_06.car import Car  # Import Car class from the prac_06 package


def main():
    """Demo test code to show how to use Car class."""
    my_car = Car(180)          # Create Car instance with 180 units of fuel
    distance_driven = my_car.drive(30)  # Drive 30 km
    print(f"Car has fuel remaining: {my_car.fuel:.2f} units")
    print(f"Distance driven this trip: {distance_driven} km")
    print(my_car)              # Uses Car's __str__ method to print status


if __name__ == "__main__":
    main()
