'''Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!'''


def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    
    else:
        return "Player 2 won!"


if __name__ == "__main__":
    


    # TEST CASES #


    print(rps('rock', 'scissors'))
    print(rps('scissors', 'paper'))
    print(rps('paper', 'rock'))
    print(rps('scissors', 'rock'))
    print(rps('paper', 'scissors'))
    print(rps('rock', 'paper'))
    print(rps('rock', 'rock'))
    print(rps('scissors', 'scissors'))
    print(rps('paper', 'paper'))