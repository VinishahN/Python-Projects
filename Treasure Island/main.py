print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction=input('''You're at a cross road.Where do you wanna go?  Type "left" or "right". ''')
if(direction=="left"):
  decision=input("You come to a lake.There is an island in the middle of the lake.Type 'wait' if you wanna wait for a boat or type 'swim' to swim across.")
  if decision=="wait":
    colour=input("You have arrived at the island safely.There is a house with three doors.One red,one blue and the other yellow.Which colour do you choose? ")
    if colour=="red":
       print("You entered a room which was full of poisonous snakes...Game over.")
    elif colour=="blue":
       print("You entered a room of angels....Congrats...You win")
    else:
       print("You entered a room of fire! Game over.")
  else:
    print("You were eaten by the shark...Choose wisely next time. Game over.")
else:
  print("You fell into a hole...Game over.")

