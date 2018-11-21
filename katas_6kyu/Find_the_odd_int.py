'''Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.'''


def find_it(list):
    
    for number in list:
        if list.count(number) % 2 != 0:
            final_number = number
    return final_number 



if __name__ == "__main__":
    
    
    # TEST CASES #

    assert(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])) == 5