''' Complete the function which returns the weekday according to the input number:

1 returns "Sunday"
2 returns "Monday"
3 returns "Tuesday"
4 returns "Wednesday"
5 returns "Thursday"
6 returns "Friday"
7 returns "Saturday"
Otherwise returns "Wrong, please enter a number between 1 and 7" '''


def whatday(num):
  keys = [1,2,3,4,5,6,7]
  values = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  dictionary = dict(zip(keys,values))
  
  if num in dictionary:
      return dictionary[num]
  else:
      return "Wrong, please enter a number between 1 and 7"


if __name__ == "__main__":
    

    # TEST CASES #


    assert whatday(1) == 'Sunday'
    assert whatday(2) == 'Monday'
    assert whatday(3) == 'Tuesday'
    assert whatday(8) == 'Wrong, please enter a number between 1 and 7'
    assert whatday(20) == 'Wrong, please enter a number between 1 and 7'