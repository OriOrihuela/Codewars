'''In this kata, the number 0 is infected. You are given a list. Every turn, any item in the list that is adjacent to a 0 becomes infected and 
transforms into a 0.  How many turns will it take for the whole list to become infected?
All lists will contain at least one item, and at least one zero, and the only items will be 0s and 1s. 
Lists may be very very long, so pure brute force approach will not work.'''


def infected_zeroes(list):
    
    if list[0] == 0 and len(list) == 1:
        return 0

    pos = 0
    turns = 0
    
    while pos < len(list):
        if list[pos] == 0:
            list[pos + 1] = 0
            pos += 1
        
        if list[-1] == 0 and list[-2] == 1:
            list[-2] = 0
        
        if list.count(0) == len(list):
            turns += 1
            return turns
        turns += 1
    
    return turns

if __name__ == "__main__":
    

    # TEST CASES #


    assert infected_zeroes([0]) == 0
    assert infected_zeroes([0,1,1,0]) == 1
    assert infected_zeroes([0,1,1,1,0]) == 2
    assert infected_zeroes([0,1,1,1]) == 3