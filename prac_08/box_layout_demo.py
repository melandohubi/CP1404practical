"""START APPLICATION

DEFINE CLASS BoxLayoutDemo INHERITS FROM App

    FUNCTION build()
        RETURN a new BoxLayout as the root layout

    FUNCTION handle_greet()
        SET name TO text from input field with id 'input_name'

        IF name.strip() != "" THEN
            // If name is not empty or just spaces
            SET text of label with id 'output_label' TO "Hello " + name
        ELSE
            SET text of label with id 'output_label' TO "Please enter your name."

    FUNCTION handle_clear()
        SET text of input field with id 'input_name' TO empty string ''
        SET text of label with id 'output_label' TO empty string ''

END CLASS

IF __name__ == "__main__" THEN
    CREATE an instance of BoxLayoutDemo
    CALL run() method on the instance

END APPLICATION
"""

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutDemo(App):
    def build(self):
        return BoxLayout()

    def handle_greet(self):
        """Update the label with a greeting based on the input name."""
        name = self.root.ids.input_name.text
        if name.strip():  # Check if the name is not empty
            self.root.ids.output_label.text = f"Hello {name}"
        else:
            self.root.ids.output_label.text = "Please enter your name."

    def handle_clear(self):
        """Reset the TextInput and the output label."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

if __name__ == '__main__':
    BoxLayoutDemo().run()
