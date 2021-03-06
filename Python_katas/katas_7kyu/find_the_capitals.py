'''Write a function that takes a single string (word) as argument. 
The function must return an ordered list containing the indexes of all capital letters in the string.'''

def capitals(word):
    index = 0
    indexes = []
    for letter in word:
        if letter.isupper():
            indexes.append(index)
        index += 1
    return indexes


if __name__ == "__main__":
    

    # TEST CASES #

    assert capitals('CodEWaRs') == [0,3,4,6]
    assert capitals('ElAINe') == [0,2,3,4]
    assert capitals('NirVaNa') == [0,3,5]
    assert capitals('OroCHiMarU') == [0,3,4,6,9]
