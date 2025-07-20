"""START APPLICATION

DEFINE CLASS DynamicLabelsApp INHERITS FROM App

    FUNCTION __init__(self, optional arguments)
        CALL superclass constructor with optional arguments
        INITIALIZE self.names WITH list ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

    FUNCTION build()
        LOAD root layout FROM external .kv file ('dynamic_labels.kv')

        ACCESS BoxLayout component WITH id 'main' FROM root layout
        ASSIGN TO main_layout

        FOR EACH name IN self.names DO
            CREATE new Label WITH:
                text = name
                font_size = 20
                color = (0, 0, 0, 1)         // RGBA: Black
                size_hint_y = None          // Allow fixed vertical size
                height = 40                 // Fixed height for spacing

            ADD the Label widget TO main_layout

        RETURN root layout

END CLASS

IF __name__ == "__main__" THEN
    CREATE an instance of DynamicLabelsApp
    CALL run() method ON the instance

END APPLICATION
"""

# dynamic_labels.py
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Define the list of names (model)
        self.names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

    def build(self):
        # Load the layout from the .kv file
        root = Builder.load_file('dynamic_labels.kv')

        # Access the inner BoxLayout by its id
        main_layout = root.ids.main

        # Dynamically create and add Labels for each name
        for name in self.names:
            label = Label(
                text=name,
                font_size=20,
                color=(0, 0, 0, 1),  # Black text
                size_hint_y=None,   # Allow fixed height
                height=40           # Set height for consistent spacing
            )
            main_layout.add_widget(label)

        return root

if __name__ == '__main__':
    DynamicLabelsApp().run()
