"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Author: Melandovriertohubi, IT@JCU
Started: 13/10/2015
"""

from kivy.app import App  # Import the App class from Kivy to create the application
from kivy.lang import Builder  # Import Builder to load Kivy language files
from kivy.core.window import Window  # Import Window to control the application window size

__author__ = 'Melandovriertohubi'  # Author information

class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ Build the Kivy app from the KV file. """
        Window.size = (400, 100)  # Set the size of the application window
        self.title = "Square Number"  # Set the title of the application window
        self.root = Builder.load_file('squaring.kv')  # Load the KV layout from the specified file
        return self.root  # Return the root widget for the application

    def handle_calculate(self, value):
        """
        Handle calculation (could be button press or other call) and
        output result to the label widget.
        """
        try:
            result = float(value) ** 2  # Convert input to float and calculate the square
            self.root.ids.output_label.text = str(result)  # Update the output label with the result
        except ValueError:
            pass  # Ignore errors in case of invalid input

# Run the application
SquareNumberApp().run()