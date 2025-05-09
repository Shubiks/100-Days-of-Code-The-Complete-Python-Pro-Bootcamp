bid = {}
repeat = True

while repeat:
    user = str(input("Enter Your Name: "))
    bid_value = int(input("Enter the Bid Price $"))
    bid[user] = bid_value

    next_user = str(input("Is there any one to build,Type 'Yes' or 'No': ")).lower()

    if next_user == 'yes':
        repeat = True
        print("\n" * 100)
    else:
        repeat = False

max = float("-inf")
max_user = ""
for key in bid:
    if bid[key] > max:
        max = bid[key]
        max_user = key

print(f"{max_user} has won the bid at ${max}")

