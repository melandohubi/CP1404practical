"""CLASS UnreliableCar EXTENDS Car

    METHOD __init__(name, fuel, reliability)
        CALL Superclass.__init__(name, fuel)
        SET self.reliability ← reliability

    METHOD drive(distance)
        random_chance ← RANDOM_FLOAT between 0 and 100        // 0 <= random_chance < 100
        IF random_chance < self.reliability THEN
            // Success: drive as normal
            distance_driven ← CALL Superclass.drive(distance)
            RETURN distance_driven
        ELSE
            // Failure: does not drive
            RETURN 0

    METHOD __str__()
        parent_str ← CALL Superclass.__str__()
        RETURN parent_str + " (Reliability: " + TO_STRING(self.reliability) + "%)"

END CLASS
"""

# unreliable_car.py

from car import Car
import random

class UnreliableCar(Car):
    """A Car that may or may not drive depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """
        Initialize an UnreliableCar instance.

        :param name: str, The name of the car.
        :param fuel: float, The initial amount of fuel.
        :param reliability: float, 0-100, chance that the car actually drives.
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Attempt to drive the car the given distance.
        Only drive if a generated random number is less than reliability.

        :param distance: float, The distance to drive.
        :return: float, the actual distance driven (0 if the car does not drive).
        """
        random_chance = random.uniform(0, 100)
        if random_chance < self.reliability:
            # Car drives as normal
            return super().drive(distance)
        else:
            # Car fails to drive
            return 0

    def __str__(self):
        """Return a string representation including the reliability."""
        return f"{super().__str__()} (Reliability: {self.reliability}%)"
