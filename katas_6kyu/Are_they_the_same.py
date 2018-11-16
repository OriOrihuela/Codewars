def comp(array1, array2):
    
    if not (len(array1) == len(array2)):
        return False
    
    if not (array1 and array2):
        return False
    
    for i in array1:
        if array2 and ( i ** 2 not in array2 ):
            return False
        else:
            array2.remove(i**2)
    
    return True



if __name__ == "__main__":

    # CASOS TEST


    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

    if comp(a1, a2):
        print ("Test case passed")
    else:
        print ("Test case not passed")

    a3 = [81, 99, 34, 11]
    a4 = [81*81, 99*99, 34*34, 44*44]

    if not comp(a3, a4):
        print ("Test case passed")
    else:
        print ("Test case not passed")

    a5= []
    a6 = []

    if not comp(a5, a6):
        print ("Test case passed")
    else:
        print ("Test case not passed")

    a7 = [121, 144, 19, 11]
    a8 = [11*11, 121*121, 144*144, 19*19]

    if comp(a7, a8):
        print ("Test case passed")
    else:
        print ("Test case not passed")

    a9 = [12, 15, 77, 56, 87]
    a10 = [12*12, 12*12, 77*77, 87*87, 56*56]

    if not comp(a9, a10):
        print ("Test case passed")
    else:
        print ("Test case not passed")
