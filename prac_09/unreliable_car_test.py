from prac_09.unreliable_car import UnreliableCar

def test_unreliable_car():
    # Create an UnreliableCar with a reliability of 70%
    unreliable_car = UnreliableCar("Faulty Car", 100, 70)

    # Attempt to drive 50 km
    distance_driven = unreliable_car.drive(50)

    # Print results
    print(f"Distance driven: {distance_driven} km")
    print(unreliable_car)  # Assuming __str__ is implemented in Car for details

# Run the test
if __name__ == "__main__":
    test_unreliable_car()