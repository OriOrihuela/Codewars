'''You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.'''

def find_outlier(integers):
    numero_par = 0
    numero_impar = 0
    pares = []
    impares = []
    
    for num in integers:
        if num % 2 == 0:
            numero_par += num
            pares.append(numero_par)
        elif num % 2 != 0:
            numero_impar += num
            impares.append(numero_impar)
    
    if len(pares) > len(impares):
        return numero_impar
    else:
        return numero_par

if __name__ == '__main__':

    # TEST CASES #

    print(find_outlier([2, 4, 6, 8, 10, 3]))
    #>>> 3
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
    #>>> 11
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
    #>>> 160