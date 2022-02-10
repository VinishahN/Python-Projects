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
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if choice==0:
  print(rock)
elif choice==1:
  print(paper)
else:
  print(scissors)
random_choice=random.randint(0,2)
if random_choice==0:
  print(f"Computer chose:\n{random_choice}\n{rock}")
elif random_choice==1:
  print(f"Computer chose:\n{random_choice}\n{paper}")
else:
  print(f"Computer chose:\n{random_choice}\n{scissors}")
if choice==0 and random_choice==2:
  print("You won")
elif choice==2 and random_choice==1:
  print("You won")
elif choice==1 and random_choice==0:
  print("You won")
elif choice==random_choice:
  print("The match is draw")
else:
  print("Computer won")

