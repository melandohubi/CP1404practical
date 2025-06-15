"""BEGIN

    CONSTANT FILENAME = "subject_data.txt"

    FUNCTION main
        SET data TO CALL load_data()
        DISPLAY "Subject Data:"

        FOR EACH subject_info IN data DO
            SET subject TO subject_info[0]
            SET lecturer TO subject_info[1]
            SET students TO subject_info[2]

            DISPLAY subject + " is taught by " + lecturer + " and has " + students + " students"
        END FOR
    END FUNCTION


    FUNCTION load_data
        INITIALIZE subject_list AS empty list

        OPEN FILENAME FOR reading AND STORE AS input_file

        FOR EACH line IN input_file DO
            REMOVE newline character from line
            SPLIT line BY ',' INTO parts

            SET parts[2] TO INTEGER VALUE OF parts[2]

            APPEND parts TO subject_list
        END FOR

        CLOSE input_file

        RETURN subject_list
    END FUNCTION

    CALL main

END
"""

"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print("Subject Data:")
    for subject_info in data:
        subject, lecturer, students = subject_info
        print(f"{subject} is taught by {lecturer} and has {students} students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_list = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])  # Convert student count to int
            subject_list.append(parts)
    return subject_list


main()
