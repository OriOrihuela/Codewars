

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

    print(duplicate_encode("din"))
    #>>> "((("
    print(duplicate_encode("recede"))
    #>>> "()()()"
    print(duplicate_encode("Success"))
    #>>> ")())())"
    print(duplicate_encode("(( @"))
    #>>> "))(("