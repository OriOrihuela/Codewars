'''Create a function isDivisible(n, x, y) that checks if a number n is divisible by two numbers x AND y. 
All inputs are positive, non-zero digits.'''

def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    
    # TEST CASES #
    
    print(is_divisible(3,3,4))
    #>>> False, test case not passed
    print(is_divisible(12,3,4))
    #>>> True, test case passed
    print(is_divisible(8,3,4))
    #>>> False, test case not passed
    print(is_divisible(48,3,4))
    #>>> True, test case passed