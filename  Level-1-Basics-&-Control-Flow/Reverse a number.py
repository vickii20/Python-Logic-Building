def rev_logic(n):
  reverse_num = 0
  while n > 0:
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n = n // 10
  return reverse_num

def user_input():
  value = int(input("Enter the Value: "))
  print(f"The Reverse number of Given Value is {rev_logic(value)}")

user_input()