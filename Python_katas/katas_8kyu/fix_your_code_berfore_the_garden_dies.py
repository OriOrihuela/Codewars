'''You have an award-winning garden and everyday the plants need exactly 40mm of water. 
You created a great piece of JavaScript to calculate the amount of water your plants will need when you have taken into consideration the amount of rain water that is forecast for the day. 
Your jealous neighbour hacked your computer and filled your code with bugs.
Your task is to debug the code before your plants die!'''

def rain_amount(rain_amount):
    if (rain_amount >= 40):
         return "Your plant has had more than enough water for today!" 
    else:
        return "You need to give your plant " + str(40 - rain_amount) + "mm of water"


if __name__ == "__main__":
    

    # TEST CASES #

    print(rain_amount(100))
    #>>> "Your plant has had more than enough water for today!"
    print(rain_amount(40))
    #>>> "Your plant has had more than enough water for today!"
    print(rain_amount(39))
    #>>> "You need to give your plant 1mm of water"
    print(rain_amount(5))
    #>>> "You need to give your plant 35mm of water"
    print(rain_amount(0))
    #>>> "You need to give your plant 40mm of water"