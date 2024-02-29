from art import logo
from replit import clear
import random

def get_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = cards[random.randint(0, 12)]
  return card
  
def compute_total(array):
  total = 0
  for i in array:
    total += i
    if total > 21:
      total, array = check_ace(array)
      return total, array
  return total, array

def check_ace(array):
  total = 0
  cnt = 0
  for i in array:
    if i == 11:
      total += 1
      array[cnt] = 1
    else:
      total += i
    cnt += 1
  return total, array
  
def blackjack():
  user = []
  computer = []
  for i in range(0 ,2):
    user.append(get_card())
    computer.append(get_card())
  user_total, user = compute_total(user)
  computer_total, computer = compute_total(computer)
  # print(user)
  # print(computer)
  print(f"  Your card is: {user}, current score: {user_total}")
  if user_total == 21 and computer_total == 21:
    print(f"  Computer's final hand: {computer}, final score: {computer_total}")
    return("Draw!! 😶")
    
  elif user_total == 21 and not computer_total == 21:
    print(f"  Computer's final hand: {computer}, final score: {computer_total}")
    return("You win!! 😊")
    
  elif (not user_total == 21) and computer_total == 21:
    print(f"  Computer's final hand: {computer}, final score: {computer_total}")
    return("You lose!! 😭")
    
  if user_total > 21:
    user_total, user = check_ace(user)
  if user_total > 21:
    return("You lose!! 😭")
    
  print(f"  Computer's first card: {computer[0]}")
  
  get_card_input = input("Type 'y' to get another card, type 'n' to pass: ")
  print("\n")
  while get_card_input == "y":
    user.append(get_card())
    user_total, user = check_ace(user)
    print(f"  Your card is: {user}, current score: {user_total}")
    if user_total > 21:
      return("You lose!! 😭")
      
    get_card_input = input("Type 'y' to get another card, type 'n' to pass: ")
    print("\n")
    
  while computer_total < 17:
    computer.append(get_card())
    computer_total, computer = check_ace(computer)
    if computer_total > 21:
      print(f"  User's final hand: {user}, final score: {user_total}")
      print(f"  Computer's final hand: {computer}, final score: {computer_total}")
      return("You win!! 😊")
      
  print(f"  User's final hand: {user}, final score: {user_total}")
  print(f"  Computer's final hand: {computer}, final score: {computer_total}")
  if computer_total < user_total:
    return("You win!! 😊")
  elif computer_total > user_total:
    return("You lose!! 😭")
  else:
    return("Draw!! 😶")
  return("End of the game.")


print(logo)
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play == "y":
  clear()
  print(logo)
  print(blackjack())
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print("Bye bye!")    
