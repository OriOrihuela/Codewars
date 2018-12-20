'''Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the 
following phrases each time a petal was torn:
I love you
a little
a lot
passionately
madly
not at all
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where nb_petals > 0.'''

def how_much_i_love_you(nb_petals):
    
    list = ['I love you','a little','a lot', 'passionately', 'madly' ,'not at all']
    
    pos = 0
    
    for number in range(nb_petals):
      answer = list[pos]
      pos += 1
      if pos == 6:
        pos = 0
    return answer


if __name__ == "__main__":
    

    # TEST CASES #


     assert how_much_i_love_you(3) == "a lot"
     assert how_much_i_love_you(6) == "not at all"
     assert how_much_i_love_you(7) == "I love you"
