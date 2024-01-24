class Employee:
    def __init__(self, name, employee_id, position, salary):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary updated to ${new_salary}")


if __name__ == "__main__":
    
    emp1 = Employee("John Doe", 101, "Software Engineer", 60000)
    emp2 = Employee("Jane Smith", 102, "Data Scientist", 70000)

    print("Initial Employee Details:")
    emp1.display_details()
    print("\n")
    emp2.display_details()
    print("\n")

    emp1.update_salary(65000)

   
    print("\nEmployee Details after Salary Update:")
    emp1.display_details()
    print("\n")
    emp2.display_details()
