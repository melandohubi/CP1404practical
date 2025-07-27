"""BEGIN

    // Create a SilverServiceTaxi named "Hummer" with 200 fuel and fanciness 4
    taxi ← NEW SilverServiceTaxi("Hummer", 200, 4)

    ASSERT taxi.price_per_km == 4.92

    ASSERT taxi.get_fare() == 4.50        // 0km, should be flagfall only

    // Create another SilverServiceTaxi for the 18km example
    limo ← NEW SilverServiceTaxi("Stretch", 100, 2)
    distance_driven ← limo.drive(18)
    ASSERT distance_driven == 18           // assuming enough fuel for 18 km

    fare ← limo.get_fare()
    ASSERT ABS(fare - 48.78) < 0.01        // 18 × 2.46 + 4.50 = 48.78

    // Fare should reset after start_fare()
    CALL limo.start_fare()
    ASSERT limo.get_fare() == 4.50

END
"""

# silver_service_taxi_test.py

from silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi: name, fuel, fanciness
    taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(taxi)  # Should show $4.92/km plus flagfall of $4.50

    # Test the correct price_per_km
    assert taxi.price_per_km == 4.92, "price_per_km should be 4.92 for Hummer with fanciness 4"

    # Test fare for 0 km
    assert taxi.get_fare() == 4.50, "fare with 0km should just be flagfall"

    # New test: 18 km trip, fanciness 2 -> price_per_km 2.46
    limo = SilverServiceTaxi("Stretch", 100, 2)
    limo.drive(18)
    print(limo)  # Should show 18km on current fare, $2.46/km plus flagfall of $4.50
    fare_18km = limo.get_fare()
    print(f"18km trip fare: ${fare_18km}")
    assert abs(fare_18km - 48.78) < 0.01, "18km trip in SilverServiceTaxi(fanciness 2) should be ~$48.78"

    # Extra: test fare resets with new fare
    limo.start_fare()  # Should reset to 0 km
    assert limo.get_fare() == 4.50, "After start_fare fare should equal flagfall"

    print("All SilverServiceTaxi tests passed.")

if __name__ == "__main__":
    main()
