# Hangman-Game
# Hangman Game

A text-based Python game where you guess a hidden word one letter at a time. You can make six incorrect guesses before losing.

## Requirements

- Python 3 installed on your computer.
- No additional packages are needed.

Check your installation with `python --version`. If Python is missing, install it from https://www.python.org/downloads/ . On Windows, select the option to add Python to PATH during installation, then reopen your terminal.

## How to run

1. Download and extract `CodeAlpha_Hangman.zip`.
2. Open the extracted folder containing `hangman.py`.
3. Open a terminal in that folder. On Windows, open the folder in File Explorer, type `cmd` in the address bar, and press Enter.
4. Run:

```sh
python hangman.py
```

If needed, use `py hangman.py` on Windows or `python3 hangman.py` on macOS/Linux.

## How to play

1. The program randomly chooses one of five predefined words.
2. Hidden letters appear as underscores.
3. Type one letter from `a` to `z` and press Enter.
4. A correct guess reveals every occurrence of that letter.
5. An incorrect guess uses one of your six allowed mistakes.
6. Reveal the entire word to win. After six incorrect guesses, you lose and the word is shown.
7. Enter `y` at the replay prompt to start another game. Enter another answer to quit.

## Example

If the selected word is `python`, a round may start like this:

```text
Word: _ _ _ _ _ _
Incorrect guesses remaining: 6
Your guess: p
Good guess!

Word: p _ _ _ _ _
Incorrect guesses remaining: 6
```

The word can be different each time you play.

## Input rules

- Enter one English letter at a time, not the full word.
- Uppercase guesses are accepted and converted to lowercase.
- Repeated guesses do not use another attempt.
- Numbers, symbols, empty input, and multiple letters do not use an attempt.
- Correct guesses do not reduce the remaining allowance.

## Output

Everything runs in the terminal. The game displays your progress, remaining incorrect guesses, guessed letters, and the result. It does not create files or require an internet connection.

## Troubleshooting

- **Python is not recognized:** try `py` on Windows or `python3` on macOS/Linux, or check your Python installation.
- **Cannot open the script:** extract the ZIP and open your terminal in the folder containing `hangman.py`.
- **The window closes immediately:** run the program from an open terminal instead of double-clicking the script.
