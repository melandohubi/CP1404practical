def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():

    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit_result = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit_result:.2f}°F")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius_result = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius_result:.2f}°C")

if __name__ == "__main__":
    main()