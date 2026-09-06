import random

# 5 predefined words
words = ["python", "laptop", "college", "coding", "program"]

# Randomly choose a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
attempts = 6

# Display word with underscores
display = ["_"] * len(word)

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses.")

while attempts > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Wrong guesses left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if input is a single alphabet
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    # Wrong guess
    else:
        attempts -= 1
        print("Wrong guess!")

# Game result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)