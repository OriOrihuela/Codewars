'''You received a whatsup message from an unknown number. Could it be from that girl/boy with a foreign accent you met yesterday evening?
Write a simple regex to check if the string contains the word hallo in different languages.
These are the languages of the possible people you met the night before:

hello - english
ciao - italian
salut - french
hallo - german
hola - spanish
ahoj - czech republic
czesc - polish
By the way, how cool is the czech republic hallo!!

PS. you can assume the input is a string. 
PS. to keep this a beginner exercise you don't need to check if the greeting is a subset of word ('Hallowen' can pass the test)
PS. regex should be case insensitive to pass the tests'''

def validate_hello(g):
    g = g.lower()
    for greeting in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']:
        if greeting in g:
            return True
    return False


if __name__ == "__main__":
    

    # TEST CASES #

    
    assert validate_hello('hello') == True
    assert validate_hello('ciao bella!') == True
    assert validate_hello('salut') == True
    assert validate_hello('hallo, salut') == True
    assert validate_hello('hombre! Hola!') == True
    assert validate_hello('Hallo, wie geht\'s dir?') == True
    assert validate_hello('AHOJ!') == True
    assert validate_hello('czesc') == True
    assert validate_hello('meh') == False
    assert validate_hello('Ahoj') == True
