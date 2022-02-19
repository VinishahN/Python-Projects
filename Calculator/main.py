from calculator_art import logo
# print(logo)
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def product(n1,n2):
  return n1*n2
def division(n1,n2):
  return n1/n2
flag = 'n'
while flag=='n':
  print(logo)
  num1 = float(input("What's the first number?: "))
  operations = {
      '+' : add,
      '-' : sub,
      '*' : product,
      '/' : division,
      }
  for operation in operations:
      print(operation)
  should_continue = True
  while should_continue:
    
    operation_symbol = input("Pick out an operation: ")
  
    num2 = float(input("What's the next number?: "))
    
    for operation in operations:
      if operation_symbol == operation:
        function = operations[operation]
    result = function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    decision = input(f"Type 'y' to continue with {result} otherwise type 'n' to start with a new calculation or type -1 to exit:\n")
    if decision == 'y':
      num1 = result
      flag='y'
    elif decision=='n':
      flag='n'
      break
    else:
      flag='y'
      break