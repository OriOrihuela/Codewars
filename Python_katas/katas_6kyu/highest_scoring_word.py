'''Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.'''

def high(x):
    arr1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    arr2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    dictionary = dict(zip(arr2, arr1))
    string = ""
    answer = ""
    count = 0
    max = 0
    
    for letra in x:
    
        if letra != " ":
            count += dictionary[letra]
            string += letra
            if count > max:
                max = count
                answer = string        
        else:
            count=0
            string = ""
    
    return answer

if __name__ == "__main__":
    

    # TEST CASES #


    assert high('man i need a taxi up to ubud') == 'taxi'
    assert high('what time are we climbing up the volcano') == 'volcano'
    assert high('take me to semynak') == 'semynak'
    assert high('massage yes massage yes massage') == 'massage'
    assert high('take two bintang and a dance please') == 'bintang'
