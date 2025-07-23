def  str_palindrome(n):
  original_str = n
  word = n[::-1]

  if word == original_str:
    print(f"The given Word '{original_str}' Is Palindrome '{word}'")
  else:
    print(f"The given Word '{original_str}' Not a Palindrome '{word}'")

def user_input():
  int_value = input("Enter the Word: ")
  str_palindrome(int_value)

user_input()