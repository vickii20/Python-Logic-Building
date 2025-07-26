def square_logic(n):

  result = ''
  for row in range(1,n+1):
    for col in range(1,n+1):
      result += '* '
    result += '\n'
  return result

def user_int():
  value = int(input("Enter the Number \n Square Pattern: "))
  final = square_logic(value)
  print(final)

user_int()