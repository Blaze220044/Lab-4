class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, target_age):
        result = [emp for emp in self.employees if emp.age == target_age]
        return result

    def search_by_name(self, target_name):
        result = [emp for emp in self.employees if emp.name == target_name]
        return result

    def search_by_salary(self, condition, target_salary):
        if condition == '>':
            result = [emp for emp in self.employees if emp.salary > target_salary]
        elif condition == '<':
            result = [emp for emp in self.employees if emp.salary < target_salary]
        elif condition == '<=':
            result = [emp for emp in self.employees if emp.salary <= target_salary]
        elif condition == '>=':
            result = [emp for emp in self.employees if emp.salary >= target_salary]
        else:
            result = []
        return result

    def display_result(self, result):
        if not result:
            print("No matching records found.")
        else:
            print("Employee ID\tName\tAge\tSalary")
            for emp in result:
                print(f"{emp.emp_id}\t{emp.name}\t{emp.age}\t{emp.salary}")

def main():
    db = EmployeeDatabase()

    emp1 = Employee("161E90", "Raman", 41, 56000)
    emp2 = Employee("161F91", "Himadri", 38, 67500)
    emp3 = Employee("161F99", "Jaya", 51, 82100)
    emp4 = Employee("171E20", "Tejas", 30, 55000)
    emp5 = Employee("171G30", "Ajay", 45, 44000)

    db.add_employee(emp1)
    db.add_employee(emp2)
    db.add_employee(emp3)
    db.add_employee(emp4)
    db.add_employee(emp5)

    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        target_age = int(input("Enter the age to search: "))
        result = db.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter the name to search: ")
        result = db.search_by_name(target_name)
    elif choice == 3:
        condition = input("Enter the salary condition (> < <= >=): ")
        target_salary = float(input("Enter the target salary: "))
        result = db.search_by_salary(condition, target_salary)
    else:
        print("Invalid choice")

    db.display_result(result)

if __name__ == "__main__":
    main()
