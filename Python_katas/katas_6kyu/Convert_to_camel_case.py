##Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
##The first word within the output should be capitalized only if the original word was capitalized.

def to_camel_case(text):
    for character in text:
        if character == "-":
            text = text.replace("-", " ")
        if character == "_":
            text = text.replace("_", " ")
    txt = text.split()
    new_txt = []
    for i in range (0,len(txt)):
        if i > 0:
            new_txt.append(txt[i].capitalize())
        else:
            new_txt.append(txt[i])

    return "".join(new_txt)

if __name__ == "__main__":
    
    # TEST CASES
    print(to_camel_case('the-stealth_warrior'))
    #>>>>theStealthWarrior
    
    print(to_camel_case("That_was-Amazing"))
    #>>>>ThatWasAmazing