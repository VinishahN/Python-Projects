import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import string

def caesar(text,shift,direction):
    result=""
    symbols=[]
    symbols.extend(string.punctuation)
    #print(symbols)
    
    for i in range(len(text)):
      if text[i] in symbols or text[i] == " " or text[i].isdigit():
         result+=text[i]
         continue
      index=alphabet.index(text[i])
      if direction == 'encode':
         required_index = index+shift
      elif direction == 'decode':
         required_index = index-shift
      while True:
        if required_index>=len(alphabet):
          required_index=required_index-len(alphabet)
        elif required_index<0:
          required_index=required_index+len(alphabet)
        else:
          break
      result+=alphabet[required_index]
    print(f"Here's the encoded result: {result}")
    

to_continue = True
while to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    decision = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if decision == 'yes':
      to_continue = True
    else:
      to_continue = False
      print("GoodBye!")