'''The main idea is to count all the occuring characters(UTF-8) in string. 
If you have string like this aba then the result should be { 'a': 2, 'b': 1 }
What if the string is empty ? Then the result should be empty object literal { }'''

def count(string): 
    if not string:
        return {}
    
    dictionary={}
    for letter in string:
        if letter in dictionary:
            dictionary[letter]=dictionary[letter] + 1  
        else:
            dictionary[letter] = 1
    return dictionary  


if __name__ == "__main__":
    

    # TEST CASES #


    print(count('aba'))
    print(count("acccdafgh"))
    print(count('+56>><<'))
    print(count('asdfdjknboa'))
    print(count('13945157/'))
    print(count(''))