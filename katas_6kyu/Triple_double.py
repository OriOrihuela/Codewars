'''Write a function triple_double(num1, num2) which takes numbers num1 and num2 and returns 1 if 
there is a straight triple of a number at any place in num1 and 
also a straight double of the same number in num2.

If this isn't the case, return 0

Examples
triple_double(451999277, 41177722899) == 1
# num1 has straight triple 999s and num2 has straight double 99s

triple_double(1222345, 12345) == 0
# num1 has straight triple 2s but num2 has only a single 2

triple_double(12345, 12345) == 0

triple_double(666789, 12345667) == 1'''


def triple_double(num1, num2):
    global number1_found, number2_found
    
    num1 = str(num1)
    for number in num1:
        num1.count(number)
        if num1.count(number) >= 3:
            number1_found = number
            
    num2 = str(num2)
    for number in num2:
        num2.count(number)
        if num2.count(number) == 2:
            number2_found = number
    
    if number1_found == number2_found:
        return 1
    else:
        return 0


if __name__ == "__main__":
    

    # TEST CASES #


    assert triple_double(1112, 122) == 0
    assert triple_double(451999277, 41177722899) == 1
    assert triple_double(1222345, 12345) == 0
    assert triple_double(12345, 12345) == 0
    assert triple_double(666789, 12345667) == 1
    assert triple_double(10560002, 100) == 1