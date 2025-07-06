import csv

class Employee:
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary
    
    def to_dict(self):
        return {
            'Employee ID': self.empid,
            'Name': self.name,
            'Address': self.address,
            'Contact Number': self.contact_number,
            'Spouse Name': self.spouse_name,
            'Number of Children': self.number_of_child,
            'Salary': self.salary
        }

def input_employee():
    print("\nEnter Employee Details:")
    empid = input("Employee ID: ")
    name = input("Name: ")
    address = input("Address: ")
    contact_number = input("Contact Number: ")
    spouse_name = input("Spouse Name: ")
    number_of_child = input("Number of Children: ")
    salary = input("Salary: ")
    return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)

def save_to_csv(employees, filename="employees.csv"):
    try:
        with open(filename, 'w', newline='') as file:
            fieldnames = ['Employee ID', 'Name', 'Address', 'Contact Number', 
                         'Spouse Name', 'Number of Children', 'Salary']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for employee in employees:
                writer.writerow(employee.to_dict())
        print(f"\nData successfully saved to {filename}")
    except Exception as e:
        print(f"\nError occurred while saving to file: {e}")

def display_employees(filename="employees.csv"):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            print("\nList of Employees:")
            print("-" * 80)
            for row in reader:
                print(f"Employee ID: {row['Employee ID']}")
                print(f"Name: {row['Name']}")
                print(f"Address: {row['Address']}")
                print(f"Contact Number: {row['Contact Number']}")
                print(f"Spouse Name: {row['Spouse Name']}")
                print(f"Number of Children: {row['Number of Children']}")
                print(f"Salary: {row['Salary']}")
                print("-" * 80)
    except FileNotFoundError:
        print("\nNo employee records found. Please add employees first.")
    except Exception as e:
        print(f"\nError occurred while reading file: {e}")

def main():
    employees = []
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Save and Exit")
        
        try:
            choice = input("Enter your choice (1-3): ")
            
            if choice == '1':
                employee = input_employee()
                employees.append(employee)
                print("\nEmployee added successfully!")
            
            elif choice == '2':
                if not employees:
                    print("\nNo employees added yet!")
                else:
                    save_to_csv(employees)  # Save current data before viewing
                    display_employees()
            
            elif choice == '3':
                if employees:
                    save_to_csv(employees)
                print("\nThank you for using Employee Management System!")
                break
            
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")
        
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()