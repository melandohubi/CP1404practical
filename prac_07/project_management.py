"""

CLASS Project
    FUNCTION __init__(name, start_date, priority, cost_estimate, completion)
        SET self.name = name
        SET self.start_date = start_date  # as a date object
        SET self.priority = priority
        SET self.cost_estimate = cost_estimate
        SET self.completion = completion
    END FUNCTION

    FUNCTION is_complete()
        RETURN self.completion == 100
    END FUNCTION

    FUNCTION __lt__(other)
        RETURN self.priority < other.priority
    END FUNCTION

    FUNCTION __str__()
        RETURN formatted string including name, start_date, priority, cost_estimate, and completion
    END FUNCTION
END CLASS

FUNCTION load_projects(filename)
    CREATE empty list projects
    OPEN file with name = filename FOR reading
    SKIP first line (header)
    FOR each line IN file
        SPLIT line by tab into name, date_str, priority_str, cost_str, completion_str
        CONVERT date_str to date object using format "%d/%m/%Y"
        CONVERT priority_str to integer
        CONVERT cost_str to float
        CONVERT completion_str to integer
        CREATE new Project object with parsed values
        ADD project to projects list
    END FOR
    RETURN projects
END FUNCTION

FUNCTION save_projects(filename, projects)
    OPEN file with name = filename FOR writing
    WRITE header line to file
    FOR each project IN projects
        FORMAT project attributes into tab-separated string
        WRITE line to file
    END FOR
END FUNCTION

FUNCTION display_projects(projects)
    SET incomplete_projects = empty list
    SET complete_projects = empty list
    FOR each project IN projects
        IF project.is_complete() == False THEN
            ADD project to incomplete_projects
        ELSE
            ADD project to complete_projects
        END IF
    END FOR

    SORT incomplete_projects BY priority (using __lt__)
    SORT complete_projects BY priority

    PRINT "Incomplete projects:"
    FOR each project IN incomplete_projects
        PRINT project
    END FOR

    PRINT "Completed projects:"
    FOR each project IN complete_projects
        PRINT project
    END FOR
END FUNCTION

FUNCTION filter_projects_by_date(projects)
    PROMPT user for date input in format dd/mm/yyyy
    CONVERT input to date object as filter_date
    CREATE empty list filtered_projects
    FOR each project IN projects
        IF project.start_date >= filter_date THEN
            ADD project to filtered_projects
        END IF
    END FOR
    SORT filtered_projects BY start_date
    FOR each project IN filtered_projects
        PRINT project
    END FOR
END FUNCTION

FUNCTION add_new_project()
    PROMPT user for name
    PROMPT user for start_date (dd/mm/yyyy) and convert to date
    PROMPT user for priority, cost_estimate, and completion
    RETURN new Project object with these inputs
END FUNCTION

FUNCTION update_project(projects)
    FOR index FROM 0 TO length of projects - 1
        PRINT index and project
    END FOR
    PROMPT user for index choice
    SET selected_project = projects[index]
    PRINT selected_project
    PROMPT user for new_completion (optional)
    IF new_completion != empty THEN
        SET selected_project.completion = int(new_completion)
    END IF
    PROMPT user for new_priority (optional)
    IF new_priority != empty THEN
        SET selected_project.priority = int(new_priority)
    END IF
END FUNCTION

FUNCTION main()
    SET FILENAME = "projects.txt"
    PRINT welcome message
    SET projects = load_projects(FILENAME)
    PRINT how many projects loaded

    WHILE True
        DISPLAY menu
        PROMPT user for choice

        IF choice == "l" THEN
            PROMPT for filename
            SET projects = load_projects(filename)
        ELIF choice == "s" THEN
            PROMPT for filename
            CALL save_projects(filename, projects)
        ELIF choice == "d" THEN
            CALL display_projects(projects)
        ELIF choice == "f" THEN
            CALL filter_projects_by_date(projects)
        ELIF choice == "a" THEN
            SET new_project = add_new_project()
            ADD new_project to projects
        ELIF choice == "u" THEN
            CALL update_project(projects)
        ELIF choice == "q" THEN
            PROMPT user if they want to save to default file
            IF yes THEN
                CALL save_projects(FILENAME, projects)
            END IF
            PRINT exit message
            BREAK
        ELSE
            PRINT "Invalid choice"
        END IF
    END WHILE
END FUNCTION

CALL main()"""

# Project Management Program
# Estimated time: 3–4 hours

import datetime
from project import Project

FILENAME = "projects.txt"

def load_projects(filename):
    """Load project data from a file and return a list of Project instances."""
    projects = []
    with open(filename, "r") as in_file:
        next(in_file)  # Skip header
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion))
    return projects

def save_projects(filename, projects):
    """Save a list of Project instances to a file."""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for p in projects:
            out_file.write(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t{p.cost_estimate}\t{p.completion}\n")

def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for p in sorted(incomplete):
        print(f"  {p}")

    print("Completed projects:")
    for p in sorted(complete):
        print(f"  {p}")

def filter_projects_by_date(projects):
    """Prompt for a date and show projects starting on or after that date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        date_filter = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered = [p for p in projects if p.start_date >= date_filter]
        for p in sorted(filtered, key=lambda x: x.start_date):
            print(p)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")

def add_new_project():
    """Prompt user to enter details for a new project and return the new Project instance."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion = int(input("Percent complete: "))
        return Project(name, start_date, priority, cost_estimate, completion)
    except ValueError:
        print("Invalid input. Please try again.")
        return None

def update_project(projects):
    """Display projects with index, allow user to update selected project's completion and/or priority."""
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)
        new_completion = input("New Percentage (leave blank to skip): ")
        if new_completion:
            project.completion = int(new_completion)
        new_priority = input("New Priority (leave blank to skip): ")
        if new_priority:
            project.priority = int(new_priority)
    except (IndexError, ValueError):
        print("Invalid selection.")

def main():
    """Main function to manage the project tracking system."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    MENU = """
- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
>>> """

    while True:
        choice = input(MENU).lower()
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            project = add_new_project()
            if project:
                projects.append(project)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            confirm = input(f"Would you like to save to {FILENAME}? ").lower()
            if confirm in ["y", "yes"]:
                save_projects(FILENAME, projects)
            print("Thank you for using Pythonic Project Management.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
