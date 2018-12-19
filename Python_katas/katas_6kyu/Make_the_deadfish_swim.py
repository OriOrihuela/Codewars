''' Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64] '''

def parse(data):
    value = 0
    final_array = []

    for letter in data:
        if letter == "o":
            final_array.append(value)
        elif letter == "i":
            value += 1
        elif letter == "d":
            value -= 1
        elif letter == "s":
            value = value * value
    return final_array
        





if __name__ == "__main__":
    

    # TEST CASES #

    assert parse("isoisoiso") == [1,4,25]
    assert parse("codewars") == [0]
    assert parse("ooo") == [0,0,0]
    assert parse("ioioio") == [1,2,3]
    assert parse("idoiido") == [0,1]