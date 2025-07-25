def prime_logic(n):
    if  n <= 1:
        return 'Not a prime number'
    else:
        for i in range(2,n):
            if n % i == 0:
              return 'Not a prime number'
        return 'prime number' 
def user_int():
    
    val = int(input("Enter the value: "))
    result  = prime_logic(val)
    print(result)
    
user_int()