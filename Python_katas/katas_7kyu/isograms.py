'''An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.'''

def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True


if __name__ == "__main__":
    

    # TEST CASES #


    assert is_isogram("Dermatoglyphics") == True 
    assert is_isogram("isogram") == True
    assert is_isogram("aba") == False
    assert is_isogram("moOse") == False
    assert is_isogram("isIsogram") == False
    assert is_isogram("") == True
