from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from operator import itemgetter

# Sample dictionary of names to scores
name_to_score = {
    'Derek': 7,
    'Xavier': 80,
    'Bob': 612,
    'Chantanelle': 9
}


class KivyDemo(App):
    """Kivy program to demo some basic interactive functionality."""
    status_text = StringProperty("Hello. Click the buttons :)")

    def __init__(self, **kwargs):
        """Construct main Kivy app."""
        super().__init__(**kwargs)
        self.counter = 0
        self.names = list(name_to_score.keys())
        self.scores = list(name_to_score.values())

    def build(self):
        """Construct the dynamic widgets."""
        self.title = "Hello world!"
        self.root = Builder.load_file('kivy_layout.kv')
        self.populate_buttons()
        return self.root

    def populate_buttons(self):
        """Populate buttons with names from the dictionary."""
        for name in self.names:
            button = Button(text=name)
            button.bind(on_press=self.handle_name_button)
            self.root.ids.names_box.add_widget(button)

        # Display sorted scores in the console
        self.display_scores()

    def handle_name_button(self, instance):
        """Handle presses on the name button to greet people."""
        print("Hello", instance.text)

    def handle_press(self, amount):
        """Handle presses on the up/down buttons to change counter."""
        self.counter += amount
        self.status_text = f"The count is: {self.counter}"

    def display_scores(self):
        """Display the names and scores in sorted order."""
        # Calculate maximum width for names and scores
        name_width = max(len(name) for name in name_to_score.keys())
        score_width = max(len(str(score)) for score in name_to_score.values())

        # Sort and print the items in the dictionary
        sorted_items = sorted(name_to_score.items(), key=itemgetter(1), reverse=True)

        # Print scores to console (or you can display them in the app if needed)
        print("\nSorted Scores:")
        for name, score in sorted_items:
            print(f"{name:<{name_width}} = {score:{score_width}}")


# Create an instance of the KivyDemo class and start the App running
if __name__ == "__main__":
    KivyDemo().run()