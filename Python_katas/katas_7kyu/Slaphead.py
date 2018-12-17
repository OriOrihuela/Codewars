''' Being a bald man myself, I know the feeling of needing to keep it clean shaven. Nothing worse that a stray hair waving in the wind.

You will be given a string(x). Clean shaved head is shown as "-" and stray hairs are shown as "/". Your task is to check the head for stray hairs and get rid of them.

You should return the original string, but with any stray hairs removed. Keep count of them though, as there is a second element you need to return:

0 hairs --> "Clean!"
1 hair --> "Unicorn!"
2 hairs --> "Homer!"
3-5 hairs --> "Careless!"
>5 hairs --> "Hobo!"

So for this head: "------/------" you should return:

["-------------", "Unicorn!"] '''

def bald(s):
    final_array = []
    str_1 = ""
    str_2 = ""
    
    for char in s:
        if char == "/":
            str_1 += "-"
        if char != "/":
            str_1 += char
    final_array.append(str_1)
    
    for char in s:
        if s.count("/") == 0:
            str_2 += "Clean!"
            break
        if char == "/" and s.count(char) == 1:
            str_2 += "Unicorn!"
            break
        if char == "/" and s.count(char) == 2:
            str_2 += "Homer!"
            break
        if char == "/" and s.count(char) in range(3, 6):
            str_2 += "Careless!"
            break
        if char == "/" and s.count(char) > 5:
            str_2 += "Hobo!"
            break
    final_array.append(str_2)
        
        

if __name__ == "__main__":
    

    # TEST CASES #
    assert bald("/---------") == ["----------", "Unicorn!"]
    assert bald("/-----/-") == ["--------", "Homer!"]
    assert bald("--/--/---/-/---") == ["---------------", "Careless!"] 