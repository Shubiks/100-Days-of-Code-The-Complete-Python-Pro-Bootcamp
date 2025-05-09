import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards = [random.choice(cards), random.choice(cards)]

user_total = sum(user_cards)

print(f"Your cards {user_cards} Total = {user_total}")

dealer_cards = [random.choice(cards), random.choice(cards)]

dealer_total = sum(dealer_cards)

print(f"Dealer's Card {dealer_cards[0]}")


a = True

def adjust_aces(cards):
    while sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1

adjust_aces(user_cards)
adjust_aces(dealer_cards)

def player():
    r = random.choice(cards)
    user_cards.append(r)
    adjust_aces(user_cards)

def dealer():
    r = random.choice(cards)
    dealer_cards.append(r)
    adjust_aces(dealer_cards)
while a:
    repeat = str(input("Do you wanna 'hit' or 'stand'? ")).lower()
    if repeat == "stand":
        if sum(user_cards) ==21 and sum(user_cards) == sum(dealer_cards):
            print("Draw")
            break
        elif sum(user_cards) > 21:
            print("Bust. You Lose!")
            break
        a = False
        print(f"Your cards {user_cards} Total = {sum(user_cards)}")
        print(f"Dealer's Card {dealer_cards} total = {sum(dealer_cards)}")
        while sum(dealer_cards)< 17:
            dealer()
            print(f"Dealer's Card {dealer_cards} total = {sum(dealer_cards)}")
        else:
            if sum(dealer_cards) >21:
                print("Player Won")
                break
            elif sum(user_cards) < sum(dealer_cards):
                print("Dealer Won")
                break
            elif sum(user_cards) > sum(dealer_cards):
                print("Player Won")
                break
            else:
                print("Draw")
                break
    elif repeat == "hit":
        player()
        print(f"Your cards {user_cards} Total = {sum(user_cards)}")
        if sum(user_cards) > 21:
            print(f"Dealer's Card {dealer_cards} total = {sum(dealer_cards)}")
            print("Bust. You Lose!")
            break
        elif  sum(user_cards) ==21 and sum(user_cards) == sum(dealer_cards):
            print(f"Dealer's Card {dealer_cards} total = {sum(dealer_cards)}")
            print("Draw")
            break
