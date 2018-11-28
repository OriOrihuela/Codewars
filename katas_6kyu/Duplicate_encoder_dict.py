
def duplicate_encode(word):




if __name__ == "__main__":
    

    # TEST CASES #


    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("