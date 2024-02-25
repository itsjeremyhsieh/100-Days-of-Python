from hangman_words import word_list
from hangman_art import stages, logo
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
word_guess = []

print(logo)

# print(chosen_word)
display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in word_guess:
        print(f"You've already entered {guess}.")
        continue
    else:
        word_guess.append(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
  
    print(stages[lives])
  
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")
        break
    if lives == 0:
        end_of_game = True
        print("You lose!")
        print(f"The word was {chosen_word}.")
        break
