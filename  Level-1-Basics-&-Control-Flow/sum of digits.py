def myfunc(n):
  total = 0

  while n > 0:
    digit = n % 10 # get the last number from the  - n
    total += digit #adding the last value to the total
    n = n // 10 #remove the last value from the n
  return total

def user_input():
  value = int(input("Enter the Value: "))
  print(f"The Given Value of Sum is {myfunc(value)}")

user_input()