from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
bid_dict = {}
again = True
while again:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  bid_dict[name] = bid
  again_input = input(
      "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  again = True if again_input == "yes" else False
  clear()

max = 0
max_name = ""
for key in bid_dict:
  if bid_dict[key] > max:
    max = bid_dict[key]
    max_name = key

print(f"The winner is {max_name} with a bid of ${max}!")
