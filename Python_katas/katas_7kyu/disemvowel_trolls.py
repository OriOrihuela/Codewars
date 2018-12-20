'''Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".'''

def disemvowel(string):
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    final_string = ""
    for i in string:
        if i not in vowels:
            final_string += i
    return final_string 

if __name__ == "__main__":
    

    # TEST CASES #

    assert disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"
    assert disemvowel("I want to break free") == "wnt t brk fr"
    assert disemvowel("Welcome to the jungle") == "Wlcm t th jngl"
    assert disemvowel("Smells like teen spirit") == "Smlls lk tn sprt"
