'''Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet" '''


def domain_name(url):
    final_string = ""
    for character in url:
        if character == ".":
                final_string += character
                if character == ".":
                    return final_string
        if character == "/":
                final_string += character
                if character == ".":
                    return final_string
    return final_string


if __name__ == "__main__":
    

    # TEST CASES #

    assert domain_name("http://github.com/carbonfive/raygun") == "github" 
    assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
    assert domain_name("https://www.cnet.com") == "cnet"