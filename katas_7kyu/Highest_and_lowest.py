'''In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.'''

def high_and_low(numbers):
    numbers = numbers.split()
    numbers = [int(number) for number in numbers]
    resultado = str(max(numbers)), str(min(numbers))
    return " ".join(resultado)

if __name__ == "__main__":
    
    # TEST CASES #

    print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
    #>>> "542 -214"