last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
age = input("Enter age: ")
contact_number = input("Enter contact number: ")
course = input("Enter course: ")

student_info = f"Last Name: {last_name}\nFirst Name: {first_name}\nAge: {age}\nContact Number: {contact_number}\nCourse: {course}\n"
with open("TF2/students.txt", "a") as file:
    file.write(student_info + "\n")

print("Student information has been saved to 'TF2/students.txt'.")