# Taxi Simulation

## Overview

This project simulates a taxi service with different types of taxis, including standard and silver service taxis. It allows users to choose a taxi, drive it a certain distance, and calculate the total fare.

## Features

- **Taxi Types**: 
  - Standard Taxi
  - Silver Service Taxi (includes a flagfall and a fanciness multiplier)
  - Unreliable Car (drives based on a reliability factor)

- **User Interaction**: 
  - Users can choose a taxi, drive it a specified distance, and view the accumulated fare.
  
- **Fare Calculation**: 
  - The fare is calculated based on distance driven and the type of taxi selected.

## Installation

To run this project, ensure you have Python installed. Clone the repository and run the main script.

```bash
git clone <repository_url>
cd taxi_simulation
python main.py
```

## Usage

1. **Choose a Taxi**: The user can select from available taxis.
2. **Drive**: Input the distance to drive.
3. **Quit**: The user can exit the simulation and view the total fare.

## Classes

### 1. `Car`
The base class for all cars.

### 2. `Taxi`
Inherits from `Car` and adds functionality for fare calculation.

### 3. `SilverServiceTaxi`
Inherits from `Taxi` and includes a flagfall charge and a fanciness multiplier.

### 4. `UnreliableCar`
Inherits from `Car` and has a reliability factor that determines if the car can drive a given distance.

## Testing

The project includes unit tests for the `SilverServiceTaxi` and `UnreliableCar` classes. Run the test scripts to verify functionality.

```bash
python silver_service_taxi_test.py
python unreliable_car_test.py
```

## Example Output

When you run the main script, you will see prompts like:

```
Let's drive!
q)uit, c)hoose taxi, d)rive
>>> c
Taxis available:
0 - Prius, fuel=100, odometer=0, 1.23/km
1 - Limo, fuel=100, odometer=0, 2.46/km plus flagfall of 4.50
...
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests for improvements!