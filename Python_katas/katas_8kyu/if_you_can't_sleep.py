''' Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". 
Input will always be valid, i.e. no negative integers. '''

def count_sheep(number):
    final_string = ""
    numberToAdd = 1
    while numberToAdd <= number:
        stringToAdd = str(numberToAdd) + " sheep..."
        final_string += stringToAdd
        numberToAdd += 1
    return final_string


if __name__ == "__main__":
    

    # TEST CASES #

    assert count_sheep(1) == "1 sheep..."
    assert count_sheep(2) == "1 sheep...2 sheep..."
    assert count_sheep(3) == "1 sheep...2 sheep...3 sheep..."