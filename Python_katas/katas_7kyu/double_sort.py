''' Simple enough this one - you will be given an array. The values in the array will either be numbers or strings, or a mix of both. 
You will not get an empty array, nor a sparse one.

Your job is to return a single array that has first the numbers sorted in ascending order, 
followed by the strings sorted in alphabetic order. The values must maintain their original type.

Note that numbers written as strings are strings and must be sorted with the other strings.''' 


def db_sort(arr): 
    arr_strings = []
    arr_numbers = []
    final_arr = []
    
    for element in arr:
        if isinstance(element, int):
            arr_numbers.append(element)
            
        elif isinstance(element, str):
            arr_strings.append(element)
    
    if arr_numbers and arr_strings:
        arr_numbers.sort()
        arr_strings.sort()
        final_arr.extend(arr_numbers)
        final_arr.extend(arr_strings)
        return final_arr
    if arr_numbers and not arr_strings:
        arr_numbers.sort()
        return arr_numbers
    if arr_strings and not arr_numbers:
        arr_strings.sort()
        return arr_strings
    return final_arr
    
if __name__ == "__main__":
    
    # TEST CASES #

    assert db_sort(["Banana", "Orange", "Apple", "Mango", 0, 2, 2]) == [0,2,2,"Apple","Banana","Mango","Orange"]
    assert db_sort(["C", "W", "W", "W", 1, 2, 0]) == [0,1,2,"C","W","W","W"]
    assert db_sort(['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6]) == [5,6,6,7,10,15,110,"!","2500","come","on"]
    assert db_sort([6, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    assert db_sort([14, 32, 3, 5, 5]) == [3, 5, 5, 14, 32]
    assert db_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
