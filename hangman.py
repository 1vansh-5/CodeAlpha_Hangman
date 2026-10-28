import random
import string


WORDS = ["python", "garden", "planet", "window", "pencil"]
MAX_MISTAKES = 6


def play_game():
    word = random.choice(WORDS)
    guessed_letters = set()
    mistakes = 0

    print("\nI have chosen a word. Guess one letter at a time.")
    print(f"You can make {MAX_MISTAKES} incorrect guesses.")

    while mistakes < MAX_MISTAKES:
        display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print(f"\nWord: {display}")
        print(f"Incorrect guesses remaining: {MAX_MISTAKES - mistakes}")
        if guessed_letters:
            print("Guessed letters:", ", ".join(sorted(guessed_letters)))

        guess = input("Your guess: ").strip().lower()
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter one letter from a to z.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)
        if guess in word:
            print("Good guess!")
        else:
            mistakes += 1
            print("That letter is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nYou won! The word was '{word}'.")
            return

    print(f"\nYou lost! The word was '{word}'.")


def main():
    print("Welcome to Hangman!")
    while True:
        play_game()
        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
