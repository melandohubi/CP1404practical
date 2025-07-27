"""BEGIN

    PRINT "Let's drive!"

    // Create list of taxis
    taxis ← [ NEW Taxi("Prius", 100),
              NEW SilverServiceTaxi("Limo", 100, 2),
              NEW SilverServiceTaxi("Hummer", 200, 4) ]

    bill ← 0.0
    current_taxi ← None

    REPEAT
        PRINT "q)uit, c)hoose taxi, d)rive"
        choice ← INPUT(">>> ")
        choice ← TO_LOWERCASE(choice)

        IF choice == 'q' THEN
            BREAK LOOP

        ELSE IF choice == 'c' THEN
            // Show taxis
            PRINT "Taxis available:"
            FOR i FROM 0 TO LENGTH(taxis) - 1 DO
                PRINT i, "-", taxis[i].ToString()
            END FOR

            taxi_choice_input ← INPUT("Choose taxi: ")
            TRY
                taxi_choice ← TO_INTEGER(taxi_choice_input)
                IF taxi_choice >= 0 AND taxi_choice < LENGTH(taxis) THEN
                    CALL taxis[taxi_choice].start_fare()
                    current_taxi ← taxis[taxi_choice]
                ELSE
                    PRINT "Invalid taxi choice"
                END IF
            CATCH invalid input
                PRINT "Invalid taxi choice"
            END TRY

        ELSE IF choice == 'd' THEN
            IF current_taxi == None THEN
                PRINT "You need to choose a taxi before you can drive"
                PRINT "Bill to date: $" + FORMAT(bill, 2)
            ELSE
                ASK_DISTANCE:
                REPEAT
                    distance_input ← INPUT("Drive how far? ")
                    TRY
                        distance ← TO_FLOAT(distance_input)
                        IF distance < 0 THEN
                            PRINT "Distance must be >= 0"
                            CONTINUE REPEAT
                        END IF
                        CALL current_taxi.drive(distance)
                        trip_cost ← current_taxi.get_fare()
                        PRINT "Your", current_taxi.name, "trip cost you $", FORMAT(trip_cost, 2)
                        bill ← bill + trip_cost
                        PRINT "Bill to date: $", FORMAT(bill, 2)
                        BREAK REPEAT
                    CATCH invalid input
                        PRINT "Invalid input; enter a number."
                    END TRY
                END REPEAT

        ELSE
            PRINT "Invalid option"
            PRINT "Bill to date: $", FORMAT(bill, 2)
        END IF

    END REPEAT

    PRINT "Total trip cost: $", FORMAT(bill, 2)
    PRINT "Taxis are now:"
    FOR i FROM 0 TO LENGTH(taxis) - 1 DO
        PRINT i, "-", taxis[i].ToString()
    END FOR

END
"""


"""Taxi Simulator - Polymorphic Taxi Fare Calculation."""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    bill = 0.0
    current_taxi = None

    while True:
        print(MENU)
        choice = input(">>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                trip_cost = drive_taxi(current_taxi)
                bill += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            print(f"Bill to date: ${bill:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill:.2f}")

    # End of session
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def choose_taxi(taxis):
    print("Taxis available:")
    for idx, taxi in enumerate(taxis):
        print(f"{idx} - {taxi}")
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            # Restart meter for the selected taxi
            taxis[taxi_choice].start_fare()
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None

def drive_taxi(taxi):
    while True:
        try:
            distance = float(input("Drive how far? "))
            if distance < 0:
                print("Distance must be >= 0")
                continue
            taxi.drive(distance)
            fare = taxi.get_fare()
            return fare
        except ValueError:
            print("Invalid input; enter a number.")

def display_taxis(taxis):
    for idx, taxi in enumerate(taxis):
        print(f"{idx} - {taxi}")

if __name__ == "__main__":
    main()
