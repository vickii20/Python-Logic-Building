def num_logic(n):
  count = 0
  while n > 0:
    digit  = n % 10
    count = count + 1
    n = n // 10
  return count
 
  
def user_input():
  int_value = int(input("Enter the Value: "))
  print(f"The Given Value of Contain {num_logic(int_value)} Digits")

user_input()