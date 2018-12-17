''' Given a dictionary/hash/object of languages and your respective test results, return the list of languages where your test score is at least 60, in descending order of the results.

Note: There will be no duplicate values.

Examples
{"Java": 10, "Ruby": 80, "Python": 65}  --> ["Ruby", "Python"]
{"Hindi": 60, "Dutch" : 93, "Greek": 71} --> ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20}   --> [] '''

def my_languages(results):
    final_array = []
    arr = []
    for key in results:
        if results[key] >= 60:
            arr.append(results[key])
    arr = sorted(arr)
    arr = arr[::-1]
    for number in arr:
        for key in results:
            if number == results[key]:
                final_array.append(key)

    return final_array


if __name__ == "__main__":
    

    # TEST CASES #

    assert my_languages({"Java": 10, "Ruby": 80, "Python": 65}) == ["Ruby", "Python"]
    assert my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71}) == ["Hindi", "Dutch", "Greek"]
    assert my_languages({"C++": 50, "ASM": 10, "Haskell": 20}) == []