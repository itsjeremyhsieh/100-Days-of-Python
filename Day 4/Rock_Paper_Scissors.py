import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
  user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. 3 to exit the game.")
  print("You choose: ")
  if user_choice == "0":
    print(rock)
  elif user_choice == "1":
    print(paper)
  elif user_choice == "2":
    print(scissors)
  elif user_choice == "3":
    print("Thanks for playing!")
    break
  else:
    print("Invalid input")
    continue
  computer_choice = random.randint(0, 2)
  print("Computer choose: ")
  if computer_choice == 0:
    print(rock)
  elif computer_choice == 1:
    print(paper)
  else:
    print(scissors)
  user_choice = int(user_choice)
  if user_choice == computer_choice:
    print("Tie!")
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
  elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
  elif user_choice == 2 and computer_choice == 1:
    print("You win!")
  elif user_choice == 1 and computer_choice == 0:
    print("You win!")
  elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
