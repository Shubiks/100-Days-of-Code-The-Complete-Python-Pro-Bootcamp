print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


ans = (bill/people) * (1+(tip/100)) # the formula for raising a value by a percentage is 1 + percentage / 100

print(f"Each person should pay: ${ans:.2f}")