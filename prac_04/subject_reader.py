"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []  # List to store the nested lists

    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Convert the number of students to an integer
        subject_data.append(parts)  # Append the list of parts to the main list

    input_file.close()
    return subject_data  # Return the nested list

def display_subject_details(data):
    """Display details for each subject."""
    for subject in data:
        subject_code = subject[0]
        lecturer = subject[1]
        student_count = subject[2]
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

main()