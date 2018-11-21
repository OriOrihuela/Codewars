'''Welcome young Jedi! In this Kata you must create a function that takes an amount of US currency in cents, and returns a dictionary which 
shows the least amount of coins used to make up that amount. The only coin denominations considered in this exercise are: 
Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢). 
Therefor the dictionary returned should contain exactly 4 key/value pairs.
• If the function is passed either 0 or a negative number, the function should return the dictionary with all values equal to 0.
• If a float is passed into the function, its value should be be rounded down, 
and the resulting dictionary should never contain fractions of a coin.
• If a float is passed into the function, its value should be be rounded down, 
and the resulting dictionary should never contain fractions of a coin.'''


def loose_change(cents):
    dictionary = {"Pennies" : 1, "Nickels" : 5, "Dimes" : 10, "Quarters" : 25}
    dictionary2 = {"Pennies" : 0, "Nickels" : 0, "Dimes" : 0, "Quarters" : 0}
    
    if cents <= 0:
        return dictionary2

    return dictionary


if __name__ == "__main__":
    

    # TEST CASES #


   
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}