"""CLASS SilverServiceTaxi EXTENDS Taxi

    // Class variable for the flagfall amount
    flagfall ← 4.50

    METHOD __init__(name, fuel, fanciness)
        // Initialize parent Taxi with name and fuel
        CALL SUPER.__init__(name, fuel)
        // Calculate and store this object's price per km using base
        self.price_per_km ← Taxi.price_per_km × fanciness
        self.fanciness ← fanciness

    METHOD get_fare()
        // Calculate fare as (price_per_km × distance) plus flagfall
        base_fare ← CALL SUPER.get_fare()
        total_fare ← base_fare + self.flagfall
        RETURN ROUND(total_fare, 2)

    METHOD __str__()
        parent_string ← CALL SUPER.__str__()
        RETURN parent_string + ", $" + FORMAT(self.price_per_km, 2) +
                "/km plus flagfall of $" + FORMAT(self.flagfall, 2)

END CLASS
"""

# silver_service_taxi.py

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A more expensive, fanciness-scaled taxi."""

    flagfall = 4.50  # Class variable: extra charge per trip

    def __init__(self, name, fuel, fanciness):
        """
        Initialize a SilverServiceTaxi.

        :param name: str, the name of the taxi
        :param fuel: float, starting amount of fuel
        :param fanciness: float, multiplies the base price per km
        """
        super().__init__(name, fuel)
        # Set the price per km for this instance using the original base value and fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
        self.fanciness = fanciness

    def get_fare(self):
        """
        Return the fare for the trip including flagfall.
        """
        base_fare = super().get_fare()  # Fare based on price per km and distance
        total_fare = base_fare + self.flagfall
        return round(total_fare, 2)

    def __str__(self):
        return (f"{super().__str__()}, ${self.price_per_km:.2f}/km plus flagfall of "
                f"${self.flagfall:.2f}")

