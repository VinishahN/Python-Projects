import random
from blackjack_art import logo
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack():
  decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
  if decision == 'y':
    clear()
    print(logo)
    user_cards = []
    i=0
    user_cards.append(random.choice(cards))
    should_continue = True
    dealer_cards = []
    i=0
    while i<2:
      dealer_cards.append(random.choice(cards))
      i+=1
    score = 0
    while should_continue:
      user_cards.append(random.choice(cards))
      if not sum(user_cards)>21:
        score=sum(user_cards)
      else:
        if 11 in user_cards:
          user_cards[user_cards.index(11)] = 1
          score = sum(user_cards)
        score = sum(user_cards)
      if 10 in user_cards and 11 in user_cards and len(user_cards)==2:
        score = 0
      
      print(f"\t\tYour cards: {user_cards}, current score: {score}")
      print(f"\t\tComputer's first card: {dealer_cards[0]}")
      if not score>=21 and not score == 0:
        get_another_card = input("Type 'y' to get another card. type 'n' to pass: ")
        if get_another_card == 'y':
          should_continue = True
        else:
          should_continue = False
      else:
          should_continue = False
    get_another_card_dealer = True
    while get_another_card_dealer:
      
      if sum(dealer_cards) <17 and not score>21 and score!=0:
        dealer_cards.append(random.choice(cards))
      else:
          get_another_card_dealer = False
      
    dealer_score = 0
    if not sum(dealer_cards)>21:
      dealer_score=sum(dealer_cards)
    else:
      if 11 in dealer_cards:
        dealer_cards[dealer_cards.index(11)] = 1
      dealer_score = sum(dealer_cards)
    if 10 in dealer_cards and 11 in dealer_cards and len(dealer_cards)==2:
      dealer_score = 0

    print(f"\t\tYour final hand: {user_cards}, final score:{score}")
    print(f"\t\tComputer's final hand: {dealer_cards}, final score: {dealer_score}" )
    if dealer_score<=21 and dealer_score!=0 and score!=0 and score>21:
        print("You went over!You lose😭! ")
    elif score<=21 and score!=0 and dealer_score!=0 and dealer_score>21:
        print("Opponent went over! You win🤩!")
    elif dealer_score == score:
      print("It's a draw😬")
    elif score<=21 and score!=0 and dealer_score!=0 and dealer_score<score:
        print("You win🤩!")
    elif dealer_score == 0:
        print("It's a blackjack! Dealer wins🤩!")
    elif score == 0:
      print("It's a blackjack! You win🤩!")
    else:
      print("You lose😭!")
    blackjack()
blackjack()  

