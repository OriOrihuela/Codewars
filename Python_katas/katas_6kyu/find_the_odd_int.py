'''Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.'''


def find_it(list):
    
    for number in list:
        if list.count(number) % 2 != 0:
            final_number = number
    return final_number 



if __name__ == "__main__":
    
    
    # TEST CASES #

    assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
    assert find_it([24,4,5,6,7,7,4,4,7,9,10]) == 10 
    assert find_it([-1,-3,-1,-1,-3,]) == -1
    assert find_it([0,7,7,0,4,56,56,34,-34,56,0]) == 0
