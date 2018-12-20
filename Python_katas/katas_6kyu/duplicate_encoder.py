

def duplicate_encode(word):
    final_word = ''
    word = word.lower()
    for letter in word:
        if word.count(letter) == 1:
            final_word += '('
        if word.count(letter) >= 2:
            final_word += ')'
    return final_word

if __name__ == '__main__':

    # TEST CASES #

    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("
