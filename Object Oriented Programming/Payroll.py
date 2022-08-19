# Make a payroll system where there will be two classes, Programmer and Assistant.

# the 'programmer' class will have name, age and programming_languages properties and the 'assistant' class will have name, age and bilingual properties in the constructor function.

# declare a function named calculate_payroll() which takes a list of instances of the assistant and employee classes and prints the monthly salary of each worker and the total amount that gets paid each month


class Programmer:

    # Add the class attributes

    def __init__(self, name, age, programming_languages):
        self.name = name
        self.age = age
        self.programming_languages = programming_languages
        self.salary = 240000  # annual salary
        self.monthlyBonus = 2000


class Assistant:

    # Add the class attributes

    def __init__(self, name, age, bilingual):
        self.name = name
        self.age = age
        self.bilingual = bilingual
        self.salary = 180000  # annual salary
        self.monthlyBonus = 1000

# Program ==================================================================

# Function that prints the monthly salary of each worker
# and the total amount that the startup owner has to pay per month


def calculate_payroll(employees):

    total = 0

    print("\n========= Welcome to our Payroll System =========\n")

    # Iterate over the list of instances to calculate
    # and display the monthly salary of each employee,
    # and add the monthly salary to the total for this month
    for employee in employees:
        salary = round(employee.salary / 12, 2) + employee.monthlyBonus
        print(employee.name.capitalize() + "'s salary is: $" + str(salary))
        total += salary

    # Display the total
    print("\nThe total payroll this month will be: $", total)


# Instances (employees)
jack = Programmer("Jack", 45, ["Python", "Java"])
isabel = Programmer("Isabel", 25, ["JavaScript"])
nora = Assistant("Nora", 23, True)

# List of instances
employees = [jack, isabel, nora]

# Function call - Passing the list of instances as argument
calculate_payroll(employees)
