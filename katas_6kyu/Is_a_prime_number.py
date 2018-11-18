'''Define a function isPrime/is_prime() that takes one integer argument and returns true/True or false/False 
depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.'''

def is_prime(num):
  if num < 2:
      return False
  for i in range(2, num):
      if num % i == 0:
          return False
  return True


if __name__ == "__main__":
    


    # TEST CASES #


    print(is_prime(0), '0 is not prime')
    #>>> "0 is not prime"
    print(is_prime(1), '1 is not prime')
    #>>> "1 is not prime"
    print(is_prime(2), '2 is prime')
    #>>> "2 is prime"
    print(is_prime(77), ', 77 is not prime')
    #>>> "77 is not prime"
    print(is_prime(54),', 54 is not prime')
    #>>> "54 is not prime"
    print(is_prime(865), ', 865 is not prime')
    #>>> "865 is not prime"