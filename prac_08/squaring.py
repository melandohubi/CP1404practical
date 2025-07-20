"""START

FUNCTION handle_calculate(input_text)
    TRY
        SET num TO CONVERT input_text TO FLOAT
        SET result TO num * num
        DISPLAY result FORMATTED TO 2 DECIMAL PLACES ON output_label
    CATCH ValueError
        DISPLAY "Invalid input. Please enter a number." ON output_label
    END TRY
END FUNCTION

FUNCTION build()
    RETURN new BoxLayout
END FUNCTION

RUN SquareNumberApp

END
"""

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SquareNumberApp(App):
    def build(self):
        return BoxLayout()

    def handle_calculate(self, input_text):
        """Handle the square calculation with error checking."""
        try:
            num = float(input_text)
            result = num ** 2
            self.root.ids.output_label.text = f"{result:.2f}"
        except ValueError:
            self.root.ids.output_label.text = "Invalid input. Please enter a number."

if __name__ == '__main__':
    SquareNumberApp().run()
