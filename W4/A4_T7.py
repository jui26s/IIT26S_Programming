print("Program starting.")

print("\nCheck multiplicative persistence.")
number = int(input("Insert an integer: "))

steps = 0

while number >= 10:
    digits = [int(digit) for digit in str(number)]

    result = 1

    for digit in digits:
        result = result * digit

    expression = " * ".join(str(digit) for digit in digits)
    print(f"{expression} = {result}")

    number = result
    steps += 1

print("No more steps.")
print(f"\nThis program took {steps} step(s)")

print("\nProgram ending.")