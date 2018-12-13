'''Given two numbers and an arithmetic operator (the name of it, as a string), 
return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.

The four operators are "add", "subtract", "divide", "multiply".'''

def arithmetic(a, b, operator):
    contador = True
    while contador:
        contador = False
        if operator == "add":
            return a + b
        elif operator == "subtract":
            return a - b
        elif operator == "multiply":
            return a * b
        else:
            return a / b


if __name__ == "__main__":
    

    # TEST CASES #


    print(arithmetic(1, 2, "add"), ", 'add' should return the two numbers added together!")
    print(arithmetic(8, 2, "subtract"), ", 'subtract' should return a minus b!")
    print(arithmetic(5, 2, "multiply"), ", 'multiply' should return a multiplied by b!")
    print(arithmetic(8, 2, "divide"),", 'divide' should return a divided by b!")