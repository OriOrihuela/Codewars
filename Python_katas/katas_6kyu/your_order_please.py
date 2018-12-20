''' Your task is to sort a given string. Each word in the string will contain a single number. 
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  "" '''


def order(string):
    
    string = string.split()
    new_string = ""
    looked_number = 1
    
    while string:
        for word in string:
            for character in word:
                if character == str(looked_number):
                    new_string += word + " "
                    looked_number += 1
        if looked_number > len(string):
            return new_string[:-1]
    return ""

    


if __name__ == "__main__":
    

    # TEST CASES #

    assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    assert order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
    assert order("") == ""
