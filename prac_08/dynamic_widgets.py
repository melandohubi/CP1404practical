from kivy.app import App  # Import the App class from Kivy to create the application
from kivy.lang import Builder  # Import Builder to load Kivy language files
from kivy.uix.label import Label  # Import Label widget to display text

class DynamicLabelsApp(App):
    """ Main program - Kivy app to demo dynamic label creation. """

    def __init__(self, **kwargs):
        """ Construct main app. """
        super().__init__(**kwargs)  # Initialize the parent App class
        # Basic data (model) - list of names
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]  # List of names for label creation

    def build(self):
        """ Build the Kivy GUI. """
        self.title = "Dynamic Labels"  # Set the title of the application window
        self.root = Builder.load_file('dynamic_labels.kv')  # Load the KV layout from the specified file
        self.create_labels()  # Call method to create labels based on the names list
        return self.root  # Return the root widget for the application

    def create_labels(self):
        """ Create labels from data and add them to the GUI. """
        for name in self.names:  # Iterate through each name in the names list
            # Create a label for each name
            temp_label = Label(text=name)  # Create a Label widget with the name as text
            # Add the label to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_label)  # Insert the label into the specified layout

# Run the application
DynamicLabelsApp().run()