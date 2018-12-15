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


    print(is_isogram("Dermatoglyphics"))
    #>>> True
    print(is_isogram("isogram"))
    #>>> True
    print(is_isogram("aba"))
    #>>> False
    print(is_isogram("moOse"))
    #>>> False
    print(is_isogram("isIsogram"))
    #>>> False
    print(is_isogram(""))
    #>>> True