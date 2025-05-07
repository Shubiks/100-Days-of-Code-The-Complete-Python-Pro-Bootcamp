import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock,paper,scissors]

#input message

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(choice_list[user_input])
computer_choice  = random.randint(0,len(choice_list)-1)
print("Computer chose: \n")
print(choice_list[computer_choice])

if  user_input<0 and  user_input >3:
    print("Invalid Number")
if ((user_input == 2 and computer_choice == 1) or
        (user_input == 0 and computer_choice == 2) or (user_input == 1 and computer_choice == 0)):
    print("You win!")
elif user_input == computer_choice:
    print("It's a draw")

else:
    print("You lose!")


