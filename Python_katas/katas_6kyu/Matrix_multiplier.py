'''In mathematics, a matrix (plural matrices) is a rectangular array of numbers. Matrices have many applications in programming, from performing transformations in 2D space to machine learning.
One of the most useful operations to perform on matrices is matrix multiplication, which takes a pair of matrices and produces another matrix – known as the dot product. Multiplying matrices is very different to multiplying real numbers, and follows its own set of rules.
Unlike multiplying real numbers, multiplying matrices is non-commutative: in other words, multiplying matrix a by matrix b will not give the same result as multiplying matrix b by matrix a.
Additionally, not all pairs of matrix can be multiplied. For two matrices to be multipliable, the number of columns in matrix a must match the number of rows in matrix b.
There are many introductions to matrix multiplication online, including at Khan Academy, and in the classic MIT lecture series by Herbert Gross.
To complete this kata, write a function that takes two matrices - a and b - and returns the dot product of those matrices. If the matrices cannot be multiplied, return -1 for JS/Python, or null for Java.
Each matrix will be represented by a two-dimensional list (a list of lists). Each inner list will contain one or more numbers, representing a row in the matrix.

For example, the following matrix:

|1 2|
|3 4|

Would be represented as:

[[1, 2], [3, 4]]

It can be assumed that all lists will be valid matrices, composed of lists with equal numbers of elements, and which contain only numbers. The numbers may include integers and/or decimal points.'''


def getMatrixProduct(matrizA, matrizB):
        
        if len(matrizA[0]) != len(matrizB):
            return - 1 

        posfila_A = 0
        result = []
        fila_result = []
        
        while posfila_A < len(matrizA):

            poscolumna_B = 0

            while poscolumna_B < len(matrizB[0]):
                
                r = 0
                indiceActual = 0

                while indiceActual < len(matrizA[0]):
                    r += matrizA[posfila_A][indiceActual] * matrizB[indiceActual][poscolumna_B]
                    indiceActual += 1
                
                fila_result.append(r)
                poscolumna_B += 1
            
            result.append(fila_result)
            fila_result = []
            posfila_A += 1
            
        return result





if __name__ == "__main__":

    ### CASOS TEST ###

    matriz1 = [[1,6,7],
                [5,8,9],
                [6,7,9]]
    
    #   multiplicar por   #

    matriz2 = [[1,6,7,5,3],
                [6,3,7,2,1],
                [7,3,1,6,7]]
    
    print(getMatrixProduct(matriz1, matriz2))



    matriz3 = [[1,6],
                [5,8],
                [6,7]]
    
    #   multiplicar por   #

    matriz4 = [[1,6,7,5,3,6,2],
                [6,3,7,2,1,7,9]]
    
    assert (getMatrixProduct(matriz3,matriz4))



    matriz5 = [[1,6,7,5,6],
                [5,8,9,7,2],
                [6,7,9,1,1]]
    
    #   multiplicar por   #

    matriz6 = [[1,6,7],
                [6,3,7],
                [7,3,1],
                [1,1,1],
                [7,5,7]]
    
    assert getMatrixProduct(matriz5,matriz6)