"""CLASS Car
    ATTRIBUTE fuel
    ATTRIBUTE odometer

    METHOD __init__(fuel=0)
        SET self.fuel TO fuel
        SET self.odometer TO 0

    METHOD add_fuel(amount)
        self.fuel = self.fuel + amount

    METHOD drive(distance)
        IF distance > self.fuel THEN
            SET distance TO self.fuel
            SET self.fuel TO 0
        ELSE
            self.fuel = self.fuel - distance
        ENDIF

        self.odometer = self.odometer + distance
        RETURN distance
ENDCLASS
"""

class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out. Return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of the car's status."""
        return f"Car(fuel={self.fuel:.2f}, odometer={self._odometer:.2f} km)"


# Example usage:
if __name__ == "__main__":
    car = Car(10)  # Start with 10 units of fuel
    print(car)     # Car(fuel=10.00, odometer=0.00 km)

    distance_driven = car.drive(5)
    print(f"Driven: {distance_driven} km")
    print(car)     # Car(fuel=5.00, odometer=5.00 km)

    car.add_fuel(20)
    print(car)     # Car(fuel=25.00, odometer=5.00 km)

    distance_driven = car.drive(30)
    print(f"Driven: {distance_driven} km")
    print(car)     # Car(fuel=0.00, odometer=30.00 km)
