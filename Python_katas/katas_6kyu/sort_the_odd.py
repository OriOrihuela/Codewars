def sort_array(array):
    
    if array == []:
        return []
        
    while array != []:
        pos = -1
        while pos < len(array):
            if array[pos] > array[pos + 1] and array[pos] % 2 != 0:
                aux = array[pos]
                array[pos] = array[pos+1]
                array[pos+1] = aux
            pos += 1
        pos += 1
    return array

if __name__ == "__main__":
    
    #TEST CASES#

    
    
    assert sort_array([]) == []
    assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]
    assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
