"""CLASS Taxi EXTENDS Car

    CLASS Taxi EXTENDS Car

    // Class variable, shared by all Taxis
    price_per_km ← 1.23

    METHOD __init__(name, fuel)
        // Initialize parent Car with name and fuel
        CALL SUPER.__init__(name, fuel)
        // Start fare distance at zero
        current_fare_distance ← 0

    METHOD start_fare()
        // Reset fare distance for a new fare
        current_fare_distance ← 0

    METHOD get_fare()
        // Calculate trip fare: price per km times fare distance, rounded to 2 decimals
        fare ← price_per_km × current_fare_distance
        RETURN ROUND(fare, 2)

    METHOD drive(distance)
        // Use parent Car drive method to actually move and use fuel
        distance_driven ← CALL SUPER.drive(distance)
        // Track fare distance (could be less than 'distance' if not enough fuel)
        current_fare_distance ← current_fare_distance + distance_driven
        RETURN distance_driven

    METHOD __str__()
        // Combine Car string with fare distance for pretty printing
        parent_str ← CALL SUPER.__str__()
        RETURN parent_str + " | " + TO_STRING(current_fare_distance) + "km on current fare"

END CLASS
"""

# taxi.py

from car import Car  # Assumes Car is implemented in car.py

class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    # Class variable, shared by all Taxi instances
    price_per_km = 1.23

    def __init__(self, name, fuel):
        """Initialise a Taxi.

        Args:
            name (str): Name of the taxi.
            fuel (float): Fuel available.
        """
        # Initialise the parent Car class
        super().__init__(name, fuel)
        # Start with zero distance for the current fare
        self.current_fare_distance = 0

    def start_fare(self):
        """Reset the fare distance for a new fare."""
        self.current_fare_distance = 0

    def get_fare(self):
        """Calculate and return the fare for the current trip."""
        return round(self.price_per_km * self.current_fare_distance, 2)

    def drive(self, distance):
        """Drive like parent Car, but also track fare distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

    def __str__(self):
        """Return a string representation of the Taxi, including current fare."""
        return f"{super().__str__()} | {self.current_fare_distance}km on current fare"

# Make sure your Car class has at least a working __str__ and drive methods!
