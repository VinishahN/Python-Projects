import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

i=j=k=0
password=""
while i<nr_letters:
  rand= random.choice(letters)
  password=password+rand
  i=i+1
while j<nr_symbols:
  rand= random.choice(symbols)
  password=password+rand
  j=j+1
while k<nr_numbers:
  rand= random.choice(numbers)
  password=password+rand
  k=k+1
#print(f"The easy level password:{password}")
password_list=[]
for i in password:
  password_list.append(i)
#print(password_list) - The list of easy level password
random.shuffle(password_list)
#print(password_list) - The shuffled list using shuffle() method
PyPassword=""
PyPassword=PyPassword.join(password_list) #To join each of the shuffled list item in PyPassword string
print(f"Here is your password: {PyPassword}")

