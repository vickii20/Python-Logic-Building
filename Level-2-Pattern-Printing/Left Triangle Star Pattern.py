value = int(input("Enter the No.of Lines: "))

def patternA(n):
  for row in range(1,n+1):
    for col in range(1,row+1):
      print('*',end='')
    print()

patternA(value)

print('\n')

def patternB(n):
  for row in range(1,n+1):
    for col in range(1,row+1):
      print(col,end='')
    print()

patternB(value)

print('\n')