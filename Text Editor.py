import os

FILENAME = "California Trip.txt"


def readTextFile():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            f.write("I dream of planning a California trip\n")
    with open(FILENAME, "r") as f:
        return f.read()

def saveTextFile(text):
    with open(FILENAME, "w") as f:
        f.write(text)


def AllWordCount(text):
    words = text.split()
    word_counts = {}

    for w in words:
        w = w.lower()
        word_counts[w] = word_counts.get(w, 0) + 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    print("\nTop 5 most common words:")
    for word, count in sorted_words[:5]:
        print(word, ":", count)
    print()

def SingleWordCount(text):
    word = input("Enter a single word: ").strip()

    
    if " " in word or word == "":
        print("Invalid input — enter ONE word only.\n")
        return

    words = text.lower().split()
    count = words.count(word.lower())
    print(f"\n{word.upper()} appears {count} times in the text.\n")

def ReplaceWord(text):
    target = input("Word to replace: ").strip()
    replacement = input("Replacement word: ").strip()

    words = text.split()
    count = 0
    new_words = []

    for w in words:
        if w == target:
            new_words.append(replacement)
            count += 1
        else:
            new_words.append(w)

    print(f"\n{count} words replaced.\n")
    return " ".join(new_words)

def AddText(text):
    add = input("Enter text to add: ")
    print("\nText added.\n")
    return text + " " + add

def DeleteText(text):
    target = input("Enter text to delete first instance of: ")

    index = text.find(target)
    if index == -1:
        print("\nText not found.\n")
        return text

    new_text = text.replace(target, "", 1)
    print("\nFirst instance deleted.\n")
    return new_text

def HighLight(text):
    word = input("Enter word to highlight: ")

    highlighted = text.replace(word, f"**{word}**")
    print("\n" + highlighted + "\n")


def menu():
    text = readTextFile()

    while True:
        print("=== Edit Menu ===")
        print("1: Top 5 most common words")
        print("2: Single Word Frequency")
        print("3: Replace a word")
        print("4: Add Text")
        print("5: Delete Text")
        print("6: Highlight Text")
        print("7: Exit")
        print("=================")

        choice = input(">>input: ")

        if choice == "1":
            AllWordCount(text)

        elif choice == "2":
            SingleWordCount(text)

        elif choice == "3":
            text = ReplaceWord(text)
            saveTextFile(text)

        elif choice == "4":
            text = AddText(text)
            saveTextFile(text)

        elif choice == "5":
            text = DeleteText(text)
            saveTextFile(text)

        elif choice == "6":
            HighLight(text)

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.\n")


menu()
