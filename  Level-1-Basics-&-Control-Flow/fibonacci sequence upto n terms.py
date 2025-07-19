def fibonacci_logic(n):
  num1 = 0
  num2 = 1

  fibo_list = []

  for i in range(n):
    fibo_list.append(num1)
    new_num = num1 + num2
    num1 = num2
    num2 = new_num
  return fibo_list

def user_input():
  num_input = int(input("Enter the Number: "))
  print(f"The Fibonacci Sequence of given number is {fibonacci_logic(num_input)}")

user_input()