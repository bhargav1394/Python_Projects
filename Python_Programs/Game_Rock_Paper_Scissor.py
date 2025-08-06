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
user_input = int(input("What do you choose, Type 0 for Rock, 1 for paper and 2 for scissors. \n"))
list_rock = [rock,paper,scissors]
if user_input >= 0 or user_input < 2:
    print(f"Your chose: {list_rock[user_input]}")
computer_input=random.randint(0,2)
random_computer=list_rock[computer_input]
print(f"Computer chose: {random_computer}")
if user_input >= 3 or user_input < 0:
    print("You enter wrong number you lose!")
elif user_input == random_computer:
    print("Draw")
elif user_input == list_rock[0] and random_computer == list_rock[2]:
    print("You win")
elif random_computer == list_rock[0] and user_input == list_rock[2]:
    print("You lose!")
elif computer_input > user_input:
    print("You Lose")
elif user_input > computer_input:
    print("You win")