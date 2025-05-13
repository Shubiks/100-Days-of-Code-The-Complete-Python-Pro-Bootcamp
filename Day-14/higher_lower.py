from art import logo, vs
from game_data import data
import random

print(logo)

# Get account display data
def account_data(acc):
    name = acc["name"]
    followers = acc["follower_count"]
    description = acc["description"]
    country = acc["country"]
    return [name, followers, description, country]

# Fix generate_b to return new account_b
def generate_b(account_a):
    account_b = random.choice(data)
    while account_a["name"] == account_b["name"]:
        account_b = random.choice(data)
    return account_b

# Main game logic
def game(a_details, b_details, score):
    print(f"\nCompare A: {a_details[0]}, a {a_details[2]} from {a_details[3]}")
    print(vs)
    print(f"Against B: {b_details[0]}, a {b_details[2]} from {b_details[3]}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    correct_ans = "A"
    if b_details[1] > a_details[1]:
        correct_ans = "B"

    if user_guess != correct_ans:
        feedback = f"Sorry! That's wrong. Final Score: {score}"
        return False, feedback, score
    else:
        score += 1
        feedback = f"You're right! Current Score: {score}"
        return True, feedback, score

# Initialize game
account_a = random.choice(data)
account_b = generate_b(account_a)
score = 0
game_on = True

# Game loop
while game_on:
    a_details = account_data(account_a)
    b_details = account_data(account_b)

    correct, feedback, score = game(a_details, b_details, score)
    print(feedback)

    if not correct:
        game_on = False
    else:
        account_a = account_b
        account_b = generate_b(account_a)