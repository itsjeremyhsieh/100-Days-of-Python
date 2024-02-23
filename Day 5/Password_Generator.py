import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
print("Your new password is: ", end = "")
while nr_letters > 0 or nr_symbols > 0 or nr_numbers > 0:
  type = random.randint(0,2)
  if type == 0 and nr_letters > 0:
    nr_letters -= 1
    print(random.choice(letters), end = "")
  elif type == 1 and nr_symbols > 0:
    nr_symbols -= 1
    print(random.choice(symbols), end = "")
  elif type == 2 and nr_numbers > 0:
    nr_numbers -= 1
    print(random.choice(numbers), end = "")
