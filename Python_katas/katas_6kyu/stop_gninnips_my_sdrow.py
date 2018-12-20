''' Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test" '''

def spin_words(s):
    final_string = ""
    s = s.split()
    
    for word in s:
        if len(word)>= 5:
            word = word[::-1]
        final_string += word + " "
    
    if len(final_string) != len(s):
        final_string = final_string[:-1]
    
    return final_string

if __name__ == "__main__":
        

        # TEST CASES #

        assert spin_words("Welcome") == "emocleW"
        assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
        assert spin_words("one Just is Strings") == 'one Just is sgnirtS'
        assert spin_words( "This is a test") == "This is a test" 
        assert spin_words( "This is another test" ) == "This is rehtona test"
