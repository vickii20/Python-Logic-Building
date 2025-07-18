def factorial(n):
  result = 1
  for i in range(n,0,-1):
    result = result * i

  return result

def user_input():
  num = int(input("Enter the Number: "))
  print(f"The Given Number Factorial is: {factorial(num)}")
user_input()