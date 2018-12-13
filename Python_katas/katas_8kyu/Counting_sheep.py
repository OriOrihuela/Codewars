'''Consider an array of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined'''

def count_sheeps(array):
  count = 0
  for bol in array:
      if bol == True:
          count += 1
  return count


if __name__ == "__main__":
    

    # TEST CASES #


    array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

    assert count_sheeps(array1) == 17

    array2 = [True,  False,  False,  False,
          True,  True,  False,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  False,  True ,
          False, False, False,  True ]

    assert count_sheeps(array2) == 12

    array3 = [False]

    assert count_sheeps(array3) == 0

    array4 = []

    assert count_sheeps(array4) == 0