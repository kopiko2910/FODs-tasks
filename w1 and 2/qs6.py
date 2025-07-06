#this program calculates average, total, percentage and division of the student
marks_science = float(input("Enter your marks in Science: "))
marks_maths = float(input("Enter your marks in Maths: "))
marks_computer = float(input("Enter your marks in Computer: "))
marks_social = float(input("Enter your marks in Social: "))
marks_english = float(input("Enter your marks in English: "))
total_marks = marks_science + marks_maths + marks_computer +marks_social+ marks_english
print("Total marks obtained = ",total_marks)
print("The average is ",total_marks/5)
total_per = (total_marks/500)*100
print("Your marks in percentage is : ",total_per,'%')
if total_per>=80:
    print("DISTINCTION")
elif total_per>=60:
    print("FIRST DIVISION")
elif total_per>=50:
    print("SECOND DIVISION")
elif total_per>=45:
    print("THIRD DIVISION")
else:
    print("FAIL")
