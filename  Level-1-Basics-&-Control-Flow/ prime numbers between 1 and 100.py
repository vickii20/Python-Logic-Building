def prime_logic(n):
  if n <= 1:
    return 'Not a Prime Number'
  
  else:

    for i in range(2,n):
      if n % i == 0:
        return 'Not a Prime Number'
    return 'Prime Number'

def check_primes():
  for i in range(1,100+1):

    passing = prime_logic(i)
    print(f'The Number {i} is {passing} ')
check_primes()