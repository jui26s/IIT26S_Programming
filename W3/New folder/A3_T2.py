print("Program started")
print("string comparison")
word1 = input("Insert the first word: ")
character = input("Insert a character: ")
if character in word1:
    print(f'word "{word1}" contains character "{character}"')
else:
    print(f'word "{word1}" does not contain character "{character}"')
word2 = input("Insert second word: ")
if word1 < word2:
    print(f'The first word "{word1}" is before the second word "{word2}" alphabetically')
elif word2 < word1:
    print(f'The second word "{word2}" is before the first word "{word1}" alphabetically')
else:
    print(f'Both inserted words are the same alphabetically, "{word1}"')
print("Program ending.")