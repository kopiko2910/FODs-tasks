class Student:
    def __init__(self, id, name, address, admission_year, level, section):
        self.id = id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section
    
    def display_info(self):
        print("\nStudent Information:")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

def create_student():
    print("Enter Student Details:")
    id = input("ID: ")
    name = input("Name: ")
    address = input("Address: ")
    admission_year = input("Admission Year: ")
    level = input("Level: ")
    section = input("Section: ")
  
    student = Student(id, name, address, admission_year, level, section)
    return student


if __name__ == "__main__":
    print("Student Information System")
    student = create_student()
    student.display_info()