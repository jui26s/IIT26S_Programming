print("Program starting.")
Word=input("Insert a closed compound word: ")
print(f"The Word you inserted is '{Word}' and in reverse it is '{Word[::-1]}'.")
print(f"The inserted word length is {len(Word)}")
print(f"Last character is '{Word[-1]}'")
print(f"Take substring from the inserted word by inserting...")
Start=int(input("1) starting point: "))
End=int(input("2) ending point: "))
step=int(input("3) step size: "))
print(f"The word '{Word}' sliced to the defined substring is '{Word[Start:End:step]}'.")
print("program ending.")


