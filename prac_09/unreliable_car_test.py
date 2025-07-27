"""BEGIN

    // Test UnreliableCar at 100% reliability
    always_car ← NEW UnreliableCar("AlwaysReliable", 100, 100)
    PRINT always_car.__str__()
    result ← always_car.drive(10)
    PRINT "Should always drive 10km:", result
    PRINT "Fuel left:", always_car.fuel

    // Test UnreliableCar at 0% reliability
    never_car ← NEW UnreliableCar("NeverReliable", 100, 0)
    PRINT never_car.__str__()
    result ← never_car.drive(10)
    PRINT "Should never drive (always 0):", result
    PRINT "Fuel left:", never_car.fuel

    // Test UnreliableCar at 50% reliability over 100 iterations
    half_car ← NEW UnreliableCar("HalfReliable", 100, 50)
    successful_drives ← 0
    attempts ← 100
    FOR i FROM 1 TO attempts DO
        distance_driven ← half_car.drive(1)
        IF distance_driven > 0 THEN
            successful_drives ← successful_drives + 1
    END FOR
    PRINT "Tried", attempts, "times. Drives succeeded:", successful_drives

END
"""

# unreliable_car_test.py

from unreliable_car import UnreliableCar

def main():
    # Examples with various reliability
    print("Testing UnreliableCar with 100% reliability:")
    always_drives = UnreliableCar("AlwaysReliable", 100, 100)
    print(always_drives)
    print("Should always drive 10km:", always_drives.drive(10))
    print("Fuel left:", always_drives.fuel)
    print()

    print("Testing UnreliableCar with 0% reliability:")
    never_drives = UnreliableCar("NeverReliable", 100, 0)
    print(never_drives)
    print("Should never drive (always 0):", never_drives.drive(10))
    print("Fuel left:", never_drives.fuel)
    print()

    print("Testing UnreliableCar with 50% reliability over multiple trials:")
    mid_reliable = UnreliableCar("HalfReliable", 100, 50)
    successful_drives = 0
    attempts = 100
    distance = 1
    for _ in range(attempts):
        if mid_reliable.drive(distance) > 0:
            successful_drives += 1
    print(f"Tried to drive {distance}km {attempts} times.")
    print(f"Successfully drove {successful_drives} times. (Expected ~50 drives)")
    print("Fuel left:", mid_reliable.fuel)
    print()

    # You can tune these numbers as you like!

if __name__ == "__main__":
    main()
