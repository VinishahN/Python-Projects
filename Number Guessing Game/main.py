from number_guessing_art import logo
import random
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100...")
thought_number = random.randint(1,101)
# print(f"Pssst, the correct answer is {thought_number}") -- Just to check if it works fine
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_level == 'easy':
  attempts = 10
else:
  attempts = 5
should_continue = True
while should_continue:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == thought_number:
    print(f"You got it! The answer was {thought_number}")
    should_continue = False
  elif guess<thought_number:
    print(f"Too low.")
    print("Guess again")
  else:
    print(f"Too high")
    print("Guess again")
  attempts -= 1