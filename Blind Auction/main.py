from replit import clear

from art import logo
print(logo)
print("Welcome to the secret auction program.")
should_continue = True
bids = {}
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if any_other_bidders == 'yes':
      clear()
      should_continue = True
    else:
      clear()
      should_continue = False
# print(bids)
highest_bid =0
for key in bids:
  if bids[key]> highest_bid:
    highest_bid= bids[key]
    highest_bidder = key
  else:
    highest_bid = highest_bid
  
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")



