'''Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. 
If the two numbers are equal return a or b.
Note: a and b are not ordered!'''

def get_sum(a,b):
    if b > a:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))


if __name__ == "__main__":
    

    # TEST CASES #


    print(get_sum(0,1))
    #>>> 1
    print(get_sum(0,-1))
    #>>> -1
    print(get_sum(5,54))
    #>>> 1475
    print(get_sum(0,78))
    #>>> 3081
    print(get_sum(-32,-1))
    #>>> -528