def largest_num_logic(num1,num2,num3):
  if num1>num2 and num1>num3:
    return num1
  elif num2>num1 and num2>num3:
    return num2
  else:
    return num3


def input_num():
  a = int(input('First: '))
  b = int(input('Second: '))
  c = int(input('Third: '))
  result = largest_num_logic(a,b,c)


  print(f"The greater num is: {result}")

input_num()