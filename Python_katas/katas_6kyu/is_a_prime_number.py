'''Define a function isPrime/is_prime() that takes one integer argument and returns true/True or false/False 
depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors 
other than 1 and itself.'''

def is_prime(number):
    if number in (0, 1):
        return False
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True


if __name__ == "__main__":
    


    # TEST CASES #


    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert not is_prime(77)
    assert not is_prime(54)
    assert not is_prime(865)
