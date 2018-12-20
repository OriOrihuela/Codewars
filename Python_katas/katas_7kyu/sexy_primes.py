'''Sexy primes are pairs of two primes that are 6 apart. In this kata, your job is to complete the function sexy_prime(x, y) 
which returns true if x & y are sexy, false otherwise. 
Note: x & y are always positive integers > 0, but they are not always in order of precendence...you can be given either (5,11) or (11,5). 
Both are equally valid.'''

def isPrime(x):
    if x in (0, 1):
        return False
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return False
    return True

def sexy_prime(x, y):
    if (x - y == 6 or x - y == -6) and isPrime(x) and isPrime(y):
        return True
    else:
        return False


if __name__ == '__main__':
    
    # TEST CASES #

    assert sexy_prime(5, 11) == True 
    assert sexy_prime(13, 19) == True
    assert sexy_prime(83, 89) == True
    assert sexy_prime(1, 11) == False
