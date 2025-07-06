import csv
import os

file_path = "students.csv"

if not os.path.exists(file_path):
    print(f"Error: '{file_path}' not found in {os.getcwd()}")
    print("Please ensure:")
    print("1. The CSV file exists in this folder")
    print("2. The filename is exactly 'students.csv'")
    print("3. File extensions are visible (not hidden)")
else:
    try:
        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            print("\n--- Student Records ---")
            for row in reader:
                try:
                    print(f"Name: {row['name']}, ID: {row['id']}, Course: {row['course']}, Level: {row['level']}, Section: {row['section']}")
                except KeyError as e:
                    print(f"Missing column in row: {e}")
    except Exception as e:
        print(f"Error reading file: {e}")