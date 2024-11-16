"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Author: Melando Vrierto Hubi, IT@JCU
Date: 06/10/2015
"""

from kivy.app import App  # Import the App class from the kivy library
from kivy.lang import Builder  # Import Builder to load Kivy language files
from kivy.properties import StringProperty  # Import StringProperty for dynamic text updates

__author__ = 'Melando Vrierto Hubi'  # Author information

# Constant to convert miles to kilometers
MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """
    MilesConverterApp is a Kivy application that provides a graphical user
    interface for converting miles to kilometers.
    """

    output_text = StringProperty()  # Property to hold the output text

    def build(self):
        """
        Build the Kivy app from the KV file.
        Sets the title of the application and loads the UI from a .kv file.
        """
        self.title = "Convert Miles to Kilometres"  # Set the window title
        self.root = Builder.load_file('convert_m_km_solution.kv')  # Load the KV layout
        return self.root  # Return the root widget

    def handle_calculate(self):
        """
        Handle the calculation of kilometers from miles.
        Updates the output label with the result.
        """
        value = self.get_validated_miles()  # Get the validated mile input
        result = value * MILES_TO_KM  # Convert miles to kilometers
        self.root.ids.output_label.text = f"{result:.3f}"  # Format and display result

    def handle_increment(self, change):
        """
        Handle the increment or decrement of miles via button press.
        Updates the input field and recalculates the result.

        :param change: Amount to change the mile input (positive or negative)
        """
        value = self.get_validated_miles() + change  # Update the mile value
        self.root.ids.input_miles.text = str(value)  # Update the input field
        self.handle_calculate()  # Recalculate the kilometers

    def get_validated_miles(self):
        """
        Get the miles input from the text entry widget and convert it to float.
        Returns 0.0 if the input is invalid.

        :return: float version of input if valid, otherwise 0.0
        """
        try:
            value = float(self.root.ids.input_miles.text)  # Attempt to convert input to float
            return value  # Return the valid float value
        except ValueError:
            return 0.0  # Return 0.0 if conversion fails


# Run the application
MilesConverterApp().run()