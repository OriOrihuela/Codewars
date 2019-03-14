'''In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.

1.  The input string will always be lower case but maybe empty.
2.  If the character in the string is whitespace then pass over it as if it was an empty seat.'''


def wave(input):
  Upper=input.upper()
  array = []
  i = 0
  while i < len(input):
    if input[i] != " ":
        first = input[0:i]
        last = input[i+1:(len(input))]
        array.append(first + Upper[i] + last)
    i+=1
    
    # Miki no me odies :D 
    
  return array


if __name__ == "__main__":
    

    # TEST CASES #


    
    result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    assert wave("hello") == result

    result2 = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
    assert wave("codewars") == result2

    result3 = []
    assert wave("") == result3

    result4 = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
    assert wave("two words") == result4

    result5 = [" Gap ", " gAp ", " gaP "]
    assert wave(" gap ") == result5
