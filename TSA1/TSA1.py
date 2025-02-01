# Program 1: Display the number of vowels, consonants, spaces, and other characters in an input string
def count_characters(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    num_vowels = num_consonants = num_spaces = num_others = 0

    for char in input_string:
        if char in vowels:
            num_vowels += 1
        elif char in consonants:
            num_consonants += 1
        elif char.isspace():
            num_spaces += 1
        else:
            num_others += 1

    print(f"Vowels: {num_vowels}")
    print(f"Consonants: {num_consonants}")
    print(f"Spaces: {num_spaces}")
    print(f"Other characters: {num_others}")

# Program 2: Count the sum of the digits from a given input string
def sum_of_digits(input_string):
    total_sum = 0

    for char in input_string:
        if char.isdigit():
            total_sum += int(char)

    print(f"Sum of digits: {total_sum}")

# Program 3a: Display the pattern using nested for statement
def pattern_a():
    for i in range(1, 6):
        for j in range(5, i, -1):
            print(" ", end="")
        for k in range(1, i + 1):
            print(k, end="")
        print()

# Program 3b: Display the pattern using nested while statement
def pattern_b():
    i = 1
    while i <= 7:
        if i % 2 != 0:
            j = 1
            while j <= i:
                print(i, end="")
                j += 1
            print()
        i += 1

# Example usage
input_string = "Hello World! 123"
count_characters(input_string)
sum_of_digits(input_string)
pattern_a()
pattern_b()