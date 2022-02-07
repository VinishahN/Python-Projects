#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6

print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
if(tip==12):
  final_tip=total_bill*0.12
  total_including_tip=total_bill+final_tip
elif(tip==15):
  final_tip=total_bill*0.15
  total_including_tip=total_bill+final_tip
else:
  final_tip=total_bill*0.10
  total_including_tip=total_bill+final_tip
split_bill=round(total_including_tip/people,2)
print(f"Each person should pay: $ {split_bill}")