import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

chosen_no = random.randint(1,100)
difficulty_level = str(input("Choose Difficulty Type easy or hard : ")).lower()

EASY = 10
HARD = 5

def choose_difficulty(level):
    if difficulty_level == "easy":
        return EASY
    return HARD

attempts =  choose_difficulty(difficulty_level)

print(f"You have {attempts} attempts remaining to guess the number.")

while attempts > 0:
    guess = int(input("Make a guess: "))

    if guess == chosen_no:
        print(f"You Got it! The answer was {chosen_no}")
        break
    elif guess > chosen_no:
        print("Two High")
        attempts -=1
        print(f"You have {attempts} attempts to guess the number")
    else:
        print("Two Low")
        attempts -= 1
        print(f"You have {attempts} attempts to guess the number")