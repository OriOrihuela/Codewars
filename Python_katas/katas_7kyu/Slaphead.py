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
    values = [0,1,2,3,4,5]
    strings = ["Clean!", "Unicorn!", "Homer!", "Careless!", "Careless!", "Careless!"]
    dictionary = dict(zip(values, strings))

    return [len(s) * "-","Hobo!"] if s.count("/") > 5 else [len(s) * "-", dictionary[s.count("/")]]
        
        

if __name__ == "__main__":
    

    # TEST CASES #
    assert bald("/---------") == ["----------", "Unicorn!"]
    assert bald("/-----/-") == ["--------", "Homer!"]
    assert bald("--/--/---/-/---") == ["---------------", "Careless!"] 