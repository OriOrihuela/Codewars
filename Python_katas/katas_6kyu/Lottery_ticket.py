'''Time to win the lottery!

Given a lottery ticket (ticket), represented by an array of 2-value arrays, you must find out if you've won the jackpot. Example ticket:

[ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
To do this, you must first count the 'mini-wins' on your ticket. Each sub array has both a string and a number within it. 
If the character code of any of the characters in the string matches the number, you get a mini win. Note you can only have one mini win per sub array.

Once you have counted all of your mini wins, compare that number to the other input provided (win). If your total is more than or equal to (win), return 'Winner!'. 
Else return 'Loser!'.

All inputs will be in the correct format. Strings on tickets are not always the same length.'''

def bingo(ticket,win):
    
    value = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    dictionary = dict(zip(alphabet,value))
    total_mini_wins_counted = 0
    
    for element in ticket:
        
        for thing in element:
            
            if isinstance(thing,str):
                count_letter = 0
                
                for letter in thing:
                   
                    if letter in dictionary:
                        count_letter += dictionary[letter]
                        
                        if count_letter != element[1]:
                            count_letter = 0
                        
                        elif count_letter == element[1]:
                            total_mini_wins_counted += 1
                            count_letter = 0
                            break
        
        if total_mini_wins_counted >= win:
            return "Winner!"
    
    return "Loser!"



if __name__ == "__main__":
    

    # TEST CASES #


    assert bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2) == 'Loser!'
    assert bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1) == 'Winner!'
    assert bingo([['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3) == 'Loser!'