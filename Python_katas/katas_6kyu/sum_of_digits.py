''' In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. 
If that value has two digits, continue reducing in this way until a single-digit number is produced. 
This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2 '''

def digital_root(n):
    n = str(n)
    new_n = ""
    sum_digits = True
    while sum_digits:
        sum_digits = False
        sumatory = 0
        for number in n:
            sumatory += int(number)
            new_n = str(sumatory)
            
        if len(new_n) == 1:
            return int(new_n)    
        elif len(new_n) < len(n):
                n = new_n
                sum_digits = True

    return int(new_n)


if __name__ == "__main__":
    

    # TEST CASES #

    assert digital_root(16) == 7
    assert digital_root(456) == 6