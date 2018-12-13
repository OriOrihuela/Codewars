'''Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays 
have the "same" elements, with the same multiplicities. 
"Same" means, here, that the elements in b are the elements in a squared, regardless of the order.'''

def comp(array1, array2):
    
    if array1 == None or array2 == None:
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

    assert comp(a1, a2)
        

    a3 = [81, 99, 34, 11]
    a4 = [81*81, 99*99, 34*34, 44*44]

    assert not comp(a3, a4)
        

    a5= []
    a6 = []

    assert comp(a5, a6)
        

    a7 = [121, 144, 19, 11]
    a8 = [11*11, 121*121, 144*144, 19*19]

    assert comp(a7, a8)
        

    a9 = [12, 15, 77, 56, 87]
    a10 = [12*12, 12*12, 77*77, 87*87, 56*56]

    assert not comp(a9, a10)
        
