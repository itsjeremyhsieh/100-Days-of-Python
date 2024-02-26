from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  new_text = ""
  if direction == "encode":
    sh_amt = shift
    function = "ciphertext"
  elif direction == "decode":
    sh_amt = 26 - shift
    function = "plaintext"
  
  for letter in text:
    if letter in alphabet:
      idx = alphabet.index(letter)
      new_idx = (idx + sh_amt) % 26
      new_letter = alphabet[new_idx]
      new_text += new_letter
    else:
      new_text += letter
  print(f"Your {function} is: {new_text}")

again = "yes"
print(logo)
while again == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if not direction == "encode" and not direction == "decode":
    print("Invalid input")
    continue
  text = input("Type your message:\n").lower()
  shift = input("Type the shift number:\n")
  try:
    shift = int(shift)
  except ValueError:
    print("Invalid input")
    continue
  
  caesar(direction, text, shift)
  again = input("Type 'yes' to continue. Otherwise type 'no'.\n").lower()
print("Bye!")
