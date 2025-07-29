value = int(input("Enter the No.of Lines: "))

def patternA(n):                               # *
  for row in range(1,n+1):                     # * *
    for col in range(1,row+1):                 # * * *
      print('*',end=' ')                       # * * * *
    print()                                    # * * * * * 

patternA(value)

print('\n')

def patternB(n):                               # 1
  for row in range(1,n+1):                     # 1 2
    for col in range(1,row+1):                 # 1 2 3
      print(col,end=' ')                       # 1 2 3 4 
    print()                                    # 1 2 3 4 5

patternB(value)

print('\n')

def patternC(n):                               # 1
  initial_val = 1                              # 0 1
                                               # 1 0 1
  for row in range(1,n+1):                     # 0 1 0 1
                                               # 1 0 1 0 1
    if row % 2 == 0:
      initial_val = 0
    else:
      initial_val = 1

    for col in range(1,row+1):

      print(initial_val,end=' ')
      initial_val = int(not initial_val)
    print()

patternC(value)

print('\n')

def patternD(n):                               # 1
                                               # 2 3
  initial_val = 1                              # 4 5 6
                                               # 7 8 9 10
  for row in range(1,n+1):                     # 11 12 13 14 15 
    for col in range(1,row+1):
      print(initial_val,end=' ')
      initial_val += 1
    print()

patternD(value)

print('\n')