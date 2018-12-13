'''Welcome young Jedi! In this Kata you must create a function that takes an amount of US currency in cents, and returns a dictionary which 
shows the least amount of coins used to make up that amount. The only coin denominations considered in this exercise are: 
Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢). 
Therefor the dictionary returned should contain exactly 4 key/value pairs.
• If the function is passed either 0 or a negative number, the function should return the dictionary with all values equal to 0.
• If a float is passed into the function, its value should be be rounded down, 
and the resulting dictionary should never contain fractions of a coin.'''

def loose_change(cents):
    coins = {
        'Nickels': 5,
        'Pennies': 1,
        'Dimes': 10,
        'Quarters': 25
    }

    result = {
        'Nickels': 0,
        'Pennies': 0,
        'Dimes': 0,
        'Quarters': 0
    }

    if cents <= 0:

        return result


    while cents >= 1:

        if cents >= coins['Quarters']:
            result['Quarters'] += 1
            cents -= coins['Quarters']

        elif cents >= coins['Dimes']:
            result['Dimes'] += 1
            cents = cents - coins['Dimes']

        elif cents >= coins['Nickels']:
            result['Nickels'] += 1
            cents = cents - coins['Nickels']

        elif cents >= coins['Pennies']:
            result['Pennies'] += 1
            cents = cents - coins['Pennies']

    return result


if __name__ == "__main__":
    

    # TEST CASES #


   
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert(loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})