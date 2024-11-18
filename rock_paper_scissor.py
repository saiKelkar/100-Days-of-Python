import random

rock = """
            -------
        ---,   ----)
              (----)
              (----)
        ___   (---)
           .--(--)
        """
    
paper = """
            -------
        ---,   ----)----
               ---------)
               -----------)
        ___    ---------)
           .----------)  
        """
scissor = """
            -------
        ---,   ----)----
               ---------)
               -----------)
        ___   (---)
           .--(--)    
        """

hands = [rock, paper, scissor]
outcomes = {
    0: {0: "It's a tie!", 1: "You lose!", 2: "You win!"},
    1: {0: "You win!", 1: "It's a tie!", 2: "You lose!"},
    2: {0: "You lose!", 1: "You win!", 2: "It's a tie!"}
}

player_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
program_num = random.randint(0, 2)

if player_num in [0, 1, 2]:
    print(hands[player_num])
    print("Computer choose: \n" + hands[program_num])

    result = outcomes[player_num][program_num]
    print(result)

else:
    print("Invalid input")

