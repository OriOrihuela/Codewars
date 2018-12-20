'''You get an array of numbers, return the sum of all of the positives ones.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0.'''

def positive_sum(arr):
    
    if not arr:
        return 0
    
    resultado = 0
    for number in arr:
        if number > 0:
            resultado += number
    return resultado 


if __name__ == "__main__":

    # TEST CASES # 

    assert positive_sum([1,2,3,4,5]) == 15
    assert positive_sum([1,-2,3,4,5]) == 13
    assert positive_sum([-1,2,3,4,-5]) == 9
    assert positive_sum([]) == 0
    assert positive_sum([-1,-2,-3,-4,-5]) == 0
