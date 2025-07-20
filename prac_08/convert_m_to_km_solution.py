"""DEFINE CONSTANT MILES_TO_KM = 1.60934

DEFINE CLASS MilesToKmApp INHERITS FROM App
    DECLARE km_result AS String INITIALIZED TO "0.0"

    FUNCTION build()
        RETURN a new BoxLayout UI

    FUNCTION handle_up_down(delta)
        SET current TO CALL get_current_miles()
        SET new_value TO current + delta
        SET text of input field with id 'input_miles' TO new_value formatted to 1 decimal place
        CALL update_kilometers(new_value)

    FUNCTION get_current_miles()
        SET text TO value from TextInput field with id 'input_miles'
        TRY
            RETURN CONVERT text TO FLOAT
        EXCEPT ValueError
            RETURN 0.0

    FUNCTION handle_text_input(instance, value)
        CALL update_kilometers(value)

    FUNCTION update_kilometers(miles)
        TRY
            SET miles TO CONVERT miles TO FLOAT
            SET km TO miles * MILES_TO_KM
            SET km_result TO STRING FORMAT of km with 4 decimal places
        EXCEPT ValueError
            SET km_result TO "0.0"

END CLASS

IF current file name IS EQUAL TO "__main__"
    CREATE instance of MilesToKmApp
    CALL run() on the instance
"""

import kivy
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

# Conversion factor from miles to kilometers
MILES_TO_KM = 1.60934

class MilesToKmApp(App):
    km_result = StringProperty("0.0")

    def build(self):
        return BoxLayout()

    def handle_up_down(self, delta):
        """Handle incrementing/decrementing the miles value."""
        current = self.get_current_miles()
        new_value = current + delta
        self.root.ids.input_miles.text = f"{new_value:.1f}"
        self.update_kilometers(new_value)

    def get_current_miles(self):
        """Get the current miles value from the TextInput, default to 0.0."""
        text = self.root.ids.input_miles.text
        try:
            return float(text)
        except ValueError:
            return 0.0

    def handle_text_input(self, instance, value):
        """Handle changes to the TextInput value."""
        self.update_kilometers(value)

    def update_kilometers(self, miles):
        """Calculate and update the kilometers result."""
        try:
            miles = float(miles)
            km = miles * MILES_TO_KM
            self.km_result = f"{km:.4f}"
        except ValueError:
            self.km_result = "0.0"

if __name__ == '__main__':
    MilesToKmApp().run()
