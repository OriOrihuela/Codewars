'''Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, 
rounded to the smallest value.'''


def litres(time):
    
    litres = 0
    if time:
        litres = int(time * 0.5)
    return litres

if __name__ == "__main__":
    

    # TEST CASES #

    assert litres(2) == 1
    assert litres(1.4) == 0
    assert litres(12.3) == 6
    assert litres(0.82) == 0
    assert litres(11.8) == 5
    assert litres(1787) == 893
    assert litres(0) == 0 