print("========================")
print("Technical Midterm Exam")
print("========================")

filename = "numbers.txt"

with open(filename, 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines, 1):
    numbers = list(map(int, line.strip().split(',')))
    total = sum(numbers)
    result = "Palindrome" if str(total) == str(total)[::-1] else "Not a palindrome"
    print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")

date_input = input("\nEnter the date (mm/dd/yyyy): ")
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

parts = date_input.split("/")
if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])
    if 1 <= month <= 12 and 1 <= day <= 31:
        print(f"Date Output: {months[month - 1]} {day}, {year}")
    else:
        print("Invalid date format! Please use mm/dd/yyyy.")
else:
    print("Invalid date format! Please use mm/dd/yyyy.")
