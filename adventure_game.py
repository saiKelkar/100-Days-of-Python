print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
direction = input("    Type \"left\" or \"right\" \n").lower()

if direction == "right":
    print("Game Over.")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input("  Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if action == "swim": 
        print("Game Over.")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        color = input("  One red, one yellow and one blue. Which color do you choose? \n").lower()
        if color in ["red", "blue"]:
            print("Game Over.")
        elif color == "yellow":
            print("You Win!")
        else:
            print("Invalid input")

