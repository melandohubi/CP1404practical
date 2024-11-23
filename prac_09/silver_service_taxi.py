from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes a flagfall and fanciness multiplier."""

    flagfall = 4.50  # Class variable for the flagfall charge

    def __init__(self, name, fuel, price_per_km, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel, price_per_km)  # Call the parent class constructor
        self.fanciness = fanciness  # Set the fanciness attribute
        self.price_per_km *= fanciness  # Scale price_per_km by fanciness

    def get_fare(self):
        """Return the total fare including flagfall."""
        return super().get_fare() + self.flagfall  # Include flagfall in fare calculation

    def __str__(self):
        """Return a string representation including the flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"