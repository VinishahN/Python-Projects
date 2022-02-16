# from replit import clear
import random
import hangman_art
print(hangman_art.logo)
from hangman_words import word_list
chosen_word = random.choice(word_list)
lives=6
# print(f'The solution is {chosen_word}.') -- Just for checking if it works fine.
display=[]
for i in chosen_word:
  display.append('_')
word=" "
guessed_words=[]
while '_' in display and lives!=0:
  guess=input("Guess a letter: ")
  # clear()
  guess=guess.lower()
  guessed_words.append(guess)
  count=0
  for i in chosen_word:
    if guess==i:
      display[count]=i
    count+=1
    #print(f"Current position: {count}\n Current letter: {i}\n Guessed letter: {guess}")
  if guess not in chosen_word:
      print(f"You guessed {guess}. That's not in the word. You lose a life.")
      lives-=1
  if guessed_words.count(guess)>1 and guess in display:
    print(f"You\'ve already guessed {guess}")
  print(word.join(display))
  print(hangman_art.stages[lives])
if lives!=0 and '_' not in display:
  print("You win!")
else:
  print("You lose!")