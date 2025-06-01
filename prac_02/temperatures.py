"""FUNCTION celsius_to_fahrenheit(celsius)
    RETURN (celsius * 9 / 5) + 32
END FUNCTION


FUNCTION fahrenheit_to_celsius(fahrenheit)
    RETURN (fahrenheit - 32) * 5 / 9
END FUNCTION


FUNCTION main()
    DISPLAY "Enter temperature in Celsius: "
    READ input_value
    CONVERT input_value TO FLOAT → celsius

    fahrenheit_result ← CALL celsius_to_fahrenheit(celsius)
    DISPLAY celsius + "°C is equal to " + FORMAT fahrenheit_result TO 2 DECIMAL PLACES + "°F"

    DISPLAY "Enter temperature in Fahrenheit: "
    READ input_value
    CONVERT input_value TO FLOAT → fahrenheit

    celsius_result ← CALL fahrenheit_to_celsius(fahrenheit)
    DISPLAY fahrenheit + "°F is equal to " + FORMAT celsius_result TO 2 DECIMAL PLACES + "°C"
END FUNCTION


IF program is being run directly THEN
    CALL main()
END IF
"""

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
