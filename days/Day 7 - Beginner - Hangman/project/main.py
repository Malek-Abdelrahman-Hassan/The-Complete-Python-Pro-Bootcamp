"""Day 7 Project - Hangman

Guess the hidden word one letter at a time before the figure is drawn.
Target: https://appbrewery.github.io/python-day7-demo/

Build it in the course's five steps:

1. Pick a random word from word_list. Ask for a guess and make it lowercase.
   Loop through the word and print "Right" or "Wrong" for each letter.
2. Print one "_" per letter. After a guess, build `display`: the guessed
   letter where it appears, "_" everywhere else.
3. Repeat guesses with `while not game_over`. Remember correct letters in a
   list created before the loop, so earlier guesses stay in `display`.
   Print "You win." when no "_" is left.
4. Start with lives = 6. A guess that is not in the word costs a life.
   At 0 lives the game is over. Print stages[lives] after every guess.
5. Import word_list, stages, and logo from the two helper files. Print the
   logo. Tell the player when a letter was already guessed (no life lost),
   when a guess costs a life, how many lives are left, and the word if
   they lose.

Messages in the demo:
    Word to guess: _ _ _ _ _
    You've already guessed a
    You guessed d, that's not in the word. You lose a life.
    ****************************4/6 LIVES LEFT****************************
    You win.
    ***********************IT WAS mouse! YOU LOSE**********************

Run from this day's folder:
    python project/main.py
"""

# Write your solution below this line.

import random

import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
display = ["_"] * len(chosen_word)
lives = 6
game_over = False
guessed_letters = []

print("Word to guess: " + " ".join(display))

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue
    guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(
                f"***********************IT WAS {chosen_word}! YOU LOSE**********************"
            )
            continue

    if "_" not in display:
        game_over = True
        print("You win.")
        continue

    print(hangman_art.stages[lives])
    print(f"{'*' * 28}{lives}/6 LIVES LEFT{'*' * 28}")
    print("Word to guess: " + " ".join(display))