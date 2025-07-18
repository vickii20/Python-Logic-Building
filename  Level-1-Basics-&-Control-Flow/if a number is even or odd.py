def odd_even_logic(num):
  if num % 2 == 0:
    return 'even'
  else:
    return 'odd'
  
def check_number(): 
  number = int(input("Enter the number: "))
  result = odd_even_logic(number)

  if result == 'even':
    print('YOU ENTER THE EVEN NUMBER')
  else:
    print('YOU ENTERED THE ODD NUMBER')

check_number()
