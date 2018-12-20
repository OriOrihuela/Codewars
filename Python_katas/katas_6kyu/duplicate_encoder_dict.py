
def duplicate_encode(word):
    
    encode = {}
    word = word.lower()
    
    for char in word:
        if char not in encode:
            encode[char] = "("
        else:
            encode[char] = ")"
    
    new_word = ""
    
    for char in word:
        new_word += encode[char]
    return new_word


if __name__ == "__main__":
    

    # TEST CASES #


    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("
