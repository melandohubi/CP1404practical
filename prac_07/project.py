"""Class Project
    Method __init__(name, start_date, priority, cost_estimate, completion)
        Set this.name = name
        Set this.start_date = start_date
        Set this.priority = priority
        Set this.cost_estimate = cost_estimate
        Set this.completion = completion

    Method __str__()
        Return string concatenation of:
            this.name + ", start: " + formatted this.start_date +
            ", priority " + this.priority +
            ", estimate: $" + formatted this.cost_estimate +
            ", completion: " + this.completion + "%"

    Method __lt__(other)
        Return (this.priority < other.priority)

    Method is_complete()
        If this.completion == 100 Then
            Return True
        Else
            Return False
"""

# Class representing a project with name, start date, priority, cost, and completion status
import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """
        Initialize a Project instance.

        :param name: str - The name of the project
        :param start_date: datetime.date - The start date of the project
        :param priority: int - The project's priority (lower is higher priority)
        :param cost_estimate: float - The estimated cost of the project
        :param completion: int - The completion percentage (0-100)
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """Return a formatted string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Define less-than for sorting by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is 100% complete, otherwise False."""
        return self.completion == 100
