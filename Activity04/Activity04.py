class StudentRecordManager:
    def __init__(self):
        self.records = []

    def add_student_record(self):
        student_id = input("Enter Student ID (6 digits): ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam_grade = float(input("Enter Major Exam Grade: "))
        record = (student_id, (first_name, last_name), class_standing, major_exam_grade)
        self.records.append(record)
        print("Record added successfully.")

    def edit_student_record(self):
        student_id = input("Enter Student ID to edit: ")
        for i, record in enumerate(self.records):
            if record[0] == student_id:
                first_name = input("Enter New First Name: ")
                last_name = input("Enter New Last Name: ")
                class_standing = float(input("Enter New Class Standing Grade: "))
                major_exam_grade = float(input("Enter New Major Exam Grade: "))
                self.records[i] = (student_id, (first_name, last_name), class_standing, major_exam_grade)
                print("Record updated successfully.")
                return
        print("Record not found.")

    def delete_student_record(self):
        student_id = input("Enter Student ID to delete: ")
        for i, record in enumerate(self.records):
            if record[0] == student_id:
                del self.records[i]
                print("Record deleted successfully.")
                return
        print("Record not found.")

    def display_all_records(self):
        for record in self.records:
            print(record)

    def save_records_to_file(self):
        filename = input("Enter filename to save: ")
        with open(filename, 'w') as file:
            for record in self.records:
                file.write(f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n")
        print("Records saved successfully.")

    def load_records_from_file(self):
        filename = input("Enter filename to load: ")
        with open(filename, 'r') as file:
            self.records = []
            for line in file:
                student_id, first_name, last_name, class_standing, major_exam_grade = line.strip().split(',')
                record = (student_id, (first_name, last_name), float(class_standing), float(major_exam_grade))
                self.records.append(record)
        print("Records loaded successfully.")

    def order_by_last_name(self):
        self.records.sort(key=lambda x: x[1][1])
        print("Records ordered by last name.")

    def order_by_grade(self):
        self.records.sort(key=lambda x: 0.6 * x[2] + 0.4 * x[3])
        print("Records ordered by grade.")

    def show_student_record(self):
        student_id = input("Enter Student ID to show: ")
        for record in self.records:
            if record[0] == student_id:
                print(record)
                return
        print("Record not found.")

def display_menu():
    print("Student Record Management System")
    print("1. Add Student Record")
    print("2. Edit Student Record")
    print("3. Delete Student Record")
    print("4. Display All Records")
    print("5. Save Records to File")
    print("6. Load Records from File")
    print("7. Order by Last Name")
    print("8. Order by Grade")
    print("9. Show Student Record")
    print("10. Exit")

def main():
    manager = StudentRecordManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            manager.add_student_record()
        elif choice == '2':
            manager.edit_student_record()
        elif choice == '3':
            manager.delete_student_record()
        elif choice == '4':
            manager.display_all_records()
        elif choice == '5':
            manager.save_records_to_file()
        elif choice == '6':
            manager.load_records_from_file()
        elif choice == '7':
            manager.order_by_last_name()
        elif choice == '8':
            manager.order_by_grade()
        elif choice == '9':
            manager.show_student_record()
        elif choice == '10':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()