from art import logo
print(logo)

#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2
def calculator():
  operation = {"+": add, "-": subtract, "*": multiply, "/": divide}
  num1_set = False
  while num1_set == False:
    try:
      num1 = float(input("What's the first number? "))
    except ValueError:
      print("Invalid input")
      continue
    num1_set = True
  again = 'y'
  first = True

  while again == 'y':
    operation_set = False
    second_set = False
    for key in operation:
      print(key)
    
    while operation_set == False:
      operation_symbol = input("Pick an operation from the line above: ")
      if operation_symbol not in operation:
        print("Invalid input")
      else:
        operation_set = True
        
    while second_set == False:
      try:
        num2 = float(input("What's the second number? "))
      except ValueError:
        print("Invalid input")
        continue
      second_set = True
      
    if first == False:
      num1 = result
    result = operation[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    first = False;
    again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'e' to exit: ")
    if again == 'n':
      calculator()
    elif again == 'e':
      return
calculator()
print("Bye!")
