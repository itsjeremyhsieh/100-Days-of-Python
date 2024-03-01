#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

print(logo)
print("\n")
play_again = True
guess = -1
while play_again == True:
  comp_guess = random.randint(1, 100)
  while guess == -1:
    user_mode = input("Welcome!\nPlease select the level, 1 for easy mode, 2 for hard mode: ")
    if user_mode == "1":
      guess = 10
      print("You have 10 guesses.")
    elif user_mode == "2":
      guess = 5
      print("You have 5 guesses.")
    else:
      print("Invalid input!")
      continue
  print("I'm thinking a number between 1 and 100, ")
  win = False
  while guess > 0 and win == False:
    user_input = input("Guess what I'm thinking: ")
    try:
      user_input = int(user_input)
    except:
      print("Invalid input!")
      continue
    
    if user_input == comp_guess:
      win = True
    elif user_input < comp_guess:
      guess -= 1
      if guess == 1:
        print(f"Guess higher! {guess} guess left.")
      elif guess == 0:
        print(f"You have ran out of guesses.")
      else:
        print(f"Guess higher! {guess} guesses left.")
    else:
      guess -= 1
      if guess == 1:
        print(f"Guess lower! {guess} guess left.")
      elif guess == 0:
        print(f"You have ran out of guesses.")
      else:
        print(f"Guess lower! {guess} guesses left.")
    
  if win == True:
     print(f"Congrate! You have guessed the number. The number was {comp_guess}!")
  else:
     print(f"You lose! The number was {comp_guess}!")
  user_play_again = input("Do you want to play again? 1 for again, 2 to exit: ")
  if user_play_again == "1":
    play_again = True
    guess = -1
    continue
  else:
    break
print("Bye bye!")
  
  
