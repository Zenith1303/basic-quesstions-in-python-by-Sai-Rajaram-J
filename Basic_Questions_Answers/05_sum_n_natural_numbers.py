n = int(input("Enter N (a non-negative integer): "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    total = 0
    number = 1
    while number <= n:
        total += number
        number += 1
    print("Sum:", total)
