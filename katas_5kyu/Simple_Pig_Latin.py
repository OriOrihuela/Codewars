'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !'''


def pig_it(text):
    text = text.split()
    word_to_add = ""
    string = ""
    
    for word in text:
        if word == "?" or word == "!":
            word_to_add = word
            string += word_to_add + " "
            break
        word_to_add = word[1:] + word[0] + "ay"
        string += word_to_add + " "
            
    return string[:-1]
      


if __name__ == "__main__":
    

    # TEST CASES #

    assert pig_it("Quis custodiet ipsos custodes ?") == 'uisQay ustodietcay psosiay ustodescay ?'
    assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
    assert pig_it('This is my string') == 'hisTay siay ymay tringsay'