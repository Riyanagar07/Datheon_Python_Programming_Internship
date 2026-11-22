import random

# List of words
words = ["python", "computer", "developer", "programming",
         "internet", "student", "keyboard"]

secret_word = random.choice(words)

guessed_letters = []

attempts = 6

hangman_art = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

while attempts > 0:

    print(hangman_art[6 - attempts])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", attempts)
    print("Guessed letters:", guessed_letters)

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        print("The word was:", secret_word)
        break

    guess = input("\nGuess a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

if attempts == 0:
    print(hangman_art[6])
    print("\nGAME OVER! You lost.")
    print("The correct word was:", secret_word)
