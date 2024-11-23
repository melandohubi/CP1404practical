from prac_09.silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    # Create a SilverServiceTaxi with fanciness of 2
    taxi = SilverServiceTaxi("Luxury Taxi", 100, 1.23, 2)

    # Start a fare and drive 18 km
    taxi.start_fare()
    taxi.drive(18)

    # Calculate expected fare: (1.23 * 2 * 18) + 4.50
    expected_fare = (1.23 * 2 * 18) + SilverServiceTaxi.flagfall
    actual_fare = taxi.get_fare()

    # Print results
    print(taxi)  # Print taxi details
    print("Expected Fare:", expected_fare)
    print("Actual Fare:", actual_fare)

    # Assert to check if the actual fare matches expected fare
    assert actual_fare == expected_fare, f"Expected {expected_fare}, but got {actual_fare}"

# Run tests
if __name__ == "__main__":
    test_silver_service_taxi()