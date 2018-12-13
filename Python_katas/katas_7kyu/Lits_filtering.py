'''In this kata you will create a function that takes 
a list of non-negative integers and strings and returns a new list with the strings filtered out.'''

def filter_list(lista):
    lista_final = []
    for elemento in lista:
          if isinstance(elemento, int):
              lista_final.append(elemento)
    return lista_final


if __name__ == "__main__":
    

    # TEST CASES #

    print(filter_list([1,2,'a','b']))
    #>>> [1,2]
    print(filter_list([1,'a','b',0,15]))
    #>>> [1,0,15]
    print(filter_list([1,2,'aasf','1','123',123]))
    #>>> [1,2,123]