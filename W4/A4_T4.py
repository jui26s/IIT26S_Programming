print("program starting")

word_count = 0
character_count = 0

word = input("Insert word (empty stops): ")
while word != "":
    word_count = word_count + 1
    character_count =  character_count + len(word)
    word = input("Insert word (empty stops): ")

print("\nYou inserted:")
print("-", word_count, "words")
print("-", character_count,"characters")

print("\nprogram ending.")
