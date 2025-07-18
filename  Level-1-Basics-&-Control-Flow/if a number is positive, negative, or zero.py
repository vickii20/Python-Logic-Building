def pos_neg_zero_logic(n):
  if n > 0:
    return 'Positive'
  elif n < 0:
    return 'Negative'
  else:
    return 'Zero'
  
def user_input():
    
    number = int(input("Enter the Number: "))
    result = pos_neg_zero_logic(number)
    print(f"The Given Number is {result}")
    
user_input()