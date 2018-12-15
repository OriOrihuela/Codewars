'''Your task is to implement a function that takes one or more dictionaries and combines them in one result dictionary.

The keys in the given dictionaries can overlap. In that case you should combine all source values in an array. 
Duplicate values should be preserved.

Here is an example:

source1 = {"A": 1, "B": 2} 
source2 = {"A": 3}

result = merge(source1, source2);
// result should have this content: {"A": [1, 3]}, "B": [2]}'''


def merge(*dicts):

    keysList = []
    for diccionario in dicts:
        for key in diccionario:
            keysList.append(key)

    merge = {}
    for key in keysList:
        merge[key] = []
        for diccionario in dicts:
            if key in diccionario:
                merge[key].append(diccionario[key])

    return merge





if __name__ == '__main__':

    assert merge({}, {}, {}) == {}
    assert merge({"A": 1, "B": 2, "C": 3}) == {"A": [1], "B": [2], "C": [3]}
    assert merge({"A": 1}, {"B": 2}) == {"A": [1], "B": [2]}
    assert merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}) == {"A": [1, 4], "B": [2], "C": [3], "D": [5]}