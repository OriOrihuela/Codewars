def comp(array1, array2):
    
    if not (len(array1) == len(array2)):
        return False
    
    if not (array1 and array2):
        return False
    
    for i in array1:
        if i ** 2 in array2:
            return True



if __name__ == "__main__":

    # CASOS TEST


    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

    if comp(a1, a2):
        print ("Test case passed")
    else:
        print ("Test case not passed")

    # CASOS TEST
    a3= []
    a4 = []

    if comp(a3, a4):
        print ("Test case passed")
    else:
        print ("Test case not passed")
