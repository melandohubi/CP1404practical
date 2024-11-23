import random
from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that has a reliability factor."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)  # Call the parent class constructor
        self.reliability = reliability  # Set the reliability attribute

    def drive(self, distance):
        """Drive the car if a random number is less than reliability."""
        chance = random.uniform(0, 100)  # Generate a random number between 0 and 100

        if chance < self.reliability:
            return super().drive(distance)  # Call the parent class's drive method
        else:
            return 0  # If the drive fails, return 0 km driven