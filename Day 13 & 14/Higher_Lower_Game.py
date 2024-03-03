from art import logo, vs
from game_data import data
from replit import clear
import random

def randomint():
  pick = random.randint(0, 49)
  return pick
print(logo)

again = 'a'
while again.lower() == 'a':
  wrong = False
  score = 0
  first = randomint()
  second = randomint()
  # print(data[first]["name"])
  while wrong == False:
    print("Compare A:", data[first]["name"] , ", a" , data[first]["description"], ", from", data[first]["country"], f". \n{vs}\nCompare B:", data[second]["name"], ", a", data[second]["description"], ", from", data[second]["country"], "." )
    user_input = input("Who has more followers? A or B: ")
    if data[first]["follower_count"] >  data[second]["follower_count"]:
      ans = "a"
    else:
      ans = "b"
    if ans == user_input.lower():
      score += 1
      clear()
      print(logo)
      print(f"Correct! Current score: {score}")
      first = second
      second = randomint()
    else:
      clear()
      wrong = True
      print(logo)
  print(f"Game over, your final score is {score}")
  again = input("Type 'a' to press again, 'e' to exit: ")
print("Bye bye!")


  
