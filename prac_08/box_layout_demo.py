from kivy.app import App  # Import the App class from Kivy to create the application
from kivy.lang import Builder  # Import Builder to load Kivy language files

class BoxLayoutDemo(App):
    """
    BoxLayoutDemo is a Kivy application that demonstrates the use of BoxLayout
    for a simple user interface that greets the user.
    """

    def build(self):
        """
        Build the Kivy app from the KV file.
        Sets the application title and loads the UI from a .kv file.
        """
        self.title = "Box Layout Demo"  # Set the title of the application window
        self.root = Builder.load_file('box_layout.kv')  # Load the KV layout from the specified file
        return self.root  # Return the root widget for the application

    def handle_greet(self, *args):
        """
        Handle the greeting action.
        Retrieves the name from the input field and updates the output label.
        """
        input_name = self.root.ids.input_name.text  # Get the text from the input field
        self.root.ids.output_label.text = f"Hello {input_name}"  # Update the label with the greeting

    def handle_clear(self, *args):
        """
        Handle the clear action.
        Resets the input field and the output label to their default states.
        """
        self.root.ids.input_name.text = ''  # Clear the input field
        self.root.ids.output_label.text = 'Enter your name'  # Reset the label text

# Run the application
BoxLayoutDemo().run()