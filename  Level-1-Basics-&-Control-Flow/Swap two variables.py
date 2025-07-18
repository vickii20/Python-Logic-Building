def swap_logic(a,b):
  temp = a
  a = b
  b = temp

  return a,b

def user_input():
  thing1 = input("Enter the First object: ")
  thing2 = input("Enter the Second object: ")

  swap_result = swap_logic(thing1,thing2)

  print('The Swap have Done!')
  print(f"The First object becomes = {swap_result[0]}")
  print(f"The First object becomes = {swap_result[1]}")
  
user_input()