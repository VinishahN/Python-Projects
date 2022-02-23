from  replit import clear
import higher_lower_art
print(higher_lower_art.logo)
score = 0
import random
from game_data import data
should_continue =True
def compare_followers(a_followers,b_followers,guess):
    if a_followers>b_followers:
      popular = 'a'
    else:
      popular = 'b'
    if guess == popular:
      return "Right"
    else:
      return "Wrong"

A = random.choice(data)
while should_continue:
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
  print(higher_lower_art.vs)
  
  again_b = True
  while again_b:
    B = random.choice(data)
    if A!= B:
      print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
      break
  # print(f"A follower_count : {A['follower_count']}")
  # print(f"B follower_count : {B['follower_count']}")
  # --------Just to check if it works fine -------------------
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  status = compare_followers(A['follower_count'], B['follower_count'],guess)
  clear()
  print(higher_lower_art.logo)
  if status == "Right":
    score +=1
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry! That's wrong! Final score: {score}")
    should_continue = False
  A = B
  