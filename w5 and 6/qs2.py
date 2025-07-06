import csv

def add_student_to_csv():

    print("Enter student details:")
    name = input("Name: ")
    student_id = input("ID: ")
    course = input("Course: ")
    level = input("Level: ")
    section = input("Section: ")
    
    student_data = [name, student_id, course, level, section]
    
 
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_data)
    
    print("Student record added successfully!")

add_student_to_csv()