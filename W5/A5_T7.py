DELIMITER = ","


def collectWords():
    words = ""

    while True:
        word = input("Insert word(empty stops): ")

        if word == "":
            break

        if words == "":
            words = word
        else:
            words = words + DELIMITER + word

    return words


def analyseWords(words):
    if words == "":
        count = 0
        characters = 0
        average = 0
    else:
        wordList = words.split(DELIMITER)

        count = len(wordList)
        characters = 0

        for word in wordList:
            characters += len(word)

        average = characters / count

    print(f"- {count} Words")
    print(f"- {characters} Characters")
    print("- {:.2f} Average word length".format(average))


def main():
    print("Program starting.")

    words = collectWords()
    analyseWords(words)

    print("Program ending.")


if __name__ == "__main__":
    main()