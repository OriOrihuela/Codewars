'''Write a function that accepts fight string consists of only small letters and return who wins the fight. 
When the left side wins return "Left side wins!", when the right side wins return "Right side wins!", in other case return "Let's fight again!".'''

def alphabet_war(fight):
    left_side = { "w":4, "p":3, "b":2, "s":1}
    right_side = { "m":4, "q":3, "d":2, "z":1}
    contador_right = 0
    contador_left = 0
    
    for letter in fight:
        if letter in left_side:
            contador_left += left_side[letter]
        elif letter in right_side:
            contador_right += right_side[letter]
    
    if contador_right > contador_left:
        return "Right side wins!"
    elif contador_right < contador_left:
        return "Left side wins!"
    else:
        return "Let's fight again!"

if __name__ == "__main__":

    # TEST CASES #

    print(alphabet_war("z"))
    #>>> "Right side wins!"
    print(alphabet_war("zdqmwpbs"))
    #>>> Let's fight again!"
    print(alphabet_war("wq"))
    #>>> "Left side wins!"
    print(alphabet_war("zzzzs"))
    #>>> "Right side wins!"
    print(alphabet_war("wwwwww"))
    #>>> "Left side wins!"