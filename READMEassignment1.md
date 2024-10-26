Program Description

Travel Tracker is a Python-based interactive application designed to assist users in managing their travel destinations. The program enables users to create and maintain a comprehensive list of places they wish to visit and those they have already visited. Key functionalities include:

1. Display Places: 
   - Users can view a formatted list of all tracked places. 
   - The list is dynamically sorted first by visited status (unvisited places are highlighted) and then by priority (higher priority numbers come first).

2. Recommend Place: 
   - The program randomly suggests an unvisited place from the list.
   - If no unvisited places are available, it notifies the user that there are no places left to visit.

3. Add New Place: 
   - Users can input new travel destinations, specifying the name, country, and priority level of the place.
   - The program ensures valid inputs, rejecting blank names or countries and requiring priority to be a positive integer.

4. Mark Place as Visited: 
   - Users can change the status of a place to "visited," preventing it from being marked unvisited later.
   - The program includes error handling to ensure the selected place exists and has not already been visited.

5. Save to CSV: 
   - Upon exiting, the program saves all tracked places to a `places.csv` file, ensuring data persistence for future sessions.
   - The file format adheres to CSV standards, making it easy to read or edit outside the program.

The Travel Tracker program is structured around functions to enhance modularity, readability, and maintainability. It incorporates robust error-checking mechanisms to handle invalid user inputs gracefully, ensuring a smooth user experience.

How to Run the Program

1. System Requirements:
   - Ensure you have **Python 3** installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

2. Download the Source Code:
   - Copy the provided Python code into a text editor or an Integrated Development Environment (IDE) such as **PyCharm**, Visual Studio Code, or any other Python-compatible IDE.

3. Save the File:
   - Save the code in a file named `travel_tracker.py`.

4. Prepare the CSV File:
   - Create a CSV file named `places.csv` in the same directory as `travel_tracker.py`. This file can be initially empty, as the program will populate it with default data if it does not exist.

5. Run the Program:
   - Open a terminal or command prompt.
   - Navigate to the directory where `travel_tracker.py` is saved using the `cd` command. For example:
     ```bash
     cd path/to/directory
     ```
   - Execute the program by entering the following command:
     ```bash
     python travel_tracker.py
     ```

6. Interact with the Program:
   - Follow the on-screen menu to navigate through the available options:
     - D: Display all places.
     - R: Recommend a random place.
     - A: Add a new place.
     - M: Mark a place as visited.
     - Q: Quit the program.

7. Exiting the Program:
   - When you select Q, the program will save all changes to `places.csv`. 
   - A confirmation message will display the number of places saved, and you will receive a friendly farewell message.

