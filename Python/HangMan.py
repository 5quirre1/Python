import time
import random


original_words = {
    "apple": "A red or green fruit that is sweet and crunchy",
    "giraffe": "A tall animal with a long neck that eats leaves",
    "volcano": "A mountain that erupts lava, ash, and gas",
    "mystery": "Something unknown or difficult to explain",
    "ocean": "A vast body of saltwater covering most of Earth",
    "laptop": "A portable computer used for work, school, or games",
    "banana": "A yellow fruit that is soft and sweet inside",
    "horizon": "The line where the earth and sky seem to meet",
    "whisper": "Speaking very softly so only a few people can hear",
    "galaxy": "A huge system of stars, planets, and space dust",
    "tornado": "A violent, spinning windstorm that can cause damage",
    "pyramid": "A large triangular structure built in ancient times",
    "eclipse": "When one space object blocks another from view",
    "gravity": "The force that pulls things toward Earth's center",
    "electricity": "A form of energy that powers lights and devices",
    "compass": "A tool that shows direction using Earth's magnetism",
    "fossil": "The remains of ancient plants or animals in rock",
    "planet": "A large object in space that orbits a star",
    "echo": "A sound that bounces back and can be heard again",
    "desert": "A dry place with little rain and few plants",
}


words = original_words.copy()
new_words = set()


def game():
    word, hint = random.choice(list(words.items()))
    word_guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("\nStarting the game...\n")
    time.sleep(1)

    while attempts > 0 and "_" in word_guessed:
        print("\n" + "=" * 30)
        print(f"Hint: {hint}")
        print(f"Word: {' '.join(word_guessed)}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print("=" * 30)

        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("enter a letter plz")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    word_guessed[i] = guess
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word..")

    print("\n" + "=" * 30)
    if "_" not in word_guessed:
        print(f"Congratulations! You guessed the word: {word} !!")
    else:
        print(f"Out of attempts.. The word was: {word}")

    main()


def add():
    word = input("\nEnter a word to add: ").strip().lower()
    if word in words:
        print(f"'{word}' is already in the word list vro.")
    else:
        hint = input(f"Enter a hint for '{word}': ").strip()
        if hint:
            words[word] = hint
            new_words.add(word)

            print("\nUpdated word list:")
            for w in words:
                if w == word:
                    print(f"{w} <-- Added!")
                else:
                    print(w)
        else:
            print("word wasn't added cause hint was empty")

    main()


def reset():
    global words, new_words
    words = original_words.copy()
    new_words.clear()
    print("\nReset complete!")
    print("Current words:")
    for word in words:
        print(word)


    main()


def main():
    while True:
        print("\n" + "=" * 30)
        print("      Welcome to Hangman!      ")
        print("=" * 30)
        print("\nChoose an option:")
        print("1. Play")
        print("2. Add Words")
        print("3. Reset Words (Remove New)")
        print("4. Exit")
        print("=" * 30)

        option = input("> ").strip()

        if option == "1":
            game()
        elif option == "2":
            add()
        elif option == "3":
            reset()
        elif option == "4":
            print("\nbai bai!")
            exit()
        else:
            print("\nuh no command, choose again")


if __name__ == "__main__":
    main()
