def main():
    while True:
        print("====================================")
        print("\t\tMENU")
        print("====================================")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter Choice: ").upper()
        
        if choice == 'Q':
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))
            except ValueError:
                print("Invalid input! Enter numeric values.")
                continue
            
            if choice == 'D':
                result = divide(num1, num2)
            elif choice == 'E':
                result = exponentiate(num1, num2)
            elif choice == 'R':
                result = remainder(num1, num2)
            elif choice == 'F':
                result = summation(int(num1), int(num2))
            
            if result is not None:
                print(f"Result: {result}")
        else:
            print("Please select a valid option.")

def divide(a, b):
    if b == 0:
        print("Error! Denominator must not be zero.")
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error! Denominator must not be zero.")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("Error! The second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))


if __name__ == "__main__":
    main()