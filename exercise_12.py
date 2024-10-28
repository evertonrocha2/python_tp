def classify_words():
    word = input("Enter a word: ")
    if len(word) < 5:
        print("The word is too short")
    else:
        print("The word is too long")

if __name__ == "__main__":
    classify_words()