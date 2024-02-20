print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
final_payment = (bill + (bill * percentage / 100)) / people
print(f"Each person should pay: ${round(final_payment, 2)}")
