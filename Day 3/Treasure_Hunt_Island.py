print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice = input("You've come to a fork in the road. Do you go left or right? L or R? ")
if choice.lower() == "r":
  print("You fell into a hole. Game over.")
else:
  choice = input("You come to a lake. There is an island in the middle of the lake. Do you want to swim or wait for a boat? S or W? ")
  if choice.lower() == "w":
    choice = input("You come to a house with three doors. Do you go through the red, yellow, or blue door? R, Y, or B ")
    if choice.lower() == "y":
      print("You Win!")
    elif choice.lower() == "r":
      print("You were burned by fire. Game over.")
    elif choice.lower() == "b":
      print("You were eaten by beasts. Game over.")
    else:
      print("Game over.")
  else:
    print("You were drown. Game over.")  
