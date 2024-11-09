import csv
from datetime import datetime


class Project:
    """Represent a project object."""

    def __init__(self, name="", start_date="", priority=0, cost=0.0, completion=0):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y") if start_date else None
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost:,.2f}, completion: {self.completion}%"

    def is_complete(self):
        """Check if the project is complete."""
        return self.completion >= 100


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, start_date, priority, cost, completion = row
                project = Project(name, start_date, int(priority), float(cost), int(completion))
                projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"No existing project file found at {filename}.")
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'), project.priority,
                             project.cost, project.completion])
    print(f"Saved {len(projects)} projects to {filename}.")


def display_projects(projects):
    """Display all projects."""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    completed_projects = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date_str):
    """Filter and display projects that start after the given date."""
    filter_date = datetime.strptime(date_str, "%d/%m/%Y")
    filtered_projects = [p for p in projects if p.start_date > filter_date]

    print(f"Projects that start after {date_str}:")
    for project in filtered_projects:
        print(f"  {project}")


def add_project(projects):
    """Add a new project interactively."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost, completion)
    projects.append(new_project)
    print(f"Added new project: {new_project}")


def update_project(projects):
    """Update an existing project's details."""
    display_projects(projects)

    choice = int(input("Project choice: "))

    if choice < 0 or choice >= len(projects):
        print("Invalid choice.")
        return

    selected_project = projects[choice]

    print(selected_project)

    new_completion = int(input("New Percentage: "))
    new_priority = input("New Priority (leave blank to keep current): ")

    selected_project.completion = new_completion
    if new_priority.strip():
        selected_project.priority = int(new_priority)


def main():
    """Main function to run the program."""

    filename = "projects.txt"

    # Load existing projects
    projects = load_projects(filename)

    while True:
        # Display menu options
        print("\nWelcome to Pythonic Project Management")
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            projects = load_projects(filename)

        elif choice == 's':
            save_projects(filename, projects)

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)

        elif choice == 'a':
            add_project(projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            save_choice = input("Would you like to save to {}? ".format(filename)).lower()
            if save_choice in ['yes', 'y']:
                save_projects(filename, projects)
            break


if __name__ == "__main__":
    main()