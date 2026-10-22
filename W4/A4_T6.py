print("Program starting.")

number = int(input("Insert a positive integer: "))

steps = 0
print(number, end="")

while number > 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1

    print(" ->", number, end="")
    steps += 1

print()
print(f"Sequence had {steps} total steps.")

print("\nProgram ending.")