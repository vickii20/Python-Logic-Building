def mult_logic(n):

  for i in range(1,11):
    multiple = n * i

    print(f"{n} x {i} = {multiple}")
  
def user_input():
  int_value = int(input("Enter the Value: "))
  assign = mult_logic(int_value)
  return assign

user_input()


