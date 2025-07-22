def palindrome_logic(n):
  original_num = n
  reverse_num = 0
  
  while n > 0:
    digit = n % 10 
    reverse_num = reverse_num * 10 + digit
    n = n // 10

  if reverse_num == original_num:
    print('Is Palindrome')
  else:
    print('Not palindrome')

def user_input():
  input_val = int(input("Enter the Value: "))
  palindrome_logic(input_val)

user_input()
