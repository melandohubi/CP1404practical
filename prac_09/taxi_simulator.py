class Taxi:
    def __init__(self, name, fuel):
        """Initializes a Taxi instance with a name and fuel amount.

        Args:
            name (str): The name of the taxi.
            fuel (float): The amount of fuel in the taxi.
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0  # Tracks the distance driven
        self.current_fare = 1.23  # Example fare per km

    def drive(self, distance):
        """Drives the taxi a certain distance, adjusting for fuel limits.

        Args:
            distance (float): The distance to drive.

        Returns:
            float: The cost of the trip based on distance driven.
        """
        if distance > self.fuel:
            distance = self.fuel  # Drive only as far as the fuel allows
        self.odometer += distance  # Update the odometer
        self.fuel -= distance  # Decrease the fuel by the distance driven
        return distance * self.current_fare  # Calculate and return the fare

    def __str__(self):
        """Returns a string representation of the taxi's current state.

        Returns:
            str: A string describing the taxi's name, fuel, odometer, and fare.
        """
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, {self.current_fare}/km"


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, flagfall):
        """Initializes a SilverServiceTaxi instance with a name, fuel, and flagfall.

        Args:
            name (str): The name of the taxi.
            fuel (float): The amount of fuel in the taxi.
            flagfall (float): The initial charge for the taxi service.
        """
        super().__init__(name, fuel)  # Call the parent class constructor
        self.flagfall = flagfall  # Set the flagfall charge
        self.current_fare = 2.46  # Example fare per km for Silver Service

    def drive(self, distance):
        """Drives the taxi a certain distance and adds the flagfall to the cost.

        Args:
            distance (float): The distance to drive.

        Returns:
            float: The total cost of the trip including flagfall.
        """
        cost = super().drive(distance)  # Get the cost from the parent class
        return cost + self.flagfall  # Add flagfall to the cost

    def __str__(self):
        """Returns a string representation of the SilverServiceTaxi's current state.

        Returns:
            str: A string describing the taxi's name, fuel, odometer, fare, and flagfall.
        """
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, {self.current_fare}/km plus flagfall of {self.flagfall}"


def main():
    """Main function to run the taxi simulation.

    It allows users to choose a taxi, drive it a certain distance, and calculates the total bill.
    """
    # Create a list of available taxis
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 4.50),
        SilverServiceTaxi("Hummer", 200, 4.50)
    ]

    current_taxi = None  # Variable to store the currently selected taxi
    total_bill = 0  # Variable to track the total bill

    while True:
        print("Let's drive!")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()  # Get user input

        if choice == 'q':
            # If the user chooses to quit, display the total bill and available taxis
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break
        elif choice == 'c':
            # If the user chooses to select a taxi, display available taxis
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = int(input("Choose taxi: "))  # Get taxi choice from user
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]  # Set the current taxi
            else:
                print("Invalid taxi choice")  # Handle invalid choice
        elif choice == 'd':
            # If the user chooses to drive, check if a taxi is selected
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))  # Get distance to drive
                trip_cost = current_taxi.drive(distance)  # Calculate trip cost
                total_bill += trip_cost  # Update total bill
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                print(f"Bill to date: ${total_bill:.2f}")
        else:
            print("Invalid option")  # Handle invalid option


if __name__ == "__main__":
    main()  # Run the main function when the script is executed