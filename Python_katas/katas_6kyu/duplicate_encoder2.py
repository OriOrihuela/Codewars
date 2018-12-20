

def duplicate_encode(word):
    word = word.lower()
    final_word = ""
    for letter in word:
        if word.count(letter) == 1:
            final_word += "("
        else:
            final_word += ")"
    return final_word


if __name__ == "__main__":
    

    # TEST CASES #


    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("
