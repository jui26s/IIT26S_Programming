print("Program starting.")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

if start >= stop:
    print("Starting point value must be less than the stopping point value.")
elif inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")
else:
    print("Using break:")
    for number in range(start, stop + 1):
        if number == inspection:
            break
        print(number, end=" ")
    print()

    print("Using continue:")
    for number in range(start, stop ):
        if number == inspection:
            continue
        print(number, end=" ")
    

print("Program ending.")